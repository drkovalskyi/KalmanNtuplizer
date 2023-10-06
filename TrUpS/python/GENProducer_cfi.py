import FWCore.ParameterSet.Config as cms

GENTProducer = cms.EDAnalyzer("GENTreeProducer",
	genParticles=cms.InputTag("genParticles")
)

