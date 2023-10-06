import FWCore.ParameterSet.Config as cms

L1TProducer = cms.EDAnalyzer("L1TreeProducer",
    bmtfInputPhDigis = cms.InputTag("BMTFStage2Digis"),
    bmtfInputThDigis = cms.InputTag("BMTFStage2Digis"),

    bmtfOutputDigis = cms.InputTag("BMTFStage2Digis"),
)

