#ifndef __TrUpS_EventRun_H__
#define __TrUpS_EventRun_H__

//-------------------------------------------------------------------------------
// Created 17/05/2013 - G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------

#include "DataFormats/Common/interface/Handle.h"

#include "EventRunDataFormat.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace TrUpS
{
  class EventRun 
  {
  public:
    EventRun(edm::ConsumesCollector && ix);
    ~EventRun();

    void SetEvr(const edm::Event& , const edm::EventSetup&);
    void Reset() {evr_.Reset();}
    EventRunDataFormat * getData() {return &evr_;}

  private : 
    EventRunDataFormat evr_;
  }; 
} 
#endif


