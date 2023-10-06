// -*- C++ -*-
//
// Package:    
// Class:      
//



//
// Original Author:  G.Flouris
//         Created:
// 
//
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

#include "DataFormats/VertexReco/interface/Vertex.h"



// ROOT output stuff
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TTree.h"
#include "TF1.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>

//local  data formats

#include "UIoannina/TrUpS/interface/EventRun.h"
//#include "../interface/EventRun.h"


//
// class declaration
//

class EVRTreeProducer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit EVRTreeProducer(const edm::ParameterSet&);
  ~EVRTreeProducer();


private:
  virtual void beginJob(void) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();

public:

  TrUpS::EventRun*     		evr;

  TrUpS::EventRunDataFormat*        evr_data;


private:

  // output file
  edm::Service<TFileService> fs_;

  // tree
  TTree * tree_;

  // EDM input tags
//  edm::InputTag jetTag_;
};



EVRTreeProducer::EVRTreeProducer(const edm::ParameterSet& iConfig)
{

 
  evr      	= new  TrUpS::EventRun(consumesCollector());
  consumes<std::vector<reco::Vertex> >(iConfig.getParameter<edm::InputTag>("offlinePrimaryVertices"));

  evr_data	     = evr->getData();

  // set up output
  tree_=fs_->make<TTree>("EVRTree", "EVRTree");
  tree_->Branch("EventRun",        "TrUpS::EventRunDataFormat",       	    &evr_data,             32000, 3);



}


EVRTreeProducer::~EVRTreeProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void EVRTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  evr->Reset();
  evr->SetEvr(iEvent,iSetup);

  tree_->Fill();

}

// ------------ method called once each job just before starting event loop  ------------
void
EVRTreeProducer::beginJob(void)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
EVRTreeProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(EVRTreeProducer);
