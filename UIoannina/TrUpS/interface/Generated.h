#ifndef __TrUpS_Generated_H__
#define __TrUpS_Generated_H__

//-------------------------------------------------------------------------------
// Created 07/03/2013 - G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------


#include "DataFormats/Common/interface/Handle.h"

#include <vector>
#include "TMatrixD.h"
#include "GeneratedDataFormat.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class Generated 
  {
  public:
    Generated();
    ~Generated();
    
    void SetGen(const edm::Event& , const edm::EventSetup&);
    void Reset() {gen_.Reset();}
    GeneratedDataFormat * getData() {return &gen_;}

  private : 
    GeneratedDataFormat gen_;
  }; 
} 
#endif


