#ifndef __TrUpS_L1AnalysisDTTF_H__
#define __TrUpS_L1AnalysisDTTF_H__

//-------------------------------------------------------------------------------
// Created 06/01/2010 - A.C. Le Bihan
// 
//  
// Original code : UserCode/L1TriggerDPG/L1NtupleProducer
//-------------------------------------------------------------------------------

#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambPhContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTChambThContainer.h"
#include "DataFormats/L1DTTrackFinder/interface/L1MuDTTrackContainer.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include "DataFormats/Common/interface/Handle.h"

#include <vector>
#include "TMatrixD.h"
#include "L1AnalysisDTTFDataFormat.h"


#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class L1AnalysisDTTF 
  {
  public:
    L1AnalysisDTTF(edm::ConsumesCollector && ix);
    ~L1AnalysisDTTF();
    
    void SetDTPH(const edm::Handle<L1MuDTChambPhContainer > L1MuDTChambPhContainer, unsigned int maxDTPH);
    void SetDTTH(const edm::Handle<L1MuDTChambThContainer > L1MuDTChambThContainer, unsigned int maxDTTH);
    void SetDTTR(const edm::Handle<L1MuDTTrackContainer >   L1MuDTTrackContainer,   unsigned int maxDTTR);
   // void SetMBTR(const edm::Handle<BMTrackContainer >   BMTrackContainer,   unsigned int maxMBTR);
    void Reset() {dttf_.Reset();}
    L1AnalysisDTTFDataFormat * getData() {return &dttf_;}

  private : 
    L1AnalysisDTTFDataFormat dttf_;
  }; 
} 
#endif


