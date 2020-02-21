//original author: g karathanasis, georgios.karathanasis@cern.ch

#ifndef __TrUpS_L1AnalysisKMTF_H__
#define __TrUpS_L1AnalysisKMTF_H__

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include "DataFormats/Common/interface/Handle.h"
//#include "DataFormats/L1KalmanMuonTrigger/interface/L1KalmanMuTrack.h"
#include "DataFormats/L1TMuon/interface/L1MuKBMTrack.h"

#include <vector>
#include "TMatrixD.h"
#include "L1AnalysisKMTFDataFormat.h"


#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class L1AnalysisKMTF
  {
  public:
    L1AnalysisKMTF(edm::ConsumesCollector && ix);
    ~L1AnalysisKMTF();

    void SetKMTF(const BXVector<L1MuKBMTrack>& coll, int& ctr, int bx);
    void SetHWKMTF(const l1t::RegionalMuonCandBxCollection& coll, int& ctr, int bx);
    void Reset() {kmtf_.Reset();}
    L1AnalysisKMTFDataFormat * getData() {return &kmtf_;}

  private :
    L1AnalysisKMTFDataFormat kmtf_;
  };
}
#endif


