// system include files
#include <memory>

// framework
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhDigi.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThDigi.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"

#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// ROOT output stuff
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TTree.h"
#include "TF1.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>

//local  data formats

#include "UIoannina/TrUpS/interface/L1AnalysisGMT.h"
#include "UIoannina/TrUpS/interface/L1AnalysisDTTF.h"
#include "UIoannina/TrUpS/interface/L1AnalysisBMTF.h"


//
// class declaration
//

class L1TreeProducer : public edm::EDAnalyzer {
public:
  explicit L1TreeProducer(const edm::ParameterSet&);
  ~L1TreeProducer();


private:
  virtual void beginJob(void) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void analyzeBMTF(const edm::Event&);
  virtual void endJob();

public:

  TrUpS::L1AnalysisBMTF*     	          	l1bmtf;
  TrUpS::L1AnalysisBMTFDataFormat*        l1bmtf_data;

private:

  // output file
  edm::Service<TFileService> fs_;

  // tree
  TTree * tree_;

  edm::InputTag bmtfInputTag_;

edm::EDGetTokenT<L1MuDTChambPhContainer> bmtfPhInputTag_;
edm::EDGetTokenT<L1MuDTChambThContainer> bmtfThInputTag_;

edm::EDGetTokenT<l1t::RegionalMuonCandBxCollection> bmtfOutputTag_;

};



L1TreeProducer::L1TreeProducer(const edm::ParameterSet& iConfig)
{


  l1bmtf      	=   new  TrUpS::L1AnalysisBMTF(consumesCollector());
  l1bmtf_data	     = l1bmtf->getData();

  //consumes<L1MuDTChambPhContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputDigis"));
  //consumes<L1MuDTChambThContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputDigis"));


   bmtfPhInputTag_ = consumes<L1MuDTChambPhContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputPhDigis"));
   bmtfThInputTag_ = consumes<L1MuDTChambThContainer>(iConfig.getParameter<edm::InputTag>("bmtfInputThDigis"));

   bmtfOutputTag_ = consumes<l1t::RegionalMuonCandBxCollection>(iConfig.getParameter<edm::InputTag>("bmtfOutputDigis"));
  


  // set up output
  tree_=fs_->make<TTree>("L1Tree", "L1Tree");
  tree_->Branch("BMTF","TrUpS::L1AnalysisBMTFDataFormat", &l1bmtf_data, 32000, 3);

}


L1TreeProducer::~L1TreeProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void L1TreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  analyzeBMTF(iEvent);
  tree_->Fill();
}



void L1TreeProducer::analyzeBMTF(const edm::Event& iEvent)
{
  l1bmtf->Reset();

edm::InputTag dttfSource_("BMTFStage2Digis");
unsigned int max = 50;
  edm::Handle<L1MuDTChambPhContainer > myL1MuDTChambPhContainer;
  //iEvent.getByLabel("BMTFStage2Digis",myL1MuDTChambPhContainer);
  iEvent.getByToken(bmtfPhInputTag_,myL1MuDTChambPhContainer);

  if (!myL1MuDTChambPhContainer.isValid()) {
    edm::LogInfo("L1Prompt") << "can't find L1MuDTChambPhContainer" ;
    }
  else l1bmtf->SetDTPH(myL1MuDTChambPhContainer, max);

  edm::Handle<L1MuDTChambThContainer > myL1MuDTChambThContainer;
  //iEvent.getByLabel("BMTFStage2Digis",myL1MuDTChambThContainer);
  iEvent.getByToken(bmtfThInputTag_,myL1MuDTChambThContainer);
  if (!myL1MuDTChambThContainer.isValid()) {
    edm::LogInfo("L1Prompt") << "can't find L1MuDTChambThContainer";
    }
  else l1bmtf->SetDTTH(myL1MuDTChambThContainer, max);

///Output of BMTF
  int ctr = 0;
  edm::Handle<l1t::RegionalMuonCandBxCollection> mycoll;
  iEvent.getByToken(bmtfOutputTag_,mycoll);
  //const l1t::RegionalMuonCandBxCollection& coll = *mycoll;
  if (mycoll.isValid()) {
        int firstbx = (*mycoll).getFirstBX();
        int lastbx  = (*mycoll).getLastBX() + 1;
        //cout<<firstbx<<"\t"<<lastbx<<endl;
        for(int i=firstbx; i<lastbx; i++)
            l1bmtf->SetBMTF(*mycoll, ctr, i);
  }
  else {
      edm::LogInfo("L1Prompt") << "can't find L1MuMBTrackContainer";
//    }
  }



}



// ------------ method called once each job just before starting event loop  ------------
void
L1TreeProducer::beginJob(void)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
L1TreeProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(L1TreeProducer);
