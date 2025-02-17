//original author: g karathanasis, georgios.karathanasis@cern.ch
//
// system include files
#include <memory>

// framework
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisKMTF.h"
//#include "DataFormats/L1KalmanMuonTrigger/interface/L1KalmanMuTrack.h"
#include "DataFormats/L1TMuon/interface/L1MuKBMTrack.h"

// ROOT output stuff
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TTree.h"
#include "TF1.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>

//local  data formats

//#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisGMT.h"
//#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisDTTF.h"
//#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisBMTF.h"


//
// class declaration
//

class L1KalmanProducer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit L1KalmanProducer(const edm::ParameterSet&);
  ~L1KalmanProducer();


private:
  virtual void beginJob(void) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void analyzeKMTF(const edm::Event&);
  virtual void endJob();

public:

  TrUpS::L1AnalysisKMTF*     	          	l1kmtf;
  TrUpS::L1AnalysisKMTFDataFormat*        l1kmtf_data;

private:

  // output file
  edm::Service<TFileService> fs_;

  // tree
  TTree * tree_;


edm::EDGetTokenT<BXVector<L1MuKBMTrack>> kmtfOutputTag_;
edm::EDGetTokenT<l1t::RegionalMuonCandBxCollection> kmtfHWOutputTag_;

};



L1KalmanProducer::L1KalmanProducer(const edm::ParameterSet& iConfig)
{


  l1kmtf      	=   new  TrUpS::L1AnalysisKMTF(consumesCollector());
  l1kmtf_data	     = l1kmtf->getData();

  //consumes<L1MuDTChambPhContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputDigis"));
  //consumes<L1MuDTChambThContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputDigis"));



   kmtfOutputTag_ = consumes<BXVector<L1MuKBMTrack>>(iConfig.getParameter<edm::InputTag>("kmtfOutputDigis"));
   kmtfHWOutputTag_ = consumes<l1t::RegionalMuonCandBxCollection>(iConfig.getParameter<edm::InputTag>("kmtfHWOutputDigis"));
  


  // set up output
  tree_=fs_->make<TTree>("L1KMTFtree", "L1KMTFtree");
  tree_->Branch("KMTF","TrUpS::L1AnalysisKMTFDataFormat", &l1kmtf_data, 32000, 3);

}


L1KalmanProducer::~L1KalmanProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void L1KalmanProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  analyzeKMTF(iEvent);
  tree_->Fill();
}



void L1KalmanProducer::analyzeKMTF(const edm::Event& iEvent)
{
  l1kmtf->Reset();

unsigned int max = 50;

///Output of BMTF
  int ctr = 0;
  edm::Handle<BXVector<L1MuKBMTrack>> mycoll;
 edm::Handle<l1t::RegionalMuonCandBxCollection> mycollHW;
  iEvent.getByToken(kmtfOutputTag_,mycoll);
   iEvent.getByToken(kmtfHWOutputTag_,mycollHW);
  //const l1t::RegionalMuonCandBxCollection& coll = *mycoll;
  l1kmtf->SetKMTF(*mycoll, ctr, 0);  
  int firstbx = (*mycollHW).getFirstBX();
  int lastbx  = (*mycollHW).getLastBX() + 1;
        //cout<<firstbx<<"\t"<<lastbx<<endl;
  for(int i=firstbx; i<lastbx; i++)
         l1kmtf->SetHWKMTF(*mycollHW, ctr, i);

}



// ------------ method called once each job just before starting event loop  ------------
void
L1KalmanProducer::beginJob(void)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
L1KalmanProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1KalmanProducer);
