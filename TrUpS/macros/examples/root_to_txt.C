#include <iostream>

#include "TH1F.h"
#include "TFile.h"
#include "TDirectory.h"
#include "TTree.h"
#include "TCanvas.h"

#include "L1TreeClass.h"
#include "GENTreeClass.h"

using namespace std;

void root_to_txt(){ 

    TFile* f1 = new TFile("Ntuple_test.root");
    
    ///L1Tree    
    TDirectory* dirl1 = (TDirectory*)f1->Get("L1TProducer");
    TTree* treel1 = (TTree*)dirl1->Get("L1Tree");

    L1TreeClass l1TC;
    l1TC.Init(treel1);

    ///GENTree    
    TDirectory* dir_gen = (TDirectory*)f1->Get("GENTProducer");
    TTree* gen_tree = (TTree*)dir_gen->Get("GENTree");

    GENTreeClass GENTC;
    GENTC.Init(gen_tree); 
    
    
    int nentries = l1TC.fChain->GetEntries();
    cout<<"Reading L1Tree with:\t"<<nentries<<"\tentries"<<endl;
     
    ///Declare a histogram
    TH1F* h1 = new TH1F("h1","h1",280,0,280);
    TH1F* h2 = new TH1F("h2","h2",280,0,280);

    for(int i=0; i<nentries; i++){
       l1TC.GetEntry(i);
       GENTC.GetEntry(i);

       if(l1TC.bmtfqual[0]!=7) continue;
       
       cout<<l1TC.phAng[0]<<"\t"<<l1TC.phBandAng[0]<<"\t"<<l1TC.phAng[1]<<"\t"<<l1TC.phBandAng[1]<<"\t"<<l1TC.phAng[2]<<"\t"<<l1TC.phBandAng[2]<<"\t"<<l1TC.phAng[3]<<"\t"<<l1TC.phBandAng[3]<<"\t"<<GENTC.genPt_Mu[0]<<endl;
       
       /*
       ///Read size and loop over GEN
       cout<<GENTC.gen_muons<<endl;
       	for(int mu=0; mu<GENTC.gen_muons; mu++){
		cout<<"Pt = "<<GENTC.genPt_Mu[mu]<<endl;
                //Fill the histogram
	        h1->Fill(GENTC.genPt_Mu[mu]);
	}///End of reading GEN	

       
       ///Read size and loop over BMTF
       cout<<"BMTF Size: "<<l1TC.bmtfSize<<endl;
       	for(int mu=0; mu<l1TC.bmtfSize; mu++){
		cout<<"Pt = "<<l1TC.bmtfPt[mu]<<endl;
                //Fill the histogram
	        h2->Fill(l1TC.bmtfPt[mu]);
	}///End of reading BMTF	
*/
    }///End loop of nentries

    TCanvas *c1 = new TCanvas("c1","c1",800,600);
    c1->cd();
    h1->Draw();
    
    TCanvas *c2 = new TCanvas("c2","c2",800,600);
    c2->cd();
    h2->Draw();
 
}