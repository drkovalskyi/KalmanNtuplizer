//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Apr  1 11:26:32 2016 by ROOT version 6.06/01
// from TTree EVRTree/EVRTree
// found on file: Ntuple_BMTF_data_Run267878.root
//////////////////////////////////////////////////////////

#ifndef Event_h
#define Event_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
//#include "UIoannina/TrUpS/interface/EventRunDataFormat.h"

class Event {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
 //TrUpS::EventRunDataFormat *EventRun;
   Int_t           pvertex;
   Int_t           run;
   Int_t           event;
   Int_t           lumi;
   Int_t           bunch;

   // List of branches
   TBranch        *b_EventRun_pvertex;   //!
   TBranch        *b_EventRun_run;   //!
   TBranch        *b_EventRun_event;   //!
   TBranch        *b_EventRun_lumi;   //!
   TBranch        *b_EventRun_bunch;   //!

   Event(TTree *tree=0);
   virtual ~Event();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

Event::Event(TTree *tree) : fChain(0) 
{

   Init(tree);
}

Event::~Event()
{
   if (!fChain) return;
}

Int_t Event::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Event::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Event::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("pvertex", &pvertex, &b_EventRun_pvertex);
   fChain->SetBranchAddress("run", &run, &b_EventRun_run);
   fChain->SetBranchAddress("event", &event, &b_EventRun_event);
   fChain->SetBranchAddress("lumi", &lumi, &b_EventRun_lumi);
   fChain->SetBranchAddress("bunch", &bunch, &b_EventRun_bunch);
   Notify();
}

Bool_t Event::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Event::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Event::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Event_cxx
