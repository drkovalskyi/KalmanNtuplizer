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


#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/Framework/interface/ConsumesCollector.h>


// ROOT output stuff
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TTree.h"
#include "TF1.h"

//local  data formats

#include "KalmanNtuplizer/TrUpS/interface/GenMuon.h"


//
// class declaration
//

class GENTreeProducer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit GENTreeProducer(const edm::ParameterSet&);
  ~GENTreeProducer();


private:
  virtual void beginJob(void) ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();

public:

  TrUpS::GenMuon*     		gen;

  TrUpS::GenMuonDataFormat*            gen_data;


private:

  // output file
  edm::Service<TFileService> fs_;

  // tree
  TTree * tree_;

  // EDM input tags
//  edm::InputTag jetTag_;
};



GENTreeProducer::GENTreeProducer(const edm::ParameterSet& iConfig)
{

 
  gen      	= new  TrUpS::GenMuon(consumesCollector());

 consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("genParticles"));
 
  gen_data	     = gen->getData();

  // set up output
  tree_=fs_->make<TTree>("GENTree", "GENTree");
  tree_->Branch("GENMuons",        "TrUpS::GenMuonDataFormat",       	    &gen_data,             32000, 3);



}


GENTreeProducer::~GENTreeProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void GENTreeProducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  gen->Reset();
  gen->SetGen(iEvent,iSetup);

  tree_->Fill();

}

// ------------ method called once each job just before starting event loop  ------------
void
GENTreeProducer::beginJob(void)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
GENTreeProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(GENTreeProducer);
