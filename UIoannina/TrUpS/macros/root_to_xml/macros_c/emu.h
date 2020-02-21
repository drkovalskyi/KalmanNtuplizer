//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sun Feb  8 23:54:49 2015 by ROOT version 5.34/24
// from TTree Emulator/Emulator
// found on file: ./new_file.root
//////////////////////////////////////////////////////////

#ifndef emu_h
#define emu_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include <vector>

// Fixed size dimensions of array or collections stored in the TTree if any.

class emu {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   vector<float>   *pt;
   vector<float>   *quality;
   vector<float>   *phi;
   vector<float>   *tradd;

   // List of branches
   TBranch        *b_pt;   //!
   TBranch        *b_quality;   //!
   TBranch        *b_phi;   //!
   TBranch        *b_tradd;   //!

   emu(TTree *tree=0);
   virtual ~emu();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef emu_cxx
emu::emu(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
//   if (tree == 0) {
//      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("./new_file.root");
//      if (!f || !f->IsOpen()) {
//         f = new TFile("./new_file.root");
//      }
//      f->GetObject("Emulator",tree);
//
 //  }
   Init(tree);
}

emu::~emu()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t emu::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t emu::LoadTree(Long64_t entry)
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

void emu::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   pt = 0;
   quality = 0;
   phi = 0;
   tradd = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("pt", &pt, &b_pt);
   fChain->SetBranchAddress("quality", &quality, &b_quality);
   fChain->SetBranchAddress("phi", &phi, &b_phi);
   fChain->SetBranchAddress("tradd", &tradd, &b_tradd);
   Notify();
}

Bool_t emu::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void emu::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t emu::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef emu_cxx
