#ifndef __TrUpS_L1AnalysisDTTFDataFormat_H__
#define __TrUpS_L1AnalysisDTTFDataFormat_H__

//-------------------------------------------------------------------------------
// Created 16/04/2010 - E. Conte, A.C. Le Bihan
// 
//  
// Original code : UserCode/L1TriggerDPG/L1NtupleProducer
//-------------------------------------------------------------------------------

#include <vector>
#include "TMatrixD.h"
#include <string>

namespace TrUpS
{
  struct L1AnalysisDTTFDataFormat
  {

    L1AnalysisDTTFDataFormat(){Reset();};
    ~L1AnalysisDTTFDataFormat(){};
    
    void Reset()
    {

    phSize = 0;  
     
    phBx.clear(); 
    phWh.clear(); 
    phSe.clear(); 
    phSt.clear(); 
    phAng.clear();
    phGlobPhi.clear(); ///
    phBandAng.clear();
    phCode.clear(); 
    phX.clear();
    phY.clear();
    phBxRAW.clear();
    phTs2Tag.clear();
    
    
    thSize = 0;
     
    thBx.clear();
    thWh.clear();
    thSe.clear();
    thSt.clear();
    thX.clear(); 
    thY.clear(); 
    
    
    trSize = 0;
    
    trBx.clear(); 
    trTag.clear();
    trQual.clear(); 
    trPtPck.clear();
    //trPtVal.clear();
    trPhiPck.clear(); 
//    trPhiVal.clear();
    trEtaPck.clear(); 
//    trEtaVal.clear();  
    trPhiGlob.clear(); 
    trChPck.clear();
    trWh.clear(); 
    trSc.clear(); 
    trAddress.clear();

    thTheta.clear();
    thCode.clear();
    
    trmbSize = 0;
    trmbBx.clear(); 
    trmbTag.clear();
    trmbQual.clear(); 
    trmbPtPck.clear();
    trmbPhiPck.clear(); 
    trmbEtaPck.clear(); 
    trmbPhiGlob.clear(); 
    trmbChPck.clear();
    trmbWh.clear(); 
    trmbSc.clear();  
    trmbAddress.clear();

    
    }
      
    // ---- L1AnalysisDTTFDataFormat information.
    
    int phSize;    
    std::vector<int>    phBx; 
    std::vector<int>    phWh; 
    std::vector<int>    phSe; 
    std::vector<int>    phSt; 
    std::vector<float>  phAng;
    std::vector<double> phGlobPhi;
    std::vector<float>  phBandAng;
    std::vector<int>    phCode; 
    std::vector<float>  phX;
    std::vector<float>  phY;
    std::vector<int>  phBxRAW;
    std::vector<int>  phTs2Tag;

    
    int thSize;
    std::vector<int>   thBx;
    std::vector<int>   thWh;
    std::vector<int>   thSe;
    std::vector<int>   thSt;
    std::vector<float> thX; 
    std::vector<float> thY; 
    
    //TMatrixD thTheta;
    //TMatrixD thCode; 
    std::vector<int> thTheta;
    std::vector<int> thCode;

    int trSize;
    std::vector<int>   trBx; 
    std::vector<int>   trTag;
    std::vector<int>   trQual; 
    std::vector<int>   trPtPck;
//    std::vector<float> trPtVal;
    std::vector<int>   trPhiPck; 
//    std::vector<float> trPhiVal; 
    std::vector<int>   trEtaPck; 
//    std::vector<float> trEtaVal; 
    std::vector<double>trPhiGlob; 
    std::vector<int>   trChPck;
    std::vector<int>   trWh; 
    std::vector<int>   trSc;  
    std::vector<unsigned int> trAddress;
    
    int trmbSize;
    std::vector<int>   trmbBx; 
    std::vector<int>   trmbTag;
    std::vector<int>   trmbQual; 
    std::vector<int>   trmbPtPck;
    std::vector<int>   trmbPhiPck; 
    std::vector<int>   trmbEtaPck; 
    std::vector<double>trmbPhiGlob; 
    std::vector<int>   trmbChPck;
    std::vector<int>   trmbWh; 
    std::vector<int>   trmbSc;  
    std::vector<unsigned int> trmbAddress;

    
  }; 
} 
#endif


