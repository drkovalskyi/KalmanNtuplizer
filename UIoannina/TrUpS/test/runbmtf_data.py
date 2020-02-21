# G Karathanasis : email, georgios.karathanasis@cern.ch
import FWCore.ParameterSet.Config as cms
process = cms.Process("L1TMuonEmulation")
import os
import sys
import commands

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')



process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))

process.source = cms.Source('PoolSource',
 fileNames = cms.untracked.vstring(#'/store/mc/RunIISummer17DRStdmix/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8/GEN-SIM-RAW/NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/00000/0A32C61D-FFEC-E711-BA08-0242AC130002.root'
#'/store/relval/CMSSW_10_1_1/SingleMuon/RAW-RECO/ZMu-101X_dataRun2_PromptLike_v9_RelVal_sigMu2017F-v1/10000/02626A91-4B3D-E811-87EF-0CC47A4D769A.root'
'/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/320/500/00000/000D3F29-E795-E811-9803-FA163E1CBD58.root'),
 secondaryFileNames = cms.untracked.vstring('/store/data/Run2018D/JetHT/RAW/v1/000/320/500/00000/00741BBC-D193-E811-9C0A-FA163E8D39C1.root')

	                    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))

# PostLS1 geometry used
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
############################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')




process.load("L1Trigger.L1TTwinMux.fakeTwinMuxParams_cff")
####Event Setup Producer
process.load('L1Trigger.L1TMuonBarrel.fakeBmtfParams_cff')
process.esProd = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(
      cms.PSet(record = cms.string('L1TMuonBarrelParamsRcd'),
               data = cms.vstring('L1TMuonBarrelParams'))
                   ),
   verbose = cms.untracked.bool(True)
)

process.load("EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi")
process.load('L1Trigger.Configuration.SimL1Emulator_cff')
process.load("EventFilter.RPCRawToDigi.rpcUnpackingModule_cfi")
process.load("EventFilter.RPCRawToDigi.RPCTwinMuxRawToDigi_cfi")

process.RPCTwinMuxRawToDigi.bxMin = cms.int32(-5)
process.RPCTwinMuxRawToDigi.bxMax = cms.int32(5)

process.load('EventFilter.DTRawToDigi.dtunpacker_cfi')
process.unpackDT = process.muonDTDigis.clone(
        inputLabel = cms.InputTag( 'rawDataCollector', processName=cms.InputTag.skipCurrentProcess()))
process.load('EventFilter.RPCRawToDigi.rpcUnpacker_cfi')
process.unpackRPC = process.rpcunpacker.clone(
InputLabel = cms.InputTag( 'rawDataCollector', processName=cms.InputTag.skipCurrentProcess()))
#DT emulator
from L1Trigger.DTTrigger.dtTriggerPrimitiveDigis_cfi import dtTriggerPrimitiveDigis
process.simDtTriggerPrimitiveDigis = dtTriggerPrimitiveDigis.clone()
#process.simDtTriggerPrimitiveDigis.digiTag =  cms.InputTag('unpackDT')
process.simDtTriggerPrimitiveDigis.digiTag =  cms.InputTag('unpackDT')

#RPC emulator
process.load('L1Trigger.RPCTrigger.rpcTriggerDigis_cff')
process.simRpcTriggerDigis = process.rpcTriggerDigis.clone()
process.simRpcTriggerDigis.label = 'simMuonRPCDigis'

process.load('EventFilter.L1TRawToDigi.validationEventFilter_cfi')

####BMTF Emulator
process.load('L1Trigger.L1TTwinMux.simTwinMuxDigis_cfi')
#process.simTwinMuxDigis.DTDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis")
#process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis")
#process.simTwinMuxDigis.RPC_Source = cms.InputTag("RPCTwinMuxRawToDigi")

process.load('L1Trigger.L1TMuonBarrel.simBmtfDigis_cfi')
process.simBmtfDigis.DTDigi_Source=cms.InputTag("simTwinMuxDigis")
process.simBmtfDigis.DTThetaDigi_Source=cms.InputTag("simDtTriggerPrimitiveDigis")
process.simBmtfDigis.Debug = cms.untracked.int32(0)
process.load("L1Trigger.L1TMuonBarrel.simKBmtfDigis_cfi")
process.load("L1Trigger.L1TMuonBarrel.simKBmtfStubs_cfi")
process.simKBmtfStubs.srcPhi=cms.InputTag("bmtfDigis")
process.simKBmtfStubs.srcTheta=cms.InputTag("bmtfDigis")
process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")
process.load("UIoannina.TrUpS.L1KalmanProducer_cfi")

process.load("UIoannina.TrUpS.L1Producer_cfi")
process.load("UIoannina.TrUpS.GENProducer_cfi")
process.load('L1Trigger.L1TNtuples.l1MuonRecoTree_cfi')

process.L1TProducer.bmtfOutputDigis = cms.InputTag("simBmtfDigis:BMTF")
process.L1TProducer.bmtfInputPhDigis = cms.InputTag("simDtTriggerPrimitiveDigis")
process.L1TProducer.bmtfInputThDigis = cms.InputTag("bmtfDigis","","L1KMTF")
process.L1TProducer.bmtfOutputDigis = cms.InputTag("bmtfDigis:BMTF")
process.L1TProducer.bmtfInputPhDigis = cms.InputTag("bmtfDigis","","L1KMTF")
process.load('EventFilter.L1TRawToDigi.bmtfDigis_cfi')

process.L1TMuonSeq = cms.Sequence( process.esProd    
#                                    +process.unpackDT
 #                                  +process.unpackRPC                                                             +process.RPCTwinMuxRawToDigi
 #                                   +process.simDtTriggerPrimitiveDigis
 #                                  +process.simRpcTriggerDigis
#
#				   + process.simTwinMuxDigis 
##                                   + process.simBmtfDigis 
                                      +process.bmtfDigis 
                                    +process.simKBmtfStubs
                                   +process.simKBmtfDigis
                                   +process.L1KalmanProducer
                                     +process.L1TProducer 
                                  # + process.dumpED
                                  # + process.dumpES
 +process.l1MuonRecoTree
  #                                  +process.GENTProducer                                   
                                   
)

process.L1TMuonPath = cms.Path(process.L1TMuonSeq)

process.out = cms.OutputModule("PoolOutputModule", 
   fileName = cms.untracked.string("l1tbmtf.root")
)

process.output_step = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.L1TMuonPath)
#process.schedule.extend([process.output_step])
process.TFileService = cms.Service("TFileService",
   # fileName = cms.string('Ntuple_GEN_BMTF_lmatest_no_sp.root')
     fileName = cms.string('Ntuple_l1tbmtf_kalman.root') )

