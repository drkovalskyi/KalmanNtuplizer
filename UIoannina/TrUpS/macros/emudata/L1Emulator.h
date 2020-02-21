//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Mar  3 17:38:12 2016 by ROOT version 6.02/13
// from TTree L1TreeEmulator/L1TreeEmulator
// found on file: Ntuple_BMTF_data_run265371.root
//////////////////////////////////////////////////////////

#ifndef L1Emulator_h
#define L1Emulator_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TMatrixT.h>
#include <vector>
#include <TTree.h>

// Header file for the classes stored in the TTree if any.
//#include "UIoannina/TrUpS/interface/L1AnalysisBMTFDataFormat.h"

class L1Emulator {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
 //TrUpS::L1AnalysisBMTFDataFormat *BMTF_Emulator;
   Int_t           emubmtfSize;
   vector<int>     emubmtfPt;
   vector<int>     emubmtfEta;
   vector<int>     emubmtfFineBit;
   vector<int>     emubmtfPhi;
   vector<int>     emubmtfqual;
   vector<int>     emubmtfch;
   vector<int>     emubmtfbx;
   vector<int>     emubmtfprocessor;
   vector<int>     emubmtftrAddress;
   vector<int>     emubmtfwh;

   // List of branches
   TBranch        *b_BMTF_Emulator_bmtfSize;   //!
   TBranch        *b_BMTF_Emulator_bmtfPt;   //!
   TBranch        *b_BMTF_Emulator_bmtfEta;   //!
   TBranch        *b_BMTF_Emulator_bmtfFineBit;   //!
   TBranch        *b_BMTF_Emulator_bmtfPhi;   //!
   TBranch        *b_BMTF_Emulator_bmtfqual;   //!
   TBranch        *b_BMTF_Emulator_bmtfch;   //!
   TBranch        *b_BMTF_Emulator_bmtfbx;   //!
   TBranch        *b_BMTF_Emulator_bmtfprocessor;   //!
   TBranch        *b_BMTF_Emulator_bmtftrAddress;   //!
   TBranch        *b_BMTF_Emulator_bmtfwh;   //!

   L1Emulator(TTree *tree=0);
   virtual ~L1Emulator();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

L1Emulator::L1Emulator(TTree *tree) : fChain(0) 
{

   Init(tree);
}

L1Emulator::~L1Emulator()
{
   if (!fChain) return;
   //delete fChain->GetCurrentFile();
}

Int_t L1Emulator::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t L1Emulator::LoadTree(Long64_t entry)
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

void L1Emulator::Init(TTree *tree)
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


   fChain->SetBranchAddress("bmtfSize", &emubmtfSize, &b_BMTF_Emulator_bmtfSize);
   fChain->SetBranchAddress("bmtfPt", &emubmtfPt, &b_BMTF_Emulator_bmtfPt);
   fChain->SetBranchAddress("bmtfEta", &emubmtfEta, &b_BMTF_Emulator_bmtfEta);
   fChain->SetBranchAddress("bmtfFineBit", &emubmtfFineBit, &b_BMTF_Emulator_bmtfFineBit);
   fChain->SetBranchAddress("bmtfPhi", &emubmtfPhi, &b_BMTF_Emulator_bmtfPhi);
   fChain->SetBranchAddress("bmtfqual", &emubmtfqual, &b_BMTF_Emulator_bmtfqual);
   fChain->SetBranchAddress("bmtfch", &emubmtfch, &b_BMTF_Emulator_bmtfch);
   fChain->SetBranchAddress("bmtfbx", &emubmtfbx, &b_BMTF_Emulator_bmtfbx);
   fChain->SetBranchAddress("bmtfprocessor", &emubmtfprocessor, &b_BMTF_Emulator_bmtfprocessor);
   fChain->SetBranchAddress("bmtftrAddress", &emubmtftrAddress, &b_BMTF_Emulator_bmtftrAddress);
   fChain->SetBranchAddress("bmtfwh", &emubmtfwh, &b_BMTF_Emulator_bmtfwh);
   Notify();
}

Bool_t L1Emulator::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void L1Emulator::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t L1Emulator::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef L1Emulator_cxx
