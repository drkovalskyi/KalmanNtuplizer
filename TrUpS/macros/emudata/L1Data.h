//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Mar  3 17:38:01 2016 by ROOT version 6.02/13
// from TTree L1Tree/L1Tree
// found on file: Ntuple_BMTF_data_run265371.root
//////////////////////////////////////////////////////////

#ifndef L1Data_h
#define L1Data_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
//#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisBMTFDataFormat.h"

class L1Data {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
 //TrUpS::L1AnalysisBMTFDataFormat *BMTF;
   Int_t           phSize;
   vector<int>     phBx;
   vector<int>     phWh;
   vector<int>     phSe;
   vector<int>     phSt;
   vector<float>   phAng;
   vector<double>  phGlobPhi;
   vector<float>   phBandAng;
   vector<int>     phCode;
   vector<float>   phX;
   vector<float>   phY;
   vector<int>     phBxRAW;
   vector<int>     phTs2Tag;
   Int_t           thSize;
   vector<int>     thBx;
   vector<int>     thWh;
   vector<int>     thSe;
   vector<int>     thSt;
   vector<float>   thX;
   vector<float>   thY;
   vector<int>     thTheta;
   vector<int>     thCode;
   Int_t           bmtfSize;
   vector<int>     bmtfPt;
   vector<int>     bmtfEta;
   vector<int>     bmtfFineBit;
   vector<int>     bmtfPhi;
   vector<int>     bmtfqual;
   vector<int>     bmtfch;
   vector<int>     bmtfbx;
   vector<int>     bmtfprocessor;
   vector<int>     bmtftrAddress;
   vector<int>     bmtfwh;
   /*Int_t           trmbSize;
   vector<int>     trmbPt;
   vector<int>     trmbEta;
   vector<int>     trmbPhi;
   vector<int>     trmbqual;
   vector<int>     trmbch;
   vector<int>     trmbbx;
   vector<int>     trmbprocessor;
   vector<int>     trmbtrAddress;
   vector<int>     trmbwh;
*/
   // List of branches
   TBranch        *b_BMTF_phSize;   //!
   TBranch        *b_BMTF_phBx;   //!
   TBranch        *b_BMTF_phWh;   //!
   TBranch        *b_BMTF_phSe;   //!
   TBranch        *b_BMTF_phSt;   //!
   TBranch        *b_BMTF_phAng;   //!
   TBranch        *b_BMTF_phGlobPhi;   //!
   TBranch        *b_BMTF_phBandAng;   //!
   TBranch        *b_BMTF_phCode;   //!
   TBranch        *b_BMTF_phX;   //!
   TBranch        *b_BMTF_phY;   //!
   TBranch        *b_BMTF_phBxRAW;   //!
   TBranch        *b_BMTF_phTs2Tag;   //!
   TBranch        *b_BMTF_thSize;   //!
   TBranch        *b_BMTF_thBx;   //!
   TBranch        *b_BMTF_thWh;   //!
   TBranch        *b_BMTF_thSe;   //!
   TBranch        *b_BMTF_thSt;   //!
   TBranch        *b_BMTF_thX;   //!
   TBranch        *b_BMTF_thY;   //!
   TBranch        *b_BMTF_thTheta;   //!
   TBranch        *b_BMTF_thCode;   //!
   TBranch        *b_BMTF_bmtfSize;   //!
   TBranch        *b_BMTF_bmtfPt;   //!
   TBranch        *b_BMTF_bmtfEta;   //!
   TBranch        *b_BMTF_bmtfFineBit;   //!
   TBranch        *b_BMTF_bmtfPhi;   //!
   TBranch        *b_BMTF_bmtfqual;   //!
   TBranch        *b_BMTF_bmtfch;   //!
   TBranch        *b_BMTF_bmtfbx;   //!
   TBranch        *b_BMTF_bmtfprocessor;   //!
   TBranch        *b_BMTF_bmtftrAddress;   //!
   TBranch        *b_BMTF_bmtfwh;   //!
   // TBranch        *b_BMTF_trmbSize;   //!
   // TBranch        *b_BMTF_trmbPt;   //!
   // TBranch        *b_BMTF_trmbEta;   //!
   // TBranch        *b_BMTF_trmbPhi;   //!
   // TBranch        *b_BMTF_trmbqual;   //!
   // TBranch        *b_BMTF_trmbch;   //!
   // TBranch        *b_BMTF_trmbbx;   //!
   // TBranch        *b_BMTF_trmbprocessor;   //!
   // TBranch        *b_BMTF_trmbtrAddress;   //!
   // TBranch        *b_BMTF_trmbwh;   //!

   L1Data(TTree *tree=0);
   virtual ~L1Data();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   //virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};


L1Data::L1Data(TTree *tree) : fChain(0) 
{

   Init(tree);
}

L1Data::~L1Data()
{
   if (!fChain) return;
   //delete fChain->GetCurrentFile();
}

Int_t L1Data::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t L1Data::LoadTree(Long64_t entry)
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

void L1Data::Init(TTree *tree)
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

   fChain->SetBranchAddress("phSize", &phSize, &b_BMTF_phSize);
   fChain->SetBranchAddress("phBx", &phBx, &b_BMTF_phBx);
   fChain->SetBranchAddress("phWh", &phWh, &b_BMTF_phWh);
   fChain->SetBranchAddress("phSe", &phSe, &b_BMTF_phSe);
   fChain->SetBranchAddress("phSt", &phSt, &b_BMTF_phSt);
   fChain->SetBranchAddress("phAng", &phAng, &b_BMTF_phAng);
   fChain->SetBranchAddress("phGlobPhi", &phGlobPhi, &b_BMTF_phGlobPhi);
   fChain->SetBranchAddress("phBandAng", &phBandAng, &b_BMTF_phBandAng);
   fChain->SetBranchAddress("phCode", &phCode, &b_BMTF_phCode);
   fChain->SetBranchAddress("phX", &phX, &b_BMTF_phX);
   fChain->SetBranchAddress("phY", &phY, &b_BMTF_phY);
   fChain->SetBranchAddress("phBxRAW", &phBxRAW, &b_BMTF_phBxRAW);
   fChain->SetBranchAddress("phTs2Tag", &phTs2Tag, &b_BMTF_phTs2Tag);
   fChain->SetBranchAddress("thSize", &thSize, &b_BMTF_thSize);
   fChain->SetBranchAddress("thBx", &thBx, &b_BMTF_thBx);
   fChain->SetBranchAddress("thWh", &thWh, &b_BMTF_thWh);
   fChain->SetBranchAddress("thSe", &thSe, &b_BMTF_thSe);
   fChain->SetBranchAddress("thSt", &thSt, &b_BMTF_thSt);
   fChain->SetBranchAddress("thX", &thX, &b_BMTF_thX);
   fChain->SetBranchAddress("thY", &thY, &b_BMTF_thY);
   fChain->SetBranchAddress("thTheta", &thTheta, &b_BMTF_thTheta);
   fChain->SetBranchAddress("thCode", &thCode, &b_BMTF_thCode);
   fChain->SetBranchAddress("bmtfSize", &bmtfSize, &b_BMTF_bmtfSize);
   fChain->SetBranchAddress("bmtfPt", &bmtfPt, &b_BMTF_bmtfPt);
   fChain->SetBranchAddress("bmtfEta", &bmtfEta, &b_BMTF_bmtfEta);
   fChain->SetBranchAddress("bmtfFineBit", &bmtfFineBit, &b_BMTF_bmtfFineBit);
   fChain->SetBranchAddress("bmtfPhi", &bmtfPhi, &b_BMTF_bmtfPhi);
   fChain->SetBranchAddress("bmtfqual", &bmtfqual, &b_BMTF_bmtfqual);
   fChain->SetBranchAddress("bmtfch", &bmtfch, &b_BMTF_bmtfch);
   fChain->SetBranchAddress("bmtfbx", &bmtfbx, &b_BMTF_bmtfbx);
   fChain->SetBranchAddress("bmtfprocessor", &bmtfprocessor, &b_BMTF_bmtfprocessor);
   fChain->SetBranchAddress("bmtftrAddress", &bmtftrAddress, &b_BMTF_bmtftrAddress);
   fChain->SetBranchAddress("bmtfwh", &bmtfwh, &b_BMTF_bmtfwh);
   // fChain->SetBranchAddress("trmbSize", &trmbSize, &b_BMTF_trmbSize);
   // fChain->SetBranchAddress("trmbPt", &trmbPt, &b_BMTF_trmbPt);
   // fChain->SetBranchAddress("trmbEta", &trmbEta, &b_BMTF_trmbEta);
   // fChain->SetBranchAddress("trmbPhi", &trmbPhi, &b_BMTF_trmbPhi);
   // fChain->SetBranchAddress("trmbqual", &trmbqual, &b_BMTF_trmbqual);
   // fChain->SetBranchAddress("trmbch", &trmbch, &b_BMTF_trmbch);
   // fChain->SetBranchAddress("trmbbx", &trmbbx, &b_BMTF_trmbbx);
   // fChain->SetBranchAddress("trmbprocessor", &trmbprocessor, &b_BMTF_trmbprocessor);
   // fChain->SetBranchAddress("trmbtrAddress", &trmbtrAddress, &b_BMTF_trmbtrAddress);
   // fChain->SetBranchAddress("trmbwh", &trmbwh, &b_BMTF_trmbwh);
   Notify();
}

Bool_t L1Data::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void L1Data::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t L1Data::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef L1Data_cxx
