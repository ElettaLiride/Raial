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

#include "writer.h"
hipo::writer *fWriter;

/* ================================================================= */
void PrintUsage(char *processName);

/* ================================================================ */
/* MAX number of hipo files */
#define MAXFILES 10000

/* ================================================================ */

int GetTriggerElectron(int jEle);
int GetRichPhoton(int g);
double nMinPhotons = 3;

#define nLayers 3
#define nMaxTiles 50
double Prob[nLayers][nMaxTiles];
void LoadTilePobabilities(int run);

TRandom3 rnd;
int nTotEvt[nLayers][nMaxTiles];


int SelectedLayer = -1;
int GoodLayer(int layer);

/******************************************/
int main(int argc, char** argv) {

  /* Filtering events for the alignment study in a new hipo */


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
      case 'L':
	SelectedLayer = atoi(++argptr);
	printf("Selected aerogel layer: %d\n", SelectedLayer);
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


  /* Loading weights per tile */
  LoadTilePobabilities(RunNumber);


  
  /* ===================================== */
  /* Some counters */
  int entry = 0;
  int nTriggers = 0;
  int nRec = 0;
  int nHad = 0;
  int nRich = 0;

  for (int l=0; l<nLayers; l++) {
    for (int t=0; t<nMaxTiles; t++) {
      nTotEvt[l][t] = 0;
    }
  }
  
  
  /* ===================================== */
  /* hipo4 object inizializations */
  fWriter = new hipo::writer();
 
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


    /* New hipo file */
    char outputFile[256];
    //sprintf(outputFile,"New_%s", inputFiles[l]);
    sprintf(outputFile,"rec_clas_%d_AIskim1.hipo", RunNumber);
    fWriter->addDictionary(*fFactory);
    fWriter->open(outputFile);

    


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

	      
	      /* Looking at the RICH */
	      if (RICH__hadCher->getRows() == 1) {
		int jHad = 0;
		get_RICH__hadCher(jHad);
		
		if (RICH__hadCher_pindex == jEle) {

		  /* Accepting the event of the tile */
		  int layer = RICH__hadCher_emilay;
		  int tile = 1 + RICH__hadCher_emico;
		  nTotEvt[layer][tile]++;
		  
		  double x = rnd.Uniform(0,1);
		  //printf("  layer %d  tile %d   P=%f  x=%f  \n", layer, tile, Prob[layer][tile], x);
		  if ( (x <= Prob[layer][tile]) && GoodLayer(layer) ) {
		    nHad++;


		    /* Looking at the photons */
		    if (RICH__ringCher->getRows()) {
		      int nPhotons = 0;

		      for (int g=0; g<RICH__ringCher->getRows(); g++) {
			if (GetRichPhoton(g)) {
			  nPhotons++;
			}
		      }

		      
		      /* Minimum number of photons */
		      if (nPhotons > nMinPhotons) {
			nRich++;
			
			fWriter->addEvent(*fEvent);
		      }

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

    
    /* Writing the new hipo file */
    fWriter->close();

    
  }
  printf("Total number of events:  %d \n", entry);
  printf("Number of triggers found: %d\n", nTriggers);
  printf("Number of rec. events: %d\n", nRec);
  printf("Number of RICH hadrons: %d\n", nHad);
  printf("Number of RICH events: %d\n", nRich);


  /* Printout of the total number of events for a new probability calculation */
  char fname[200];
  sprintf(fname,"rec_clas_%d_AIskim1_events.out", RunNumber);
  FILE *fOut = fopen(&fname[0], "w");
  for (int t=0; t<nMaxTiles; t++) {
    fprintf(fOut, "%2d  ", t+1);
    for (int l=0; l<nLayers; l++) {
      fprintf(fOut, "%8d  ", nTotEvt[l][t+1]);
    }
    fprintf(fOut, "\n");
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
  fprintf(stderr,"\t-L[#]\t\tSelecting aerogel layer (0/1/2)\n");



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
/* ==================================================== */
void LoadTilePobabilities(int run)
{

  /* Inizialization, all set to 1 */
  for (int l=0; l<nLayers; l++) {
    for (int t=0; t<nMaxTiles; t++) {
      Prob[l][t] = 1;
    }
  }


  /* Reading probabilities from file */
  char file[200];
  string RICHGEOAL(getenv("RICHGEOAL"));
  string tile_IB("config/TileWeights_IB.dat");
  string tile_OB("config/TileWeights_OB.dat");
  tile_IB = RICHGEOAL + tile_IB;
  tile_OB = RICHGEOAL + tile_OB;

  if ( (5030 < run) && (run < 5422) ) sprintf(file, "%s", tile_IB.c_str());
  else if ( (5422 < run) && (run < 5670) ) sprintf(file, "%s", tile_OB.c_str());
  else sprintf(file, "TileWeights.dat");
  
  FILE *fProb = fopen(&file[0], "r");
  if (fProb) {
    int tile;
    double p0, p1, p2;

    printf("Reading tile weigths from file %s\n", file);
    
    while (fscanf(fProb, "%d %lf %lf %lf", &tile, &p0, &p1, &p2) != EOF) {
      Prob[0][tile] = p0;
      Prob[1][tile] = p1;
      Prob[2][tile] = p2;
      //printf("   tile %d    P0=%f\n", tile, Prob[0][tile]);
    }


    fclose(fProb);
  }
  else {
    printf("ERROR: Cannot read tile weights from file %s, set to 1\n", file);
  }

  return;
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
/* ------------------------------------- */
int GoodLayer(int layer)
{

  if (SelectedLayer == -1) return 1;
  else {
    if (layer == SelectedLayer) return 1;
  }


  return 0;
}

