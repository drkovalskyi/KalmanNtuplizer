//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jan 20 18:05:49 2016 by ROOT version 6.04/02
// from TTree GENTree/GENTree
// found on file: Ntuple_test.root
//////////////////////////////////////////////////////////

#ifndef GENTreeClass_h
#define GENTreeClass_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TMatrixT.h>
#include <TTree.h>
#include <vector>

// Header file for the classes stored in the TTree if any.

class GENTreeClass {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
 //TrUpS::GenMuonDataFormat *GENMuons;
   vector<float>   genPt_Mu;
   vector<float>   genPhi_Mu;
   vector<float>   genEta_Mu;
   vector<float>   genStatus_Mu;
   Int_t           gen_muons;

   // List of branches
   TBranch        *b_GENMuons_genPt_Mu;   //!
   TBranch        *b_GENMuons_genPhi_Mu;   //!
   TBranch        *b_GENMuons_genEta_Mu;   //!
   TBranch        *b_GENMuons_genStatus_Mu;   //!
   TBranch        *b_GENMuons_gen_muons;   //!

   GENTreeClass(TTree *tree=0);
   virtual ~GENTreeClass();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

GENTreeClass::GENTreeClass(TTree *tree) : fChain(0) 
{
   Init(tree);
}

GENTreeClass::~GENTreeClass()
{
   if (!fChain) return;
  // delete fChain->GetCurrentFile();
}

Int_t GENTreeClass::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t GENTreeClass::LoadTree(Long64_t entry)
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

void GENTreeClass::Init(TTree *tree)
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

   fChain->SetBranchAddress("genPt_Mu", &genPt_Mu, &b_GENMuons_genPt_Mu);
   fChain->SetBranchAddress("genPhi_Mu", &genPhi_Mu, &b_GENMuons_genPhi_Mu);
   fChain->SetBranchAddress("genEta_Mu", &genEta_Mu, &b_GENMuons_genEta_Mu);
   fChain->SetBranchAddress("genStatus_Mu", &genStatus_Mu, &b_GENMuons_genStatus_Mu);
   fChain->SetBranchAddress("gen_muons", &gen_muons, &b_GENMuons_gen_muons);
   Notify();
}

Bool_t GENTreeClass::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void GENTreeClass::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t GENTreeClass::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef GENTreeClass_cxx
