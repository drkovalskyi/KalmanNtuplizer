#ifndef __TrUpS_L1AnalysisBMTF_H__
#define __TrUpS_L1AnalysisBMTF_H__

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include "DataFormats/Common/interface/Handle.h"

#include <vector>
#include "TMatrixD.h"
#include "L1AnalysisBMTFDataFormat.h"


#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class L1AnalysisBMTF
  {
  public:
    L1AnalysisBMTF(edm::ConsumesCollector && ix);
    ~L1AnalysisBMTF();

    void SetDTPH(const edm::Handle<L1MuDTChambPhContainer > L1MuDTChambPhContainer, unsigned int maxDTPH);
    void SetDTTH(const edm::Handle<L1MuDTChambThContainer > L1MuDTChambThContainer, unsigned int maxDTTH);
    void SetBMTF(const l1t::RegionalMuonCandBxCollection& coll, int& ctr, int bx);

    void Reset() {bmtf_.Reset();}
    L1AnalysisBMTFDataFormat * getData() {return &bmtf_;}

  private :
    L1AnalysisBMTFDataFormat bmtf_;
  };
}
#endif


