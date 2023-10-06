#ifndef __TrUpS_GeneratedDataFormat_H__
#define __TrUpS_GeneratedDataFormat_H__

//-------------------------------------------------------------------------------
// Created 07/03/2013 - G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------

#include <vector>
#include "TMatrixD.h"


namespace TrUpS
{
  struct GeneratedDataFormat
  {

    GeneratedDataFormat(){Reset();};
    ~GeneratedDataFormat(){};
    
    void Reset()
    {


    genPt_Mu.clear();
    genEta_Mu.clear();
    genPhi_Mu.clear();
    genStatus_Mu.clear();
    }


    std::vector<float> genPt_Mu;
    std::vector<float> genPhi_Mu;
    std::vector<float> genEta_Mu;
    std::vector<float> genStatus_Mu;

  }; 
} 
#endif


