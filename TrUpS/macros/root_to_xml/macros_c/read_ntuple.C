#include <vector>
#include <iostream>
#include <emu.C>
#include <mp7.C>
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
using namespace std;
int read_ntuple(TString infile){

  
emu t;
mp7 tmp7;



TFile *f = new TFile(infile);
//irectory *diremu = new (TDirectory*)(infile+":/Emulator");
//TDirectory *dirmp7 = new (TDirectory*)(infile+":/MP7");
TTree *t_emu;
TTree *t_mp7;
f->GetObject("Emulator",t_emu);
f->GetObject("MP7",t_mp7);

t.Init(t_emu);
tmp7.Init(t_mp7);





//      //      if (!f || !f->IsOpen()) {
//      //         f = new TFile("./new_file.root");
//      //      }
//      //      f->GetObject("Emulator",tree);
//      


int netr = t.fChain->GetEntries();
int diffs = 0;

for(int i=0; i<netr; i++){
  t.GetEntry(i);
  tmp7.GetEntry(i);
  
  vector<float> emu_pt = t.pt[0];
  vector<float> mp7_pt = tmp7.pt[0];
  
  
  float diff = emu_pt[0] - mp7_pt[0];
  if(diff != 0 ) {cout<<i<<"  "<<emu_pt[0]<<"  "<<mp7_pt[0]<<endl; diffs++;};
  
  
}
cout<<endl<<diffs<<endl;
return 0;
}
