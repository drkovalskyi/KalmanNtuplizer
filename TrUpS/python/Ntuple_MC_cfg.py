import FWCore.ParameterSet.Config as cms

# make L1 ntuples from RAW+RECO

process = cms.Process("NTUPLE")

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
#process.load('Configuration/StandardSequences/SimL1Emulator_cff')
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
#process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
#process.load('Configuration.StandardSequences.GeometryIdeal_cff')
#process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
#process.load("JetMETCorrections.Configuration.DefaultJEC_cff")
#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

# output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('Tree.root')
)


# L1 ntuple producers
process.load("UIoannina.TrUpS.PATProducer_cfi")
process.load("UIoannina.TrUpS.GENProducer_cfi")
process.load("UIoannina.TrUpS.RECOProducer_cfi")
process.load("UIoannina.TrUpS.L1Producer_cfi")
process.load("UIoannina.TrUpS.EVRProducer_cfi")

process.default = cms.Path(
#process.default = cms.Sequence(
    process.EVRTProducer
#   +process.L1TProducer
#   +process.RECOTProducer
   +process.GENTProducer
)

# job options
#process.GlobalTag.globaltag = 'START52_V9::All'

#SkipEvent = cms.untracked.vstring('ProductNotFound')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source ("PoolSource",
                             fileNames = readFiles,
                             secondaryFileNames = secFiles
                             )

