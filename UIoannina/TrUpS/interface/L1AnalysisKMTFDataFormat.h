//original author: g karathanasis , georgios.karathanasis@cern.ch
//
#ifndef __TrUpS_L1AnalysisKMTFDataFormat_H__
#define __TrUpS_L1AnalysisKMTFDataFormat_H__



#include <vector>
#include "TMatrixD.h"
#include <string>

namespace TrUpS
{
  struct L1AnalysisKMTFDataFormat
  {

    L1AnalysisKMTFDataFormat(){Reset();};
    ~L1AnalysisKMTFDataFormat(){};

    void Reset()
    {


    kmtfSize = 0;
    kmtfPt.clear();
    kmtfEta.clear();
    kmtfPhi.clear();
    kmtfbx.clear();
    kmtfCurv.clear();
    kmtfCurvAtVertex.clear();
    kmtfCharge.clear();
    kmtfDxy.clear();
    kmtfQual.clear();
    kmtfChi2.clear();
    kmtfCurvAtMuon.clear();
    kmtfPhiAtMuon.clear();
    kmtfPhiBAtMuon.clear();
    kmtfPosAngle.clear();
    kmtfCoarseEta.clear();
    kmtfFineEta.clear();
    kmtfHasFineEta.clear();
    kmtfhitPattern.clear();
    kmtfCoarseEtaPat.clear();
    kmtfDeltaK.clear();
    kmtfUncPt.clear();    
    kmtfStep.clear();
    kmtfSector.clear();
    kmtfStubSec.clear();
    kmtfStubWh.clear();
    kmtfStubSt.clear();
    kmtfNStub.clear();
    kmtfRank.clear();

    kmtfHWSize = 0;
    kmtfHWPt.clear();
    kmtfHWEta.clear();
    kmtfHWPhi.clear();
    kmtfHWDxy.clear();
    kmtfHWqual.clear();
    kmtfHWch.clear();
    kmtfHWbx.clear();
    kmtfHWprocessor.clear();
    kmtfHWtrAddress.clear();
    kmtfHWwh.clear();
    kmtfHWFineBit.clear();
    
    
    }

    // ---- L1AnalysisBMTFDataFormat information.

    int kmtfSize;
    std::vector<float> kmtfPt;
    std::vector<float> kmtfEta;
    std::vector<float> kmtfPhi;
    std::vector<float> kmtfbx;
    std::vector<float> kmtfCurv;
    std::vector<float> kmtfCurvAtVertex;
     std::vector<float>  kmtfCharge;
     std::vector<float> kmtfDxy;
     std::vector<float> kmtfQual;
     std::vector<float> kmtfChi2;
    std::vector<float>  kmtfCurvAtMuon;
    std::vector<float> kmtfPhiAtMuon;
    std::vector<float> kmtfPhiBAtMuon;
    std::vector<float> kmtfPosAngle;
   std::vector<float>  kmtfCoarseEta;
    std::vector<float>  kmtfFineEta;
    std::vector<bool>  kmtfHasFineEta;
    std::vector<float> kmtfhitPattern;
    std::vector<float> kmtfCoarseEtaPat;
    std::vector<float> kmtfDeltaK;
    std::vector<float> kmtfUncPt;
         std::vector<float> kmtfRank;
    std::vector<float> kmtfStep;
    std::vector<float> kmtfSector;
    std::vector<float> kmtfNStub;
     std::vector<std::vector<float>> kmtfStubSec;
    std::vector<std::vector<float>> kmtfStubSt;
    std::vector<std::vector<float>> kmtfStubWh;

    int kmtfHWSize;
    std::vector<int> kmtfHWPt;
    std::vector<int> kmtfHWEta;
    std::vector<int> kmtfHWPhi;
    std::vector<int> kmtfHWDxy;
    std::vector<int> kmtfHWqual;
    std::vector<int> kmtfHWch;
    std::vector<int> kmtfHWbx;
    std::vector<int> kmtfHWprocessor;
    std::vector<int> kmtfHWtrAddress;
    std::vector<int> kmtfHWwh;
    std::vector<int> kmtfHWFineBit;
  };
}
#endif


