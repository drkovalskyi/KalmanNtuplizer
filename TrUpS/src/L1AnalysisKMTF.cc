//original author: g karathanasis
//
#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisKMTF.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
//#include "DataFormats/L1KalmanMuonTrigger/interface/L1KalmanMuTrack.h"
#include <sstream>
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/L1TMuon/interface/L1MuKBMTrack.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"

TrUpS::L1AnalysisKMTF::L1AnalysisKMTF(edm::ConsumesCollector && ix)
{
}


TrUpS::L1AnalysisKMTF::~L1AnalysisKMTF()
{

}


void TrUpS::L1AnalysisKMTF::SetKMTF(const BXVector<L1MuKBMTrack>& coll, int& ctr, int bx) {
  //std::cout<<"skata "<<coll.size()<<std::endl;
  for (auto mu = coll.begin(); mu != coll.end(); ++mu) {
    //  std::cout<<ctr<<std::endl;
      ctr++;
      //mu->unconstrainedP4().pt() 
      kmtf_.kmtfPt.push_back(mu->pt());
      kmtf_.kmtfEta.push_back(mu->eta());
      kmtf_.kmtfPhi.push_back(mu->phi());
      kmtf_.kmtfCurv.push_back(mu->curvature());
      kmtf_.kmtfCurvAtVertex.push_back(mu->curvatureAtVertex());
      kmtf_.kmtfCurvAtMuon.push_back(mu->curvatureAtMuon());
      kmtf_.kmtfPhiAtMuon.push_back(mu->phiAtMuon());
      kmtf_.kmtfPhiBAtMuon.push_back(mu->phiBAtMuon());
      kmtf_.kmtfPosAngle.push_back(mu->positionAngle());

     kmtf_.kmtfCoarseEta.push_back(mu->coarseEta());
     kmtf_.kmtfhitPattern.push_back(mu->hitPattern());
     kmtf_.kmtfFineEta.push_back(mu->fineEta());
     kmtf_.kmtfHasFineEta.push_back(mu->hasFineEta());
   //  kmtf_.kmtfCoarseEtaPat.push_back(mu->etaCoarsePattern());
     kmtf_.kmtfStep.push_back(mu->step());
          kmtf_.kmtfSector.push_back(mu->sector());
     // kmtf_.kmtfDeltaK.push_back(mu->deltaK());
      kmtf_.kmtfUncPt.push_back(mu->ptUnconstrained());
      kmtf_.kmtfCharge.push_back(mu->charge());
      kmtf_.kmtfDxy.push_back(mu->dxy());
      kmtf_.kmtfQual.push_back(mu->quality());
      kmtf_.kmtfChi2.push_back(mu->approxChi2());
      kmtf_.kmtfRank.push_back(mu->rank());
      kmtf_.kmtfbx.push_back(mu->bx());
      std::vector<float> tempsc,tempwh,tempst;
      int tempn=0;
      for (const auto s : mu->stubs()){
         tempsc.push_back(s->scNum());
         tempwh.push_back(s->whNum());
         tempst.push_back(s->stNum());
         tempn++;
       } 
       kmtf_.kmtfStubSec.push_back(tempsc);
       kmtf_.kmtfStubWh.push_back(tempwh);
       kmtf_.kmtfStubSt.push_back(tempst);
       kmtf_.kmtfNStub.push_back(tempn);
      //kmtf_.kmtfNormalizedChi2.push_back(mu->approxChi2());
     // bmtf_.bmtftrAddress.push_back(mu->hwTrackAddress());

    }
        kmtf_.kmtfSize = ctr;




}


void TrUpS::L1AnalysisKMTF::SetHWKMTF(const l1t::RegionalMuonCandBxCollection& coll, int& ctr, int bx) {

  for (auto mu = coll.begin(bx); mu != coll.end(bx); ++mu) {
      //cout<<ctr<<endl;
         ctr++;
         kmtf_.kmtfHWPt.push_back(mu->hwPt());
         kmtf_.kmtfHWEta.push_back(mu->hwEta());
         kmtf_.kmtfHWFineBit.push_back(mu->hwHF());
         kmtf_.kmtfHWPhi.push_back(mu->hwPhi());
         kmtf_.kmtfHWDxy.push_back(mu->hwDXY());
         kmtf_.kmtfHWqual.push_back(mu->hwQual());
         kmtf_.kmtfHWch.push_back(mu->hwSign());
         kmtf_.kmtfHWbx.push_back(bx);
         kmtf_.kmtfHWprocessor.push_back(mu->processor());
         // bmtf_.bmtftrAddress.push_back(mu->hwTrackAddress());
         std::map<int, int>  trAdd;
         trAdd = mu->trackAddress();
         int wheel = pow(-1,trAdd[0]) * trAdd[1];
         kmtf_.kmtfHWwh.push_back(wheel);
         kmtf_.kmtfHWtrAddress.push_back(trAdd[2]);
         kmtf_.kmtfHWtrAddress.push_back(trAdd[3]);
         kmtf_.kmtfHWtrAddress.push_back(trAdd[4]);
         kmtf_.kmtfHWtrAddress.push_back(trAdd[5]);
               }
         kmtf_.kmtfHWSize = ctr;
         }
      //


