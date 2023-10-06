#include "KalmanNtuplizer/TrUpS/interface/EventRun.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"

#include "DataFormats/VertexReco/interface/Vertex.h"

// framework
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include <FWCore/Framework/interface/LuminosityBlock.h>
#include <FWCore/Framework/interface/ConsumesCollector.h>

TrUpS::EventRun::EventRun(edm::ConsumesCollector && ix)
{	     
}


TrUpS::EventRun::~EventRun()
{

}

void TrUpS::EventRun::SetEvr(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

//edm::Handle<std::vector<reco::Vertex> > vertex;
//iEvent.getByLabel(edm::InputTag("offlinePrimaryVertices"), vertex);


//evr_.pvertex = vertex->size();
evr_.run     = iEvent.id().run();
evr_.event   = iEvent.id().event();
evr_.lumi    = iEvent.luminosityBlock();
evr_.bunch   = iEvent.bunchCrossing();



}
