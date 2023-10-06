#include <iostream>
#include <sstream>
#include <istream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
#include <functional>
#include <vector>
#include <cassert>
#include "TMath.h"
using namespace std;
#include "TStyle.h"
#include "TGraph.h"
#include "TCanvas.h"
#include "TGraphAsymmErrors.h"
#include "TAxis.h"
#include "TFrame.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TFile.h"
#include "TDirectoryFile.h"
#include "TH1D.h"
#include "TApplication.h"
#include "TMatrixD.h"
#include "TF1.h"
#include "TRootCanvas.h"
#include "TH2F.h"
#include "TH2Poly.h"
#include "TLine.h"
#include "TTree.h"
#include <algorithm>

//#include "/mnt/storage/shared/PATClass.C"
#include "/mnt/storage/shared/DTTFStudies/RECOClass.C"
#include "/mnt/storage/shared/DTTFStudies/GENClass.C"


// tdrGrid: Turns the grid lines on (true) or off (false)

// void tdrGrid(bool gridOn) {
//   TStyle *tdrStyle;
//   tdrStyle->SetPadGridX(gridOn);
//   tdrStyle->SetPadGridY(gridOn);
// }


// fixOverlay: Redraws the axis

void fixOverlay() {
  gPad->RedrawAxis();
}


void setTDRStyle() {
  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

// For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

// For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

// For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);




// For the histo:
  // tdrStyle->SetHistFillColor(1);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Double_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

  tdrStyle->SetEndErrorSize(2);
//**  tdrStyle->SetErrorMarker(20);
  tdrStyle->SetErrorX(0.5);
  
  tdrStyle->SetMarkerStyle(20);

//For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

//For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Double_t x = 0.01);
  // tdrStyle->SetDateY(Double_t y = 0.01);

// For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Double_t x = 0);
  // tdrStyle->SetStatY(Double_t y = 0);

// Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.16);
  tdrStyle->SetPadRightMargin(0.02);

// For the Global title:

  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

// For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Double_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Double_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.25);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

// For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

// For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

// Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

// Postscript options:
  tdrStyle->SetPaperSize(20.,20.);
  // tdrStyle->SetLineScalePS(Double_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Double_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Double_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

  tdrStyle->cd();


}



int genreco(){


//  setTDRStyle();
//  gStyle->SetPalette(1);
  GENClass genc;
  RECOClass recoc;

  TFile *f ;
  f = new TFile("../test/Tree_from_RECO.root");//Tree_from_RAW.root");
  f->cd("../test/Tree_from_RECO.root:/RECOTProducer");
  TTree *tree;
  tree = (TTree*)gDirectory->Get("RECOTree");
  recoc.Init(tree);

  f->cd("../test/Tree_from_RECO.root:/GENTProducer");
  TTree *tree1;
  tree1 = (TTree*)gDirectory->Get("GENTree");
  genc.Init(tree1);


  TH1F *genpt_histo = new TH1F("Gen Pt Histogramm", "GPH", 400,0,2000);
  TH1F *recopt_histo = new TH1F("RECO Pt Histogramm", "RPH", 400,0,2000);

  TH2F *reco_vs_gen = new TH2F("RECO VS GEN Pt Histogramm", "RGPH", 400,0,2000, 400,0,2000);




int nentries = genc.fChain -> GetEntries();
float gen_pt, rec_pt;
bool tight_reco;

vector<float> pt_gen, pt_rec, eta_gen, eta_rec, phi_gen, phi_rec;
//bool tight;

for(int i=0; i<nentries; i++){
	int sizeg =0, sizer=0;

	genc.GetEntry(i);
	recoc.GetEntry(i);

	sizeg = genc.genPt_Mu.size();
	sizer = recoc.recoPt_Mu.size();
        pt_gen.clear();
        eta_gen.clear();
        phi_gen.clear();
 
 	pt_rec.clear();
	eta_rec.clear();	
	phi_rec.clear();
		for(int j=0; j<sizeg; j++)
		{
		gen_pt=0;
		gen_pt = genc.genPt_Mu[j];

		//tight = genc.
		if(gen_pt>0. ) {
		genpt_histo->Fill(gen_pt);
		pt_gen.push_back(gen_pt);
		eta_gen.push_back(genc.genEta_Mu[j]);
		phi_gen.push_back(genc.genPhi_Mu[j]);
		}

		}

		for(int j=0; j<sizer; j++)
		{
		tight_reco = false;
		rec_pt = 0;
		rec_pt = recoc.recoPt_Mu[j];
		tight_reco = recoc.isTight_Mu[j];
		//tight = genc.
		if(rec_pt>0.  && tight_reco) {

		recopt_histo->Fill(rec_pt);
		pt_rec.push_back(rec_pt);
		eta_rec.push_back(recoc.recoEta_Mu[j]);
		phi_rec.push_back(recoc.recoPhi_Mu[j]);


		}

		}
		if(pt_rec.size() == pt_gen.size()){
		float dr = 0.;
		for(int ii=0; ii<pt_gen.size(); ii++){
		dr=0;
		dr=sqrt(pow((eta_rec[ii]-eta_gen[ii]),2)+pow((phi_rec[ii]-phi_gen[ii]),2));
		//cout<<dr<<" "<<eta_rec[ii]<<" "<<eta_gen[ii]<<endl;
		if(dr<0.5)	reco_vs_gen->Fill(pt_rec[ii],pt_gen[ii]);	
		}

		}


}

TFile f1("./ROOTFiles/reco_gen.root", "NEW");
genpt_histo->Write();
recopt_histo->Write();
reco_vs_gen->Write();
f1.Close();


return 0;
}
