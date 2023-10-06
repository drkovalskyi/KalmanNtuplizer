#ifndef __TrUpS_EventRunDataFormat_H__
#define __TrUpS_EventRunDataFormat_H__

//-------------------------------------------------------------------------------
// Created 17/05/2013 G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------

#include <vector>
#include "TMatrixD.h"


namespace TrUpS
{
  struct EventRunDataFormat
  {

    EventRunDataFormat(){Reset();};
    ~EventRunDataFormat(){};
    
    void Reset()
    {
    pvertex=-1;
    run=-1;
    event=-1;
    lumi=-1;
    bunch=-1;
    }

    int  pvertex;
    int  run;
    int  event;
    int  lumi;
    int  bunch;


  }; 
} 
#endif


