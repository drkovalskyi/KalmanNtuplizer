#ifndef __TrUpS_GenMuonDataFormat_H__
#define __TrUpS_GenMuonDataFormat_H__

//-------------------------------------------------------------------------------
// Created 07/03/2013 - G. Flouris
// 
//  
// Original code : 
//-------------------------------------------------------------------------------

#include <vector>
#include "TMatrixD.h"
#include "DataFormats/Candidate/interface/Particle.h"
typedef reco::Particle::LorentzVector LorentzVector;

namespace TrUpS
{
  struct GenMuonDataFormat
  {

    GenMuonDataFormat(){Reset();};
    ~GenMuonDataFormat(){};
    
    void Reset()
    {


    genPt_Mu.clear();
    genEta_Mu.clear();
    genPhi_Mu.clear();
    genStatus_Mu.clear();
    genQ_Mu.clear();
    genDxy_Mu.clear();
    genP4_Mu.clear();
    gen_muons = 0;
    }


    std::vector<float> genPt_Mu;
    std::vector<float> genQ_Mu;
    std::vector<float> genPhi_Mu;
    std::vector<float> genEta_Mu;
    std::vector<float> genStatus_Mu;
    std::vector<float> genDxy_Mu;
    std::vector<LorentzVector> genP4_Mu;
    int			gen_muons;

  }; 
} 
#endif


