#ifndef __TrUpS_L1AnalysisBMTFDataFormat_H__
#define __TrUpS_L1AnalysisBMTFDataFormat_H__



#include <vector>
#include "TMatrixD.h"
#include <string>

namespace TrUpS
{
  struct L1AnalysisBMTFDataFormat
  {

    L1AnalysisBMTFDataFormat(){Reset();};
    ~L1AnalysisBMTFDataFormat(){};

    void Reset()
    {

    phSize = 0;

    phBx.clear();
    phWh.clear();
    phSe.clear();
    phSt.clear();
    phAng.clear();
    phGlobPhi.clear(); 
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
    thCode.clear();
    thTheta.clear();

    bmtfSize = 0;
    bmtfPt.clear();
    bmtfEta.clear();
    bmtfPhi.clear();
    bmtfqual.clear();
    bmtfch.clear();
    bmtfbx.clear();
    bmtfprocessor.clear();
    bmtftrAddress.clear();
    bmtfwh.clear();
    bmtfFineBit.clear();
    }

    // ---- L1AnalysisBMTFDataFormat information.

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

    std::vector<int> thTheta;
    std::vector<int> thCode; 
 
    int bmtfSize;
    std::vector<int> bmtfPt;
    std::vector<int> bmtfEta;
    std::vector<int> bmtfPhi;
    std::vector<int> bmtfqual;
    std::vector<int> bmtfch;
    std::vector<int> bmtfbx;
    std::vector<int> bmtfprocessor;
    std::vector<int> bmtftrAddress;
    std::vector<int> bmtfwh;
    std::vector<int> bmtfFineBit;

  };
}
#endif


