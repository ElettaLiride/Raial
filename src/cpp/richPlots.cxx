#include "Riostream.h"
#include "TApplication.h"
#include "TBenchmark.h"
#include "TROOT.h"
#include "TFile.h"
#include "TNtuple.h"
#include "TMath.h"
#include "TDatabasePDG.h"
#include "TParticlePDG.h"
#include <vector>
#include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

//#include<TFile.h>
//#include<TMath.h>
#include<TTree.h>
#include<TChain.h>
#include<TH2F.h>
#include<TF1.h>
#include<TVector3.h>
#include<TObject.h>
#include<TLorentzVector.h>
#include<TCanvas.h>
#include<TApplication.h>
#include<TRint.h>
#include<TStyle.h>
#include<TRandom3.h>
//#include <TROOT.h>

#include <TClonesArray.h>



/****************************************/
/* CLAS12 Bank definition */
//#include <Clas12Banks4.h>
#include "Clas12Banks4.h"

#define ElectronMass 0.000511

/* ================================================================= */
void PrintUsage(char *processName);

/* ================================================================ */
/* MAX number of hipo files */
#define MAXFILES 10000

/* ================================================================ */

int GetTriggerElectron(int jEle);
int GetRichPhoton(int g);
double nMinPhotons = 3;

/* ----------------------------------------------- */
void makeHistos();
TObjArray Hlist(0);

/* ----------------------------------------------- */
/* Loading the Aerogel nominal ref. index */

#define nAerogelLayers 3
/* max number of aerogel tile per layer (big number) */
#define MaxTilesN 50

#define nMaxRows 5
int nAerogelRows[nAerogelLayers];
int nAerogelTiles[nAerogelLayers];
int FirstTileOfTheRow[nAerogelLayers][nMaxRows];


double RefIndexCCDB[nAerogelLayers][MaxTilesN];

int LoadAerogelData();

/* minimum number of track in a tile for quality parameter estimate */
double nmin = 50;

/******************************************/
int main(int argc, char** argv) {

  /* produces histograms for the AI based alignment studies */

  char hname[200];


  /* number of input files */
  int nFiles = 0;
  /* max number of entries to read */
  int nEntries = 0;

  int RunNumber = 0;
  
  /* list of input file names */
  char inputFile[256];
  char *inputFiles[MAXFILES];

  /* output root file */
  char treeFile[256];


  /* ======================================== */
  /* Scanning the command line */
  char *argptr = NULL;
  
  if(argc == 1) {
    PrintUsage(argv[0]);
    exit(0);
  }
  
  
  for (int i=1; i<argc; i++) {
    argptr = argv[i];
    //cout << argv[i] << endl;
    
    if (*argptr == '-') {
      argptr++;

      switch (*argptr) {
	
	
      case 'n':
	nEntries = atoi(++argptr);
	printf("Reading %d entries per file\n", nEntries);
	break;
      case 'R':
	RunNumber = atoi(++argptr);
	printf("Run number: %d\n", RunNumber);
	break;
       default:
	fprintf(stderr, "Unrecognized argument: [-%s]\n\n", argptr);
	PrintUsage(argv[0]);
	break;
      }

    }
    else {
      
      sprintf(inputFile,"%s",argptr);

      inputFiles[nFiles] = (char*)malloc(256*sizeof(char));
      sprintf(inputFiles[nFiles], "%s", inputFile);
      nFiles++;
    }
    

  }

  if (RunNumber == 0) {
    printf("Please give the run number\n");
    return -1;
  }
  
  printf("Reading %d files\n", nFiles); 
  sprintf(treeFile, "richTree_%d.root", RunNumber);
  printf("Root file name:  %s \n", treeFile);

  /* ===================================== */
  if (!LoadAerogelData() ) {
    return -2;
  }

  /* ===================================== */
  /* Histograms */
  makeHistos();
  TH1F *h1;
  TH2F *h2;
  
  /* ===================================== */
  /* Some counters */
  int entry = 0;
  int nTriggers = 0;
  int nRec = 0;
  int nHad = 0;
  int nRich = 0;

  
  /* ===================================== */
  /* hipo4 object inizializations */
  fEvent = new hipo::event();
  fFactory = new hipo::dictionary();
  fReader = new hipo::reader();
 
  
  /* ====================================== */
  /* LOOP OVER THE HIPO FILES */
  for (int l=0; l<nFiles; l++) {
    printf("==>> READING HIPO FILE: %s\n", inputFiles[l]);
 
    /* opening the hipo4 file */
    //fReader->open(flist[f]);  TString input
    fReader->open(inputFiles[l]);

    /* Bank definition */
    fReader->readDictionary(*fFactory);
    InitBanks();



    /* looping over the current file */
    while( (fReader->next() )  && ( (entry < nEntries)||(nEntries == 0) ) ) {
      fReader->read(*fEvent);


       /* looking for CLAS12 banks */
      if (FillBanks() ) {

	/* looking for good triggers */
	if (RUN__config->getRows()) {
	  get_RUN__config(0);
	  nTriggers++;

	  /* reconstructed events */
	  if (REC__Event->getRows()) {

	    //printf("==================== Event %d    np=%d  =========\n", RUN__config_event, REC__Particle->getRows());


	    /* Looking for a trigger electron */
	    int jEle = 0;
	    if ( GetTriggerElectron(jEle) ) {
	      nRec++;

	      
	      get_REC__Particle(jEle);
	      TLorentzVector Pele;
	      Pele.SetXYZM(REC__Particle_px, REC__Particle_py, REC__Particle_pz, ElectronMass);
	      
	      /* Looking at the RICH */
	      if (RICH__hadCher->getRows() == 1) {
		int jHad = 0;
		get_RICH__hadCher(jHad);
		
		if (RICH__hadCher_pindex == jEle) {
		  nHad++;

		  int layer = RICH__hadCher_emilay;
		  int tile = 1 + RICH__hadCher_emico;
		  double refIndex = RefIndexCCDB[layer][tile];
		  double etacCCDB = 0;
		  if (refIndex*Pele.Beta() > 1) {
		    etacCCDB = TMath::ACos(1. / (refIndex*Pele.Beta()) );
		  }

		  /* looking at RICH::response for track matching with RICH */
		  double chi2 = -1;
		  if (RICH__response->getRows()) {
		    int jResp = 0;
		    get_RICH__response(jResp);
		    chi2 = RICH__response_chi2;
		    
		  }
		  //printf("RICH::response:  nrows=%d    chi2=%f\n", RICH__response->getRows(), chi2);


		  /* Looking at the photons */
		  if (RICH__ringCher->getRows()) {
		    int nPhotons = 0;
		    double AveEtaC = 0;
		    
		    for (int g=0; g<RICH__ringCher->getRows(); g++) {
		      if (GetRichPhoton(g)) {
			get_RICH__ringCher(g);
			AveEtaC = (RICH__ringCher_tEtaC + nPhotons*AveEtaC) / (nPhotons + 1);
			nPhotons++;
		      }
		    }
		    
		    
		    /* Minimum number of photons */
		    if (nPhotons > nMinPhotons) {
		      nRich++;

		      sprintf(hname, "hThetaVsP");
		      gDirectory->GetObject(hname, h2);
		      h2->Fill(Pele.Vect().Mag(), Pele.Vect().Theta()*TMath::RadToDeg());

		      sprintf(hname, "hNtrkVsTile");
		      gDirectory->GetObject(hname, h2);
		      h2->Fill(tile, layer);

		      sprintf(hname, "hNphotonsVsTile_l%d", layer);
		      gDirectory->GetObject(hname, h2);
		      h2->Fill(nPhotons, tile);


		      if (chi2 >= 0) {
			sprintf(hname, "hRichMatchChi2");
			gDirectory->GetObject(hname, h1);
			h1->Fill(chi2);
		      }

			
		      sprintf(hname, "hDEtacVsTile_l%d", layer);
		      gDirectory->GetObject(hname, h2);
		      h2->Fill(1000.*(AveEtaC-etacCCDB), tile);

		    }
		  }
		  
		}
	      }/* END good RICH particle */
	      
	      
	    }/* END good trigger electron */
	    
	    
	  }/* END event with reconstructed particles */
	  
	  
	}
      }/* END event with CLAS12 banks */

      entry++;
      if ( (entry%1000) == 0) {
	fprintf(stdout, "%d  %d  %d  %d  %d\r", entry, nTriggers, nRec, nHad, nRich);
	fflush(stdout);	

	//fWriter->showSummary();
      }


    }/* END loop over the current file */

    
  }


  
  /* ==================================== */
  /* Writing histograms */
  TFile f(Form("RichPlots_%d.root", RunNumber), "RECREATE");
  Hlist.Write();
  f.Close();



  
  /* ==================================== */
  printf("Total number of events:  %d \n", entry);
  printf("Number of triggers found: %d\n", nTriggers);
  printf("Number of rec. events: %d\n", nRec);
  printf("Number of RICH hadrons: %d\n", nHad);
  printf("Number of RICH events: %d\n", nRich);


  /* =================================== */
  /* Writing the alignment quality factors */
  FILE *fOut = fopen(Form("RichPlots_%d.out", RunNumber), "w");
  printf("---------------------------------------- \n");
  sprintf(hname, "hRichMatchChi2");
  gDirectory->GetObject(hname, h1);
  printf("Track Matching:  chi2=%f\n", h1->GetMean());
  fprintf(fOut, "Track Matching:  chi2=%f\n", h1->GetMean());
  
  printf("---------------------------------------- \n");
  for (int l=0; l<nAerogelLayers; l++) {
    sprintf(hname, "hDEtacVsTile_l%d", l);
    gDirectory->GetObject(hname, h2);
    for (int t=0; t<MaxTilesN; t++) {
      h2->ProjectionX("_px", t, t);
      TH1F *h2_px = (TH1F*)gDirectory->GetList()->FindObject(Form("%s_px", h2->GetName()));
      if (h2_px) {
	if (h2_px->GetEntries() > nmin) {
	  printf("Layer %d tile %d   dEtaC=%f\n", l, t+1, h2_px->GetMean());
	  fprintf(fOut, "Layer %d tile %d   dEtaC=%f\n", l, t+1, h2_px->GetMean());
	}
      }
    }
    
    
  }

  fclose(fOut);
  
  
  return 1;
}
/* ===================================================== */
void PrintUsage(char *processName)
{
  fprintf(stderr,"Usage: %s [-Options] \n\n",processName);
  fprintf(stderr,"  Options:\n");

  fprintf(stderr,"\t-n[#]\t\tMax number of entries\n");
  fprintf(stderr,"\t-R[#]\t\tRun number\n");


  exit(0);
}
/* ------------------------------------------------------ */
int GetTriggerElectron(int jEle)
{

  get_REC__Particle(jEle);

  /* PID number */
  if (REC__Particle_pid != 11) return 0;
    
  /* Momentum */
  TVector3 P(REC__Particle_px, REC__Particle_py, REC__Particle_pz);
  double pmin = 2.;
  double pmax = 8.;
    
  if ( (pmin > P.Mag()) || (P.Mag() > pmax) ) return 0;

  /* status */
  if (REC__Particle_status >= 0) return 0;

  /* DC chi2 */
  double chi2min = 0;
  double chi2max = 10;
  double chi2 = -1;
  if (REC__Track->getRows()) {
    for (int t=0; t<REC__Track->getRows(); t++) {
      get_REC__Track(t);
      
      if (REC__Track_pindex == jEle) {
	if (REC__Track_NDF > 0) chi2 = REC__Track_chi2 / REC__Track_NDF;
	
	break;
      }
    }

    
  }

  if ( (chi2min > chi2) || (chi2 > chi2max) ) return 0;
  


  return 1;
}
/* ---------------------------------------------- */
int GetRichPhoton(int g)
{
  get_RICH__ringCher(g);

  /* Good Cherenkov angle */
  if (RICH__ringCher_tEtaC <= 0) return 0;


  /* direct photons */
  if (RICH__ringCher_nrfl > 0) return 0;

  /* time cut */
  double dtimeCut = 2;

  double dtime = RICH__ringCher_ttime - RICH__ringCher_time;
  if (TMath::Abs(dtime) > dtimeCut) return 0;
  
  
  return 1;
}
/* ---------------------------------------------- */
void makeHistos()
{
  char htitle[200];
  char hname[200];


  /* Deleting old histograms */
  gDirectory->Clear();

  /* momentum binning */
  double pmin = 0.;
  double pmax = 10.;
  int np = 100;

  /* track theta binning */
  double trktmin = 0.;
  double trktmax = 30.;
  int ntrkt = 90;

  /* kinematics of the particles */
  sprintf(hname, "hThetaVsP");
  sprintf(htitle, "Track #theta vs Momentum");
  TH2F *hThetaVsP = new TH2F(hname, htitle, np, pmin, pmax, ntrkt, trktmin, trktmax);
  Hlist.Add(hThetaVsP);

  /* number of tracks per tile */
  sprintf(hname, "hNtrkVsTile");
  sprintf(htitle, "Number of Tracks per tile");
  TH2F *hNtrkVsTile = new TH2F(hname, htitle, MaxTilesN, 0.5, 0.5+MaxTilesN, nAerogelLayers, -0.5, -0.5+nAerogelLayers);
  Hlist.Add(hNtrkVsTile);
  


  /* Matching between the track and the RICH clusters */
  sprintf(hname, "hRichMatchChi2");
  sprintf(htitle, "Matching between the track and the RICH cluster, #chi^{2}");
  TH1F *hRichMatchChi2 = new TH1F(hname, htitle, 200, 0., 20);
  Hlist.Add(hRichMatchChi2);


  /* Cherenkov angle difference per tile */
  for (int l=0; l<nAerogelLayers; l++) {
    sprintf(hname, "hDEtacVsTile_l%d", l);
    sprintf(htitle, "#theta_{C}(RICH)-#theta_{C}(CCDB) (mrad) per tile, Layer %d", l);
    TH2F *hDEtacVsTile = new TH2F(hname, htitle, 200, -50, 50, MaxTilesN, 0.5, 0.5+MaxTilesN);
    Hlist.Add(hDEtacVsTile);

    sprintf(hname, "hNphotonsVsTile_l%d", l);
    sprintf(htitle, "Number of photons per tile, Layer %d", l);
    TH2F *hNphotonsVsTile = new TH2F(hname, htitle, 100, -0.5, 99.5, MaxTilesN, 0.5, 0.5+MaxTilesN);
    Hlist.Add(hNphotonsVsTile);

  }
  

  return;
}


/* --------------------------------------------------- */
int LoadAerogelData()
{
  /* Loading Cherenkov angle data, nominal values from CCDB */
  
  /* Soma aerogel geometry numbers */
  
  /* First layer (2 cm) */
  FirstTileOfTheRow[0][0] = 1;
  FirstTileOfTheRow[0][1] = 3;
  FirstTileOfTheRow[0][2] = 7;
  FirstTileOfTheRow[0][3] = 11;
  FirstTileOfTheRow[0][4] = 17;
  nAerogelRows[0] = 4;
  nAerogelTiles[0] = 16;
  
  /* Second layer (2 cm) */
  FirstTileOfTheRow[1][0] = 1;
  FirstTileOfTheRow[1][1] = 7;
  FirstTileOfTheRow[1][2] = 15;
  FirstTileOfTheRow[1][3] = 23;
  FirstTileOfTheRow[1][4] = 0;
  nAerogelRows[1] = 3;
  nAerogelTiles[1] = 22;
  
  /* Third layer (3 cm) */
  FirstTileOfTheRow[2][0] = 1;
  FirstTileOfTheRow[2][1] = 11;
  FirstTileOfTheRow[2][2] = 21;
  FirstTileOfTheRow[2][3] = 33;
  FirstTileOfTheRow[2][4] = 45;
  nAerogelRows[2] = 4;
  nAerogelTiles[2] = 44;


  /* Default values */
  for (int l=0; l<nAerogelLayers; l++) {
    for (int t=0; t<MaxTilesN; t++) {
      RefIndexCCDB[l][t] = 0;

    }

  }

  
  
  /* Reading the ccdb data */
  string RICHGEOAL(getenv("RICHGEOAL"));
  string aerogel_dat("config/Aerogel_ccdb.dat");
  aerogel_dat = RICHGEOAL + aerogel_dat;

  FILE *fCCDB = fopen(aerogel_dat.c_str(), "r");
  if (fCCDB) {
    printf("Reading aerogel CCDB\n");
    int layer, tile, sector, thick;
    double val[12];
    while (fscanf(fCCDB, "%d %d %d %d", &sector, &layer, &tile, &thick) != EOF) {
      
      //for (int v=0; v<11; v++) fscanf(fCCDB, "%lf ", &val[v]);
      for (int v=0; v<9; v++) fscanf(fCCDB, "%lf ", &val[v]);
      int l = layer - 201;
      int t = tile;
      if (l < 3) {
	RefIndexCCDB[l][t] = val[0];
      }
      else {
	/* For 3 cm, Average of layer 203 and 204 */
	RefIndexCCDB[l-1][t] = 0.5*(RefIndexCCDB[l-1][t] + val[0]);
      }
    }

    fclose(fCCDB);
    return 1;
  }
  else {
    printf("-->> Warning: Cannot read ccdb aerogel data\n");
  }


  

  return 0;
}
