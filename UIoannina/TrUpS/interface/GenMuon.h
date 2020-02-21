#ifndef __TrUpS_GenMuon_H__
#define __TrUpS_GenMuon_H__

//-------------------------------------------------------------------------------
// Created 07/03/2013 - G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------


#include "DataFormats/Common/interface/Handle.h"

#include <vector>
#include "TMatrixD.h"
#include "GenMuonDataFormat.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class GenMuon 
  {
  public:
    GenMuon(edm::ConsumesCollector && ix);
    ~GenMuon();
    
    void SetGen(const edm::Event& , const edm::EventSetup&);
    void Reset() {gen_.Reset();}
    GenMuonDataFormat * getData() {return &gen_;}

  private : 
    GenMuonDataFormat gen_;
  }; 
} 
#endif


