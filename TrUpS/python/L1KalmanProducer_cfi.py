#original author: georgios.karathanasis@cern.ch
import FWCore.ParameterSet.Config as cms

L1KalmanProducer = cms.EDAnalyzer("L1KalmanProducer",

    kmtfOutputDigis = cms.InputTag("simKBmtfDigis"),
    kmtfHWOutputDigis = cms.InputTag("simKBmtfDigis:BMTF"),
)

