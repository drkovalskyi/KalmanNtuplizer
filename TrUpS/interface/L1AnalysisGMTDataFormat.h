#ifndef __TrUpS_L1AnalysisGMTDataFormat_H__
#define __TrUpS_L1AnalysisGMTDataFormat_H__

//-------------------------------------------------------------------------------
// Created 
// 
//
// Original code : UserCode/L1TriggerDPG/L1NtupleProducer
//-------------------------------------------------------------------------------

#include <vector>


namespace TrUpS
{
  struct L1AnalysisGMTDataFormat
  {
    L1AnalysisGMTDataFormat(){Reset();};
    ~L1AnalysisGMTDataFormat(){};
    
    void Reset()
    {
//      Ndt = 0; Ncsc = 0; Nrpcb = 0;
//      Nrpcf = 0;
// N = 0;


 //Global Muon Trigger

  Bx.clear();
  Quality.clear();
  Pt.clear();
  Eta.clear();
  Phi.clear();
  gmt_muons = 0;
  Charge.clear();
  Charge_Valid.clear();
  Isol.clear();
  IsMatchedCand.clear();
  IsHaloCand.clear();
  Mip.clear();

  }
      
    // ---- General L1AnalysisGMTDataFormat information.
    
    int EvBx;
    
 
    		  
    //Global Muon Trigger
    int gmt_muons;
    std::vector<int>	  Bx;
    std::vector<int>	  Quality;
    std::vector<float>    Pt;
    std::vector<float>    Eta;
    std::vector<float>    Phi;
    std::vector<int>	  Charge;
    std::vector<bool>  	  Charge_Valid;
    std::vector<bool>     Isol;
    std::vector<bool>     IsMatchedCand;
    std::vector<bool>     IsHaloCand;
    std::vector<bool>     Mip;

    
  }; 
} 
#endif


