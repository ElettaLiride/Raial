#include "TF1.h"

#include "TH1.h"
#include "TH2D.h"
#include "TH2I.h"

#include "TH2.h"

#include "TROOT.h"
#include "TRint.h"

#include "TStyle.h"
#include "TLatex.h"

#include "stdio.h"


#include "TLorentzVector.h"
#include "TVector3.h"

#include "math.h"

#include "TFile.h"

#include "TGraph.h"
#include "TGraphErrors.h"
#include "TLine.h"

#include "TLegend.h"
#include "TCanvas.h"

#include <TSpectrum.h>

/* ================================ */


#define nAerogelLayers 3
/* max number of aerogel tile per layer (big number) */
#define MaxTilesN 50

#define nMaxRows 5
int nAerogelRows[nAerogelLayers];
int nAerogelTiles[nAerogelLayers];
int FirstTileOfTheRow[nAerogelLayers][nMaxRows];

int TilePosition[nAerogelLayers][MaxTilesN];


double RefIndexCCDB[nAerogelLayers][MaxTilesN];

int LoadAerogelData();


/* ======================================================= */
void DrawRichPlots(const char *fileHist)
{



  Char_t fname[100];
  Char_t hname[100];
  Char_t hname2[100];
  Char_t title[100];
  Char_t htitle[100];


  LoadAerogelData();



  /******************************************/
  /* Opening root histogram file */
  TFile *fHist = new TFile(fileHist);
  if (fHist->IsZombie()) {
    cout << "  error: No file " << fileHist << endl;
    return;
  }



  /******************************************/
  /* per legende */
  double sizeTXT = 0.04;
  double dxLeg = 0.5;
  double x1Leg, x2Leg;
  
  double dyLeg = 0.04;
  double y2Leg, y1Leg;

  x1Leg = 0.65;
  x2Leg = x1Leg + dxLeg;
  y2Leg = 0.9;
  y1Leg = y2Leg - dyLeg;


  int color;
  int marker;
  double size;




  /********************************************/
  /* Root canvas */
  TCanvas *c1 = new TCanvas("c1");
  int nx = 3;
  int ny = 3;
  c1->Divide(nx, ny);

  TCanvas *c2 = new TCanvas("c2"); 
  c2->Divide(2, 2);

  TCanvas *c3 = new TCanvas("c3"); 


  /* For the maps */
  int nxb[nAerogelLayers], nyb[nAerogelLayers];

  TCanvas *c1b[nAerogelLayers];
  for (int l=0; l<nAerogelLayers; l++) {
    c1b[l] = new TCanvas(Form("cl%d", l), "", 1);
    nyb[l] = nAerogelRows[l];
    nxb[l] = FirstTileOfTheRow[l][nAerogelRows[l]] - FirstTileOfTheRow[l][nAerogelRows[l]-1];
    printf("Layer %d:  nx=%d  ny=%d\n", l, nxb[l], nyb[l]);
    c1b[l]->Divide(nxb[l], nyb[l]);
  }


  
  /*******************************************************/
  /* file pdf */ 
  sprintf(fname, "%s.pdf", fileHist);
  c1->Print(Form("%s[", fname));




  /*******************************************************/
  /* PLOTS */
  /*******************************************************/


  /* ---------------------------------------------- */
  /* P vs Theta of the particles */
  c3->cd();
  gStyle->SetOptStat(11);

  sprintf(hname, "hThetaVsP");
  TH2F *hThetaVsP = (TH2F*)fHist->Get(hname);
  hThetaVsP->Draw("colz");

  c3->Print(Form("%s", fname));


  /* ---------------------------------------------- */
  /* number of tracks per tile */
  c3->cd();
  gStyle->SetOptStat(11);

  sprintf(hname, "hNtrkVsTile");
  TH2F *hNtrkVsTile = (TH2F*)fHist->Get(hname);
  hNtrkVsTile->Draw("colz");

  c3->Print(Form("%s", fname));

  /* projections per layer */
  for (int l=0; l<nAerogelLayers; l++) {
    c3->cd();
    gStyle->SetOptStat(1111);
   
    hNtrkVsTile->ProjectionX("_px", l+1, l+1);
    TH1F *hNtrkVsTile_px = (TH1F*)gDirectory->GetList()->FindObject(Form("%s_px", hNtrkVsTile->GetName()));
    if (hNtrkVsTile_px) {
      hNtrkVsTile_px->SetName(Form("%s_l%d", hNtrkVsTile->GetName(), l));
      hNtrkVsTile_px->SetTitle(Form("%s, Layer %d", hNtrkVsTile->GetTitle(), l));
      if (hNtrkVsTile_px->GetEntries()) {
        hNtrkVsTile_px->Draw();
        c3->Print(Form("%s", fname));
      }
    }

  }
  


  /* ---------------------------------------------- */
  /* number of photons per tile */
  
  for (int l=0; l<nAerogelLayers; l++) {
    //for (int l=0; l<=0; l++) {
    
    sprintf(hname, "hNphotonsVsTile_l%d", l);
    TH2F *hNphotonsVsTile = (TH2F*)fHist->Get(hname);
    
    if (hNphotonsVsTile->GetEntries()) {
      
      /* loop over the rows of the layer */
      for (int r=0; r<nAerogelRows[l]; r++) {

        /* loop over the tiles of the row */
        for (int t=FirstTileOfTheRow[l][r]; t<FirstTileOfTheRow[l][r+1]; t++) {
          
          //printf("Layer %d   row %d  tile %d   pos %d\n", l, r, t, TilePosition[l][t]);
          
          c1b[l]->cd(TilePosition[l][t]);
          gStyle->SetOptStat(1111);
          
          hNphotonsVsTile->ProjectionX("_px", t, t);
          TH1F *hNphotonsVsTile_px = (TH1F*)gDirectory->GetList()->FindObject(Form("%s_px", hNphotonsVsTile->GetName()));
          if (hNphotonsVsTile_px) {
            hNphotonsVsTile_px->SetName(Form("%s_t%d", hNphotonsVsTile->GetName(), t));
            hNphotonsVsTile_px->SetTitle(Form("%s, tile %d", hNphotonsVsTile->GetTitle(), t));
            hNphotonsVsTile_px->GetXaxis()->SetRangeUser(-0.5, 49.5);
            hNphotonsVsTile_px->Draw();
          }
          
          
          
        }

      }
      
      
      c1b[l]->Print(Form("%s", fname));
    }
    
  }


  /* ---------------------------------------------- */
  /* Track matching with RICH cluster */
  c3->cd();
  gStyle->SetOptStat(1111);

  sprintf(hname, "hRichMatchChi2");
  TH1F *hRichMatchChi2 = (TH1F*)fHist->Get(hname);
  hRichMatchChi2->Draw();

  c3->Print(Form("%s", fname));
 

  /* ---------------------------------------------- */
  /* Cherenkov angle per tile */
   
  for (int l=0; l<nAerogelLayers; l++) {
    //for (int l=0; l<=0; l++) {
    
    sprintf(hname, "hDEtacVsTile_l%d", l);
    TH2F *hDEtacVsTile = (TH2F*)fHist->Get(hname);

    TLine *Zero[MaxTilesN];
    
    if (hDEtacVsTile->GetEntries()) {
      
      /* loop over the rows of the layer */
      for (int r=0; r<nAerogelRows[l]; r++) {

        /* loop over the tiles of the row */
        for (int t=FirstTileOfTheRow[l][r]; t<FirstTileOfTheRow[l][r+1]; t++) {
          
          //printf("Layer %d   row %d  tile %d   pos %d\n", l, r, t, TilePosition[l][t]);
          
          c1b[l]->cd(TilePosition[l][t]);
          gPad->SetGrid();
          gStyle->SetOptStat(1111);
          
          hDEtacVsTile->ProjectionX("_px", t, t);
          TH1F *hDEtacVsTile_px = (TH1F*)gDirectory->GetList()->FindObject(Form("%s_px", hDEtacVsTile->GetName()));
          if (hDEtacVsTile_px) {
            hDEtacVsTile_px->SetName(Form("%s_t%d", hDEtacVsTile->GetName(), t));
            hDEtacVsTile_px->SetTitle(Form("%s, tile %d", hDEtacVsTile->GetTitle(), t));
            //hDEtacVsTile_px->GetXaxis()->SetRangeUser(-0.5, 25.5);
            hDEtacVsTile_px->Draw();

            Zero[t] = new TLine(0, 0, 0, hDEtacVsTile_px->GetMaximum());
            Zero[t]->SetLineColor(2);
            Zero[t]->Draw("same");
            
          }
          
          
          
        }

      }
      
      
      c1b[l]->Print(Form("%s", fname));
    }
    
  }



  /******************************************/
  c1->Print(Form("%s]", fname));
  c1->Close();
  c2->Close();
  c3->Close();

  
  for (int l=0; l<nAerogelLayers; l++) {
    c1b[l]->Close();
  }

  fHist->Close();

  gDirectory->Clear();
  
  return;
}
/* --------------------------------------------------- */
int LoadAerogelData()
{
  /* Loading Cherenkov angle data, nominal values from CCDB */
  
  /* Some aerogel geometry numbers */
  
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

  /* Set the position of the tile in the aerogel wall 
     It is used to make a vertical canvas per layer
  */

  /* First layer (2 cm) */
  TilePosition[0][1] = 21;
  TilePosition[0][2] = 22;

  TilePosition[0][3] = 14;
  TilePosition[0][4] = 15;
  TilePosition[0][5] = 16;
  TilePosition[0][6] = 17;

  TilePosition[0][7] = 8;
  TilePosition[0][8] = 9;
  TilePosition[0][9] = 10;
  TilePosition[0][10] = 11;

  TilePosition[0][11] = 1;
  TilePosition[0][12] = 2;
  TilePosition[0][13] = 3;
  TilePosition[0][14] = 4;
  TilePosition[0][15] = 5;
  TilePosition[0][16] = 6;


  /* second layer (2 cm) */
  TilePosition[1][1] = 18;
  TilePosition[1][2] = 19;
  TilePosition[1][3] = 20;
  TilePosition[1][4] = 21;
  TilePosition[1][5] = 22;
  TilePosition[1][6] = 23;

  TilePosition[1][7] = 9;
  TilePosition[1][8] = 10;
  TilePosition[1][9] = 11;
  TilePosition[1][10] = 12;
  TilePosition[1][11] = 13;
  TilePosition[1][12] = 14;
  TilePosition[1][13] = 15;
  TilePosition[1][14] = 16;
  
  TilePosition[1][15] = 1;
  TilePosition[1][16] = 2;
  TilePosition[1][17] = 3;
  TilePosition[1][18] = 4;
  TilePosition[1][19] = 5;
  TilePosition[1][20] = 6;
  TilePosition[1][21] = 7;
  TilePosition[1][22] = 8;


  /* third layer (3+3 cm) */
  TilePosition[2][1] = 38;
  TilePosition[2][2] = 39;
  TilePosition[2][3] = 40;
  TilePosition[2][4] = 41;
  TilePosition[2][5] = 42;
  TilePosition[2][6] = 43;
  TilePosition[2][7] = 44;
  TilePosition[2][8] = 45;
  TilePosition[2][9] = 46;
  TilePosition[2][10] = 47;

  TilePosition[2][11] = 26;
  TilePosition[2][12] = 27;
  TilePosition[2][13] = 28;
  TilePosition[2][14] = 29;
  TilePosition[2][15] = 30;
  TilePosition[2][16] = 31;
  TilePosition[2][17] = 32;
  TilePosition[2][18] = 33;
  TilePosition[2][19] = 34;
  TilePosition[2][20] = 35;

  TilePosition[2][21] = 13;
  TilePosition[2][22] = 14;
  TilePosition[2][23] = 15;
  TilePosition[2][24] = 16;
  TilePosition[2][25] = 17;
  TilePosition[2][26] = 18;
  TilePosition[2][27] = 19;
  TilePosition[2][28] = 20;
  TilePosition[2][29] = 21;
  TilePosition[2][30] = 22;
  TilePosition[2][31] = 23;
  TilePosition[2][32] = 24;

  TilePosition[2][33] = 1;
  TilePosition[2][34] = 2;
  TilePosition[2][35] = 3;
  TilePosition[2][36] = 4;
  TilePosition[2][37] = 5;
  TilePosition[2][38] = 6;
  TilePosition[2][39] = 7;
  TilePosition[2][40] = 8;
  TilePosition[2][41] = 9;
  TilePosition[2][42] = 10;
  TilePosition[2][43] = 11;
  TilePosition[2][44] = 12;



  
  /* Default CCDB values set to 0 */
  for (int l=0; l<nAerogelLayers; l++) {
    for (int t=0; t<MaxTilesN; t++) {
      RefIndexCCDB[l][t] = 0;

    }

  }

  
  
  /* Reading the ccdb data */
  FILE *fCCDB = fopen("Aerogel_ccdb.dat", "r");
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
