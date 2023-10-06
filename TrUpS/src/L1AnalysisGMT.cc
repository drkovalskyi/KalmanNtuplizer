#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisGMT.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>
#include "DataFormats/Common/interface/Handle.h"

#include <vector>
#include "TMatrixD.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


TrUpS::L1AnalysisGMT::L1AnalysisGMT(edm::ConsumesCollector && ix)
{
}


TrUpS::L1AnalysisGMT::~L1AnalysisGMT()
{
}

void TrUpS::L1AnalysisGMT::SetGMT(const L1MuGMTReadoutCollection* gmtrc)
{
std::vector<L1MuGMTReadoutRecord> gmt_records = gmtrc->getRecords();
  std::vector<L1MuGMTReadoutRecord>::const_iterator igmtrr;



  for(igmtrr=gmt_records.begin(); igmtrr!=gmt_records.end(); igmtrr++) {
   
   if(igmtrr->getBxInEvent()==0) {
     gmt_.EvBx = igmtrr->getBxNr();
   }
   
  //
  // GMT_. Trigger
  //  
  
  std::vector<L1MuGMTExtendedCand>::const_iterator gmt_iter;
  std::vector<L1MuGMTExtendedCand> exc = igmtrr->getGMTCands();
  for(gmt_iter=exc.begin(); gmt_iter!=exc.end(); gmt_iter++) {
    if ( (unsigned) gmt_.gmt_muons < 12 && !(*gmt_iter).empty() ) {
        gmt_.Bx.push_back((*gmt_iter).bx());
        gmt_.Quality.push_back((*gmt_iter).quality());
        gmt_.Eta.push_back((*gmt_iter).etaValue());
        gmt_.Phi.push_back((*gmt_iter).phiValue()); 
        gmt_.Pt.push_back((*gmt_iter).ptValue());
        gmt_.Charge.push_back((*gmt_iter).charge());
        gmt_.Charge_Valid.push_back((*gmt_iter).charge_valid());
        gmt_.Isol.push_back((*gmt_iter).isol());
        gmt_.IsMatchedCand.push_back((*gmt_iter).isMatchedCand());
        gmt_.IsHaloCand.push_back((*gmt_iter).isHaloCand());
        gmt_.Mip.push_back((*gmt_iter).mip());
	
      }

      gmt_.gmt_muons++;
    }
  }

if(gmt_.gmt_muons ==0 ){
        gmt_.Bx.push_back(-100);
        gmt_.Quality.push_back(-100);
        gmt_.Eta.push_back(-100);
        gmt_.Phi.push_back(-100); 
        gmt_.Pt.push_back(-100);
        gmt_.Charge.push_back(-100);
        gmt_.Charge_Valid.push_back(false);
        gmt_.Isol.push_back(false);
        gmt_.IsMatchedCand.push_back(false);
        gmt_.IsHaloCand.push_back(false);
        gmt_.Mip.push_back(false);
}
    
  }


