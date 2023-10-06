import FWCore.ParameterSet.Config as cms

EVRTProducer = cms.EDAnalyzer("EVRTreeProducer",
	offlinePrimaryVertices=cms.InputTag("offlinePrimaryVertices")
)

