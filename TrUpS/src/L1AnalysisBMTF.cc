#include "KalmanNtuplizer/TrUpS/interface/L1AnalysisBMTF.h"
#include <FWCore/Framework/interface/ConsumesCollector.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include <sstream>

TrUpS::L1AnalysisBMTF::L1AnalysisBMTF(edm::ConsumesCollector && ix)
{
}


TrUpS::L1AnalysisBMTF::~L1AnalysisBMTF()
{

}

void TrUpS::L1AnalysisBMTF::SetDTPH(const edm::Handle<L1MuDTChambPhContainer > L1MuDTChambPhContainer, unsigned int maxDTPH)
{

   L1MuDTChambPhContainer::Phi_Container const *PhContainer = L1MuDTChambPhContainer->getContainer();

   bmtf_.phSize = PhContainer->size();
   int iphtr=0;
   double pig=acos(-1);
   for( L1MuDTChambPhContainer::Phi_Container::const_iterator
       DTPhDigiItr =  PhContainer->begin() ;
       DTPhDigiItr != PhContainer->end() ;
       ++DTPhDigiItr )
    {
      if((unsigned int) iphtr>maxDTPH-1) continue;
      bmtf_.phBx.push_back     (  DTPhDigiItr->bxNum() - DTPhDigiItr->Ts2Tag()+1 );
      bmtf_.phBxRAW.push_back     (  DTPhDigiItr->bxNum() );
      bmtf_.phTs2Tag.push_back     ( DTPhDigiItr->Ts2Tag() );
      bmtf_.phWh.push_back     (  DTPhDigiItr->whNum() );
      bmtf_.phSe.push_back     (  DTPhDigiItr->scNum() );
      bmtf_.phSt.push_back     (  DTPhDigiItr->stNum() );
      bmtf_.phAng.push_back    (  DTPhDigiItr->phi()   );
      bmtf_.phBandAng.push_back(  DTPhDigiItr->phiB()  );
      double locphi = (((double)DTPhDigiItr->phi())/4096.0);
      double newphi = locphi+(DTPhDigiItr->scNum()*(pig/6.));
      if (newphi>2*pig) newphi-=2*pig;
      if (newphi<0    ) newphi+=2*pig;
      bmtf_.phGlobPhi.push_back(  newphi               );
      bmtf_.phCode.push_back   (  DTPhDigiItr->code()  );
      bmtf_.phX.push_back      (  DTPhDigiItr->scNum() );
      bmtf_.phY.push_back      (  DTPhDigiItr->stNum()+4*(DTPhDigiItr->whNum()+2) );

      iphtr++;
    }

}


void TrUpS::L1AnalysisBMTF::SetDTTH(const edm::Handle<L1MuDTChambThContainer > L1MuDTChambThContainer, unsigned int maxDTTH)
{

   L1MuDTChambThContainer::The_Container const *ThContainer = L1MuDTChambThContainer->getContainer();

   int ithtr=0;
   bmtf_.thSize = ThContainer->size();

   for( L1MuDTChambThContainer::The_Container::const_iterator
	 DTThDigiItr =  ThContainer->begin() ;
       DTThDigiItr != ThContainer->end() ;
       ++DTThDigiItr )
     {

      if((unsigned int) ithtr>maxDTTH-1) continue;
      bmtf_.thBx.push_back( DTThDigiItr->bxNum()  );
      bmtf_.thWh.push_back( DTThDigiItr->whNum() );
      bmtf_.thSe.push_back( DTThDigiItr->scNum() );
      bmtf_.thSt.push_back( DTThDigiItr->stNum() );
      bmtf_.thX.push_back( DTThDigiItr->stNum()+4*(DTThDigiItr->whNum()+2) );
      bmtf_.thY.push_back( DTThDigiItr->scNum() );

      ostringstream  ss1, ss2; 
      ss1.clear(); ss2.clear();
      ss1<<"9"; ss2<<"9";

      for(int j=0; j<7; j++){
        ss1<<DTThDigiItr->position(6-j);
         ss2<<DTThDigiItr->code(6-j) ;
      }
      bmtf_.thTheta.push_back(stoi(ss1.str())) ;
      bmtf_.thCode.push_back(stoi(ss2.str()));

      ithtr++;

    }
}

void TrUpS::L1AnalysisBMTF::SetBMTF(const l1t::RegionalMuonCandBxCollection& coll, int& ctr, int bx) {

  for (auto mu = coll.begin(bx); mu != coll.end(bx); ++mu) {
      //cout<<ctr<<endl;
      ctr++;
      bmtf_.bmtfPt.push_back(mu->hwPt());
      bmtf_.bmtfEta.push_back(mu->hwEta());
      bmtf_.bmtfFineBit.push_back(mu->hwHF());
      bmtf_.bmtfPhi.push_back(mu->hwPhi());
      bmtf_.bmtfqual.push_back(mu->hwQual());
      bmtf_.bmtfch.push_back(mu->hwSign());
      bmtf_.bmtfbx.push_back(bx);
      bmtf_.bmtfprocessor.push_back(mu->processor());
     // bmtf_.bmtftrAddress.push_back(mu->hwTrackAddress());
      std::map<int, int>  trAdd;
      trAdd = mu->trackAddress();
      int wheel = pow(-1,trAdd[0]) * trAdd[1];
      bmtf_.bmtfwh.push_back(wheel);
      bmtf_.bmtftrAddress.push_back(trAdd[2]);
      bmtf_.bmtftrAddress.push_back(trAdd[3]);
      bmtf_.bmtftrAddress.push_back(trAdd[4]);
      bmtf_.bmtftrAddress.push_back(trAdd[5]);

    }
        bmtf_.bmtfSize = ctr;

}



