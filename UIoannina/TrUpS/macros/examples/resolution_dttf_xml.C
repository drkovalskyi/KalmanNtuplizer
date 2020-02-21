#include <iostream>
#include <sstream>
#include <istream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
#include <functional>
#include <vector>
#include <cassert>
#include <algorithm>
#include <sstream>

#include "TH1F.h"
#include "TString.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TDirectory.h"
#include "TFile.h"
#include "TLegend.h"
using namespace std;


#include "./classes/L1TreeClass.C"
#include "./classes/GENTreeClass.C"
//#include "/home/gflouris/Analysis/setTDRStyle.C"


#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>

using boost::property_tree::ptree;
using boost::property_tree::write_xml;
using boost::property_tree::xml_writer_settings;

void write_xml(std::map<string, string> map_data, ptree& data);

void init_map(std::map<string, string> &	map_data);

string my_to_string(int Number){
string Result;         
ostringstream convert; 
convert << Number;     
Result = convert.str();
return Result;
}

string my_to_string(double Number){
string Result;
ostringstream convert;  
convert << Number;      
Result = convert.str(); 
return Result;
}

int main(int argc, char** argv){

  char *cfile = argv[1];
  
 // bool upgrade_plots = true;
  
  //setTDRStyle();

  L1TreeClass l1c;
  GENTreeClass genc;

  TString in_file = cfile;
  
  TFile *f = new TFile(in_file);
  TFile *file1 = new TFile(in_file);
  
  TDirectory * dirgen = (TDirectory*)f->Get(in_file+":/GENTProducer");
  TTree *treegen;
  dirgen->GetObject("GENTree",treegen);

  TDirectory * dir = (TDirectory*)file1->Get(in_file+":/L1TProducer");
  TTree *treel1;
  dir->GetObject("L1Tree",treel1);

  l1c.Init(treel1);
  genc.Init(treegen);

  
// float phtf_pt[1700];
// ifstream infile1;
// //for(int i=0; i<17; i++){
// 
// std::stringstream sst; sst<< "./DTTF_up/phtf_output100.txt";
// string name = sst.str();
// infile1.open (name.c_str(), ifstream::in);
// 
//   for(int k=0; k<1700; k++){
//     infile1 >> phtf_pt[k];
//   }
// 
// infile1.close();
//}

  
  
  int nentries = l1c.fChain -> GetEntries();

  float PCKtoPHYS[33] = {-100, 0.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10., 12., 14., 16., 18., 20., 25., 30., 35., 40., 45., 50., 60., 70., 80., 90., 100., 120., 140.,160.};

  
int ff =0 ;
float res = 0;
int count =0;
int datas_bad = 0;

float genpt=0,geneta=0,genphi=0, gmtpt=0,gmteta=0,gmtphi=0, dttf_ph_pt=0, tr_add_1 = 0, tr_add_2 = 0, tr_add_3 = 0, tr_add_4 = 0, dttf_phi = 0, dttf_qual = 0;



std::map<string, string> map_data;



    boost::property_tree::ptree rootNode;
    boost::property_tree::ptree eventNode;
    boost::property_tree::ptree setNode2;
    boost::property_tree::ptree fieldNode1;
    boost::property_tree::ptree fieldNode_gen;
    boost::property_tree::ptree fieldNode_gmt;
    boost::property_tree::ptree fieldNode_tr;
        boost::property_tree::ptree fieldNode_dttf;

boost::property_tree::ptree fieldNode_th;
boost::property_tree::ptree fieldNode_ph;

boost::property_tree::ptree pt;
   
cout<<"Analysing tree with: "<<nentries<<" events"<<endl;
int ts2tag = 0, bxxx = 0;
  for(int i=0; i<nentries; i++){

    l1c.GetEntry(i);
    genc.GetEntry(i);
    
      int good_m_k[10] = {0,0,0,0,0,0,0,0,0,0};
      int good_m_kk=0;
int deb_good_m_kk=0;
	
      for(int k=0; k<l1c.phSize; k++){
//		if(l1c.phBxRAW[k]==0 && l1c.phTs2Tag[k]==0 ) {good_m_k[k] = 1; good_m_kk++; ts2tag++;}
		if(l1c.phBx[k]==1 && l1c.phTs2Tag[k]==0 && l1c.phWh[k]==0 && l1c.phSe[k]==0) {   good_m_kk++;}
     	 
      }


  if(good_m_kk!=4) continue; ///Hits at all stations
  if(good_m_kk>4) cerr<<i<<"  More than four"<<endl;
    //if(count==179 || count==328 || count==355) {
//		cout<<"Bad event "<<i<<"  "<<good_m_kk<<"  "<<endl;
 //               cout<<"1c.phBxRAW[k]+<<l1c.Ts2Tag[k]<<<l1c.phSize<<<<l1c.phWh[k]<<<<l1c.phSt[k]<<<<l1c.phSe[k]<<<<l1c.phAng[k]<<<<l1c.phBandAng[k]<<<<l1c.phCode[k]"<<endl;

//	      for(int k=0; k<l1c.phSize; k++){
 //               cout<<l1c.phBxRAW[k]<<"\t"<<l1c.phTs2Tag[k]<<"\t"<<l1c.phSize<<"\t"<<l1c.phWh[k]<<"\t"<<l1c.phSt[k]<<"\t"<<l1c.phSe[k]<<"\t"<<l1c.phAng[k]<<"\t"<<l1c.phBandAng[k]<<"\t"<<l1c.phCode[k]<<endl;

//cout<<endl<<l1c.phBxRAW[k]<<endl;
  //    }
//}
    	
    ff = 0;

    for(int l=0; l<l1c.trSize; l++){
        if(l1c.trBx[l]==1 && l1c.trTag[l]==0)  {
	  int ptpck = l1c.trPtPck[l];
	  //if (ptpck==0) continue;
//	  if(l1c.trTag[l]!=0) cerr<<"tr tag non zero"<<endl;
	  dttf_ph_pt = (PCKtoPHYS[ptpck]);
	  tr_add_1 = l1c.trAddress[0];
          tr_add_2 = l1c.trAddress[1];
          tr_add_3 = l1c.trAddress[2];
          tr_add_4 = l1c.trAddress[3];
          dttf_qual = l1c.trQual[l];
	  dttf_phi = l1c.trPhiPck[l];
	}
     }
    
     genpt = genc.genPt_Mu[0];
     geneta = genc.genPhi_Mu[0];
     genphi = genc.genEta_Mu[0];


     for(int l=0; l<l1c.gmt_muons; l++){
	if(l1c.Bx[l]==0){
	 gmtpt = l1c.Pt[l];
	 gmtphi = l1c.Phi[l];
	 gmteta = l1c.Eta[l];}
      else	ff++;
     } 
  if(ff!=0) continue;

 // if(upgrade_plots){
  
  if(count<201700){
    
    

    init_map(map_data);

    fieldNode1.clear();
    fieldNode_gen.clear();
    fieldNode_gmt.clear(); 
    fieldNode_tr.clear();
    fieldNode_th.clear();
    fieldNode_ph.clear();
    fieldNode_dttf.clear();
    eventNode.clear();
    
    fieldNode1.add("tree_event",i);
    fieldNode1.add("muon","1");
    fieldNode1.put("<xmlattr>.type", "event");
    eventNode.add_child("info", fieldNode1);
  
    eventNode.put("<xmlattr>.id", count);


    map_data["tremu_pt"] = my_to_string(dttf_ph_pt);
    map_data["tremu_tradd_st1"] = my_to_string(tr_add_1);
    map_data["tremu_tradd_st2"] = my_to_string(tr_add_2);
    map_data["tremu_tradd_st3"] = my_to_string(tr_add_3);
    map_data["tremu_tradd_st4"] = my_to_string(tr_add_4);
    map_data["tremu_phi"] = my_to_string(dttf_phi);
    map_data["tremu_qual"] = my_to_string(dttf_qual);

    map_data["gen_pt"] = my_to_string(genpt);
    map_data["gen_phi"] = my_to_string(genphi);
    map_data["gen_eta"] = my_to_string(geneta);
    map_data["gmt_pt"] = my_to_string(gmtpt);
    map_data["gmt_phi"] = my_to_string(gmtphi);
    map_data["gmt_eta"] = my_to_string(gmteta);
    
    fieldNode_gen.add("pt",map_data["gen_pt"]);
    fieldNode_gen.add("eta",map_data["gen_eta"]);    
    fieldNode_gen.add("phi",map_data["gen_phi"]);
    fieldNode_gen.put("<xmlattr>.type", "GEN");
    eventNode.add_child("info", fieldNode_gen);

    
    fieldNode_gmt.add("pt",map_data["gmt_pt"]);
    fieldNode_gmt.add("eta",map_data["gmt_eta"]);    
    fieldNode_gmt.add("phi",map_data["gmt_phi"]);
    fieldNode_gmt.put("<xmlattr>.type", "GMT");
    eventNode.add_child("info", fieldNode_gmt);

    fieldNode_tr.add("pt",map_data["tremu_pt"]);
    fieldNode_tr.add("tradd_st1",map_data["tremu_tradd_st1"]);
    fieldNode_tr.add("tradd_st2",map_data["tremu_tradd_st2"]);
    fieldNode_tr.add("tradd_st3",map_data["tremu_tradd_st3"]);
    fieldNode_tr.add("tradd_st4",map_data["tremu_tradd_st4"]);
    fieldNode_tr.add("phi",map_data["tremu_phi"]);
    fieldNode_tr.add("qual",map_data["tremu_qual"]);
    
    fieldNode_tr.put("<xmlattr>.type", "tr_emu");
    eventNode.add_child("info", fieldNode_tr);

bool good_event = true;
          //for(int l=0; l<l1c.phSize; l++){

          //      if(l1c.phWh[l]!=0 || l1c.phSe[l]!=0) good_event = false;
          //}
    
    if(good_event){     
	  for(int l=0; l<l1c.phSize; l++){
	    //  if(l1c.phBx[l]==1){
            if(l1c.phBxRAW[l]==0 && l1c.phTs2Tag[l]==0 && l1c.phWh[l]==0 && l1c.phSe[l]==0 ) {
	       if(l1c.phTs2Tag[l]!=0) cerr<<i<<" Mixed up event"<<endl;
		if(l1c.phBxRAW[l]!=0) cerr<<i<<"Wrong bx"<<endl;
	      string station = my_to_string(l1c.phSt[l]);

	      map_data["phemu_ang_st"+station] = my_to_string(l1c.phAng[l]);
	      if(l1c.phSt[l] != 3) {
		map_data["phemu_b_ang_st"+station] = my_to_string(l1c.phBandAng[l]);
		  fieldNode_ph.add("b_ang_st"+station,map_data["phemu_b_ang_st"+station]);
	      }
	      map_data["phemu_code_st"+station] = my_to_string(l1c.phCode[l]);
	      map_data["phemu_wh_st"+station] = my_to_string(l1c.phWh[l]);
	      map_data["phemu_se_st"+station] = my_to_string(l1c.phSe[l]);
 	
		if(l1c.phWh[l]!=0) cerr<<i<<" Diff wheel"<<endl;
		if(l1c.phSe[l]!=0) cerr<<i<<" Diff Sec"<<endl; 

	      
	      }
	      
	      
	 
	  }
	  	  for(int l=0; l<4; l++){
		    fieldNode_ph.add("ang_st"+my_to_string(l+1),map_data["phemu_ang_st"+to_string(l+1)]);
		    fieldNode_ph.add("wh_st"+my_to_string(l+1),map_data["phemu_wh_st"+to_string(l+1)]);    
		    fieldNode_ph.add("se_st"+my_to_string(l+1),map_data["phemu_se_st"+to_string(l+1)]);
		    fieldNode_ph.add("code_st"+my_to_string(l+1),map_data["phemu_code_st"+to_string(l+1)]);

		  }
	   fieldNode_ph.put("<xmlattr>.type", "ph_emu");
	    eventNode.add_child("info", fieldNode_ph);

	  int phcount = 0;
	     for(int l=0; l<l1c.thSize; l++){
 		  if(l1c.thBx[l]==1) {
		   	      string station = my_to_string(l1c.thSt[l]);

			      stringstream s1; s1<<l1c.thTheta[l][0]<<l1c.thTheta[l][1]<<l1c.thTheta[l][2]<<l1c.thTheta[l][3]<<l1c.thTheta[l][4]<<l1c.thTheta[l][5]<<l1c.thTheta[l][6];
		      	      map_data["themu_hits_st"+station] = s1.str();
			      map_data["themu_wh_st"+station] = my_to_string(l1c.thWh[l]);
			      map_data["themu_se_st"+station] = my_to_string(l1c.thSe[l]);
		}
	      }
      for(int l=0; l<3; l++){
		      fieldNode_th.add("hits_st"+my_to_string(l+1),map_data["themu_hits_st"+to_string(l+1)]);
			      fieldNode_th.add("wh_st"+my_to_string(l+1),map_data["themu_wh_st"+to_string(l+1)]);    
			      fieldNode_th.add("se_st"+my_to_string(l+1),map_data["themu_se_st"+to_string(l+1)]);
      }
	    fieldNode_th.put("<xmlattr>.type", "th_emu");
	    eventNode.add_child("info", fieldNode_th);

 }




	    fieldNode_dttf.add("pt","-999999");
            fieldNode_dttf.add("tradd_st1","-999999");
            fieldNode_dttf.add("tradd_st2","-999999");
            fieldNode_dttf.add("tradd_st3","-999999");
            fieldNode_dttf.add("tradd_st4","-999999");
            fieldNode_dttf.add("phi","-999999");
            fieldNode_dttf.add("qual","-999999");

	    fieldNode_dttf.put("<xmlattr>.type", "DTTF");
	    eventNode.add_child("info", fieldNode_dttf);


    //write_xml(map_data,data);
    count++;
    rootNode.add_child("Event", eventNode);

  }
  
 // }



}
	
	
  pt.add_child("Data", rootNode);
	
cout<<"count = "<<count<<endl;	
cout<<"bxx = "<<bxxx<<endl;	
cout<<"ts2tag = "<<ts2tag<<endl;
cout<<"ff = "<<ff<<endl;
write_xml("./output.xml", pt, std::locale(), xml_writer_settings<char>(' ', 4));

return 0;

}
/*
 void write_xml(std::map<string, string> map_data, ptree& data){
 
       data.add("muons", 1);

        data.add("Event.gen.pt",map_data["gen_pt"]);
        data.add("gen.eta",map_data["gen_eta"]);
        data.add("gen.phi",map_data["gen_phi"]);
 
        data.add("gmt.pt",map_data["gmt_pt"]);
        data.add("gmt.eta",map_data["gmt_eta"]);
        data.add("gmt.phi",map_data["gmt_phi"]);
 
        data.add("tr_emu.pt",map_data["tremu_pt"]);

        data.add("ph_emu.ang_st1",map_data["phemu_ang_st1"]);
        data.add("ph_emu.b_ang_st1",map_data["phemu_b_ang_st1"]);
        data.add("ph_emu.code_st1",map_data["phemu_code_st1"]);
        data.add("ph_emu.wh_st1",map_data["phemu_wh_st1"]);
        data.add("ph_emu.se_st1",map_data["phemu_se_st1"]);

        data.add("ph_emu.ang_st2",map_data["phemu_ang_st2"]);
        data.add("ph_emu.b_ang_st2",map_data["phemu_b_ang_st2"]);
        data.add("ph_emu.code_st2",map_data["phemu_code_st2"]);
        data.add("ph_emu.wh_st2",map_data["phemu_wh_st2"]);
        data.add("ph_emu.se_st2",map_data["phemu_se_st2"]);
	        
	data.add("ph_emu.ang_st3",map_data["phemu_ang_st3"]);
        data.add("ph_emu.code_st3",map_data["phemu_code_st3"]);
        data.add("ph_emu.wh_st3",map_data["phemu_wh_st3"]);
        data.add("ph_emu.se_st3",map_data["phemu_se_st3"]);
	
        data.add("ph_emu.ang_st4",map_data["phemu_ang_st4"]);
        data.add("ph_emu.b_ang_st4",map_data["phemu_b_ang_st4"]);
        data.add("ph_emu.code_st4",map_data["phemu_code_st4"]);
        data.add("ph_emu.wh_st4",map_data["phemu_wh_st4"]);
        data.add("ph_emu.se_st4",map_data["phemu_se_st4"]);
	


        data.add("th_emu.hits_st1",map_data["themu_hits_st1"]);
        data.add("th_emu.wh_st1",map_data["themu_wh_st1"]);
        data.add("th_emu.se_st1",map_data["themu_se_st1"]);
        data.add("th_emu.hits_st2",map_data["themu_hits_st2"]);
        data.add("th_emu.wh_st2",map_data["themu_wh_st2"]);
        data.add("th_emu.se_st2",map_data["themu_se_st2"]);
        data.add("th_emu.hits_st3",map_data["themu_hits_st3"]);
        data.add("th_emu.wh_st3",map_data["themu_wh_st3"]);
        data.add("th_emu.se_st3",map_data["themu_se_st3"]);

	data.add("dttf.pt",map_data["dttf_pt"]);
 
 }

*/

 void init_map(std::map<string, string> &map_data){
 
// typedef std::map<std::string, std::string>::iterator it_type;
// for(it_type iterator = map_data.begin(); iterator != map_data.end(); iterator++) {
     // iterator->first = key
     // iterator->second = value
     //iterator->second = "-99999";
   
// }
        map_data["gen_pt"] = "-999999";
        map_data["gen_eta"] = "-999999";
        map_data["gen_phi"] = "-999999";
 
        map_data["gmt_pt"] = "-999999";
        map_data["gmt_eta"] = "-999999";
        map_data["gmt_phi"] = "-999999";
 
        map_data["tremu_pt"] = "-999999";
        map_data["tremu_tradd_st1"] = "-999999";
        map_data["tremu_tradd_st2"] = "-999999";
        map_data["tremu_tradd_st3"] = "-999999";
        map_data["tremu_tradd_st4"] = "-999999";
        map_data["tremu_phi"] = "-999999";
        map_data["tremu_qual"] = "-999999";


        map_data["phemu_ang_st1"] = "-999999";
        map_data["phemu_b_ang_st1"] = "-999999";
        map_data["phemu_code_st1"] = "-999999";
        map_data["phemu_wh_st1"] = "-999999";
        map_data["phemu_se_st1"] = "-999999";

        map_data["phemu_ang_st2"] = "-999999";
        map_data["phemu_b_ang_st2"] = "-999999";
        map_data["phemu_code_st2"] = "-999999";
        map_data["phemu_wh_st2"] = "-999999";
        map_data["phemu_se_st2"] = "-999999";
	        
	map_data["phemu_ang_st3"] = "-999999";
        map_data["phemu_code_st3"] = "-999999";
        map_data["phemu_wh_st3"] = "-999999";
        map_data["phemu_se_st3"] = "-999999";
	
        map_data["phemu_ang_st4"] = "-999999";
        map_data["phemu_b_ang_st4"] = "-999999";
        map_data["phemu_code_st4"] = "-999999";
        map_data["phemu_wh_st4"] = "-999999";
        map_data["phemu_se_st4"] = "-999999";

        map_data["themu_hits_st1"] = "-999999";
        map_data["themu_wh_st1"] = "-999999";
        map_data["themu_se_st1"] = "-999999";
        map_data["themu_hits_st2"] = "-999999";
        map_data["themu_wh_st2"] = "-999999";
        map_data["themu_st_st2"] = "-999999";
        map_data["themu_hits_st3"] = "-999999";
        map_data["themu_wh_st3"] = "-999999";
        map_data["themu_se_st3"] = "-999999";

        map_data["dttf_pt"]      = "-999999";
        map_data["dttf_tradd_st1"] = "-999999";
        map_data["dttf_tradd_st2"] = "-999999";
        map_data["dttf_tradd_st3"] = "-999999";
        map_data["dttf_tradd_st4"] = "-999999";
        map_data["dttf_phi"] = "-999999";
        map_data["dttf_qual"] = "-999999";

 
 }	
