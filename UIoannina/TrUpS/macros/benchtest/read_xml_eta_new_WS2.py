#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------- Stavros Mallios ----------------------
#09/02/2016 : 1. changed the fist event read pointer ---
#                for 80M algo to 55                  ---
#                                                    ---
#12/02/2016 : 1. added write_bad_events() function   ---
#             2. print 'η' value to reports          ---
#                                                    ---
#19/02/2016 : 1. Print Eta inputs for all Wheels     ---
#												     ---
#22/02/2016 : 1. Print central sectors for all Wheels --
#			  2. Reads all WS muons and prints them  ---
#				 in Wedge_Sorter_Outputs.txt	  	 ---
#-------------------------------------------------------


import wx
from lxml import etree
from ROOT import gROOT, TCanvas, TH1F, TH2F, TLatex
gROOT.Reset()

			
#-------- Create bad events Files --------
filebad_events_pt = open("phtftests/report/bad_events_pt.txt", "wb")
filebad_events_phi = open("phtftests/report/bad_events_phi.txt", "wb")
filebad_events_qual = open("phtftests/report/bad_events_qual.txt", "wb")
filebad_events_traddr = open("phtftests/report/bad_events_traddr.txt", "wb")
filebad_events_traddr_1 = open("phtftests/report/bad_events_traddr_st1.txt", "wb")
filebad_events_traddr_2 = open("phtftests/report/bad_events_traddr_st2.txt", "wb")
filebad_events_traddr_3 = open("phtftests/report/bad_events_traddr_st3.txt", "wb")
filebad_events_traddr_4 = open("phtftests/report/bad_events_traddr_st4.txt", "wb")
filebad_events_sig = open("phtftests/report/bad_events_sig.txt", "wb")# added
filebad_events_eta = open("phtftests/report/bad_events_eta.txt", "wb")# added
#                  for WS
file_WS_Outputs = open("phtftests/report/Wedge_Sorter_Outputs.txt", "wb+")# added for WS outputs


#------------Create histogram files ------------------------
histo_pt = TH1F("Histogram pT","Histogram pT",200,-1,1)
histo_pt_mp7 = TH1F("histo_pt_mp7","histo_pt_mp7", 7, 0,210);
histo_pt_emu = TH1F("histo_pt_emu","histo_pt_emu", 7, 0,210);
histo_phi = TH1F("Histogram phi","Histogram phi",200,-1,1)
histo_qual = TH1F("Histogram qual","Histogram qual",200,-8,8)
histo_traddr = TH1F("Histogram TrAddr","Histogram TrAddr",200,-5,5)
histo_2d = TH2F("histo_2d","histo_2d", 26, 0, 260, 200, -1, 1) 
histo_2d_phi = TH2F("histo_2d_phi","histo_2d_phi", 120, -60, 60, 240, -120, 120)
histo_sig = TH1F("Histogram sig","Histogram sig",200,-1,1)# added
histo_eta = TH1F("Histogram eta","Histogram eta",200,-1,1)# added
#                  For WS
histo_WS_pt = TH1F("Histogram WS pT","Histogram WS pT",200,-1,1)# added
histo_WS_phi = TH1F("Histogram WS pT","Histogram WS pT",200,-1,1)# added
histo_WS_qual = TH1F("Histogram WS qual","Histogram WS qual",200,-8,8)# added
histo_WS_eta = TH1F("Histogram WS eta","Histogram WS eta",200,-1,1)# added
histo_WS_traddr = TH1F("Histogram WS traddr","Histogram WS traddr",200,-5,5)# added
histo_WS_eta_distr = TH1F("Histogram WS traddr","Histogram WS traddr",240,-120,120)# added


tree = etree.parse('phtftests/report/xmlout.xml')
events = tree.getroot()

#-------- Write first line of Bad event files -----------
filebad_events_pt.write("\nThis file records the bad events\n\n")
filebad_events_phi.write("\nThis file records the bad events\n\n")
filebad_events_qual.write("\nThis file records the bad events\n\n")
filebad_events_traddr.write("\nThis file records the bad events\n\n")
filebad_events_traddr_1.write("\nThis file records the bad events\n\n")
filebad_events_traddr_2.write("\nThis file records the bad events\n\n")
filebad_events_traddr_3.write("\nThis file records the bad events\n\n")
filebad_events_traddr_4.write("\nThis file records the bad events\n\n")
filebad_events_sig.write("\nThis file records the bad events\n\n") # added
filebad_events_eta.write("\nThis file records the bad events\n\n") # added
file_WS_Outputs.write("\nThis file records the Wedge Sorter Outputs\n\n") # added for WS outputs


app = wx.PySimpleApp()
dialog = wx.ProgressDialog("Test in progress", "read_xml_eta.py is running", len(events))
keepGoing = True

traddr = 0
ws_traddr = 0


#==================================================================== Begin Fill Bad event Files function ============================================================================
def write_bad_event(file_name):
	file_name.write(70*"+"+"\n")
	file_name.write(30*"+"+"   ID: "+str(kk)+"  "+30*"+"+"\n")
	file_name.write(70*"+"+"\n")
	file_name.write("------------------------------------------------ Inputs -------------------------------------------\n")
	file_name.write("----------- Wheel -2 (own low) ------------------------- Wheel -1 (own low)--------------------------- Wheel 0 (own low)----------------------------- Wheel +1 (own low)---------------------------- Wheel +2 (own low)\n")
	# file_name.write("--- Left sector ---\n")
	# file_name.write("ST1  ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\t\tST1  ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\n")
	# file_name.write("ST2  ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\t\tST2  ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\n")
	# file_name.write("ST3  ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"+"code: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\t\tST3  ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"+"code: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\n")
	# file_name.write("ST4  ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp2_sl_sh.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\t\tST4  ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp2_sl_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\n")
	file_name.write("--- Own sector  ---\n")
	file_name.write("ST1  ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\t"+"ST1  ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)  +"\t"+"ST1  ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\t"+"ST1  ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\t"+"ST1  ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\n")  
	file_name.write("ST2  ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\t"+"ST2  ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)  +"\t"+"ST2  ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\t"+"ST2  ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\t"+"ST2  ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\n")  
	file_name.write("ST3  ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"                                                                            +"code: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\t"+"ST3  ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"                                                                            +"code: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)  +"\t"+"ST3  ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"                                                                            +"code: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\t"+"ST3  ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"                                                                            +"code: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\t"+"ST3  ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"                                                                            +"code: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\n")
	file_name.write("ST4  ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wm2_so_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\t"+"ST4  ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wm1_so_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)  +"\t"+"ST4  ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wh0_so_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\t"+"ST4  ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp1_so_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\t"+"ST4  ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp2_so_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\n\n")  
	file_name.write("   Wheel: --- -2 --------- -1 ----------- 0 ---------- +1 ---------- +2 --\n")
	file_name.write("ET3 hits: "+str(wm2_so_sl.xpath("./info[@type='th_emu']/hits_st3")[0].text)+"  ||  "+str(wm1_so_sl.xpath("./info[@type='th_emu']/hits_st3")[0].text)+"  ||  "+str(wh0_so_sl.xpath("./info[@type='th_emu']/hits_st3")[0].text)+"  ||  "+str(wp1_so_sl.xpath("./info[@type='th_emu']/hits_st3")[0].text)+"  ||  "+str(wp2_so_sl.xpath("./info[@type='th_emu']/hits_st3")[0].text)+"\n")
	file_name.write("ET2 hits: "+str(wm2_so_sl.xpath("./info[@type='th_emu']/hits_st2")[0].text)+"  ||  "+str(wm1_so_sl.xpath("./info[@type='th_emu']/hits_st2")[0].text)+"  ||  "+str(wh0_so_sl.xpath("./info[@type='th_emu']/hits_st2")[0].text)+"  ||  "+str(wp1_so_sl.xpath("./info[@type='th_emu']/hits_st2")[0].text)+"  ||  "+str(wp2_so_sl.xpath("./info[@type='th_emu']/hits_st2")[0].text)+"\n")
	file_name.write("ET1 hits: "+str(wm2_so_sl.xpath("./info[@type='th_emu']/hits_st1")[0].text)+"  ||  "+str(wm1_so_sl.xpath("./info[@type='th_emu']/hits_st1")[0].text)+"  ||  "+str(wh0_so_sl.xpath("./info[@type='th_emu']/hits_st1")[0].text)+"  ||  "+str(wp1_so_sl.xpath("./info[@type='th_emu']/hits_st1")[0].text)+"  ||  "+str(wp2_so_sl.xpath("./info[@type='th_emu']/hits_st1")[0].text)+"\n\n")
	# file_name.write("--- Right sector ---\n")
	# file_name.write("ST1  ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\t\tST1  ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/ang_st1")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text)+"\t"+"code: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/code_st1")[0].text)+"\n")
	# file_name.write("ST2  ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\t\tST2  ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/ang_st2")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text)+"\t"+"code: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/code_st2")[0].text)+"\n")
	# file_name.write("ST3  ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"+"code: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\t\tST3  ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/ang_st3")[0].text)+"\t\t\t"+"code: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/code_st3")[0].text)+"\n")
	# file_name.write("ST4  ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp2_sr_sh.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\t\tST4  ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/ang_st4")[0].text)+"\t"+"b_ang: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text)+"\t"+"code: "+str(wp2_sr_sl.xpath("./info[@type='ph_emu']/code_st4")[0].text)+"\n")
	file_name.write("------------------------------------------------ Output -------------------------------------------\n")
	file_name.write("EMU  pt: "+str(emu_pt)+"\t"+"phi: "+str(emu_phi)+"\t "+"qual: "+str(emu_qual)+"\t"+"tradd: "+str(emu_tradd)+"\t"+"sig: "+str(emu_sig)+"\t\t"+"eta: "+str(emu_eta)+"\t\t"+"η: "+str(float(emu_eta)*0.0109)+"\n") #------------------added
	#file_name.write("MP7  pt: "+str(dttf_pt)+"\t"+"phi: "+str(dttf_phi)+"\t "+"qual: "+str(dttf_qual)+"\t"+"tradd: "+str(dttf_tradd)+"\t"+"sig: "+str(dttf_sig)+"\t\t"+"eta: "+str(dttf_eta)+"\t\t"+"η: "+str(float(dttf_eta)*0.0109)+"\t"+"\n") #----------added					
	#file_WS_Outputs.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n") #----------added
#==================================================================== END Fill Bad event Files function ============================================================================






#==================================================================== Begin read_xml() function - MAIN Function ===================================================================================
def read_xml():
	#--------------------declare all variables here :
	bad_events = 0
	bad_events_pt = 0
	bad_events_phi = 0
	bad_events_qual = 0
	bad_events_traddr = 0
	bad_events_traddr_1 = 0
	bad_events_traddr_2 = 0
	bad_events_traddr_3 = 0
	bad_events_traddr_4 = 0
	bad_events_sig = 0 # added
	bad_events_eta = 0 # added
	print
	
	global wm2_sl_sl,wm2_sl_sh,wm2_sr_sl,wm2_sr_sh,wm2_so_sl,wm2_so_sh,wm1_sl_sl,wm1_sl_sh,wm1_sr_sl,wm1_sr_sh,wm1_so_sl,wm1_so_sh,wh0_sl_sl,wh0_sl_sh,wh0_sr_sl,wh0_sr_sh,wh0_so_sl,wh0_so_sh,wp2_so_sl,wp2_so_sh,wp2_sl_sl,wp2_sl_sh,wp2_sr_sl,wp2_sr_sh
	global wp1_sl_sh,wp1_sl_sl,wp1_so_sh,wp1_so_sl,wp1_sr_sh,wp1_sr_sl
	global emu_pt,emu_phi,emu_qual,emu_tradd_st1,emu_tradd_st2,emu_tradd_st3,emu_tradd_st4,emu_sig,emu_eta,emu_tradd,dttf_pt,dttf_phi,dttf_qual,dttf_tradd_st1,dttf_tradd_st2,dttf_tradd_st3,dttf_tradd_st4,dttf_sig,dttf_eta,dttf_tradd
	global dttf_pt_WS,  dttf_phi_WS, dttf_qual_WS, dttf_tradd_st1_WS, dttf_tradd_st2_WS, dttf_tradd_st3_WS, dttf_tradd_st4_WS, dttf_sig_WS, dttf_eta_WS, dttf_tradd_WS  #--- WS muon 1
	global dttf_pt_WS2, dttf_phi_WS2,dttf_qual_WS2,dttf_tradd_st1_WS2,dttf_tradd_st2_WS2,dttf_tradd_st3_WS2,dttf_tradd_st4_WS2,dttf_sig_WS2,dttf_eta_WS2,dttf_tradd_WS2 #--- WS muon 2
	global dttf_pt_WS3, dttf_phi_WS3,dttf_qual_WS3,dttf_tradd_st1_WS3,dttf_tradd_st2_WS3,dttf_tradd_st3_WS3,dttf_tradd_st4_WS3,dttf_sig_WS3,dttf_eta_WS3,dttf_tradd_WS3 #--- WS muon 3
	
	#--------------------declare all arrays here :
	pt_ws_array = []
	phi_ws_array = []
	qual_ws_array = []
	eta_ws_array = []
	traddr_ws_array = []
	pt_emu_array = []
	phi_emu_array = []
	qual_emu_array = []
	eta_emu_array = []
	traddr_emu_array = []
	ws_pt_wr = []
	
	global kk
	kk=0
	count = 0

#	----------------------------------- The following code loops 100 times. Once for every event -----------------------------------
	for event in events:
		tevent    = event.xpath("./info[@type='event' ]/tree_event")[0].text
		muon      = event.xpath("./info[@type='event' ]/muon")[0].text
		wm2_sl_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='left']/Segment[@id='high']")[0]  # 0
		wm2_sl_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='left']/Segment[@id='low']")[0]   # 1
		wm2_so_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='own']/Segment[@id='high']")[0]   # 2
		wm2_so_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='own']/Segment[@id='low']")[0]    # 3
		wm2_sr_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='right']/Segment[@id='high']")[0] # 4
		wm2_sr_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='right']/Segment[@id='low']")[0]  # 5
		wm1_sl_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='left']/Segment[@id='high']")[0]  # 6
		wm1_sl_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='left']/Segment[@id='low']")[0]   # 7
		wm1_so_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='own']/Segment[@id='high']")[0]   # 8
		wm1_so_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='own']/Segment[@id='low']")[0]    # 9
		wm1_sr_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='right']/Segment[@id='high']")[0] # 10
		wm1_sr_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='right']/Segment[@id='low']")[0]  # 11
		wh0_sl_sh = event.xpath("./Wheel[@id='0']/Sector[@id='left']/Segment[@id='high']")[0]   # 12
		wh0_sl_sl = event.xpath("./Wheel[@id='0']/Sector[@id='left']/Segment[@id='low']")[0]    # 13
		wh0_so_sh = event.xpath("./Wheel[@id='0']/Sector[@id='own']/Segment[@id='high']")[0]    # 14
		wh0_so_sl = event.xpath("./Wheel[@id='0']/Sector[@id='own']/Segment[@id='low']")[0]     # 15
		wh0_sr_sh = event.xpath("./Wheel[@id='0']/Sector[@id='right']/Segment[@id='high']")[0]  # 16
		wh0_sr_sl = event.xpath("./Wheel[@id='0']/Sector[@id='right']/Segment[@id='low']")[0]   # 17
		wp1_sl_sh = event.xpath("./Wheel[@id='1']/Sector[@id='left']/Segment[@id='high']")[0]   # 18
		wp1_sl_sl = event.xpath("./Wheel[@id='1']/Sector[@id='left']/Segment[@id='low']")[0]    # 19
		wp1_so_sh = event.xpath("./Wheel[@id='1']/Sector[@id='own']/Segment[@id='high']")[0]    # 20
		wp1_so_sl = event.xpath("./Wheel[@id='1']/Sector[@id='own']/Segment[@id='low']")[0]     # 21
		wp1_sr_sh = event.xpath("./Wheel[@id='1']/Sector[@id='right']/Segment[@id='high']")[0]  # 22
		wp1_sr_sl = event.xpath("./Wheel[@id='1']/Sector[@id='right']/Segment[@id='low']")[0]   # 23
		wp2_sl_sh = event.xpath("./Wheel[@id='2']/Sector[@id='left']/Segment[@id='high']")[0]   # 24
		wp2_sl_sl = event.xpath("./Wheel[@id='2']/Sector[@id='left']/Segment[@id='low']")[0]    # 25
		wp2_so_sh = event.xpath("./Wheel[@id='2']/Sector[@id='own']/Segment[@id='high']")[0]    # 26
		wp2_so_sl = event.xpath("./Wheel[@id='2']/Sector[@id='own']/Segment[@id='low']")[0]     # 27
		wp2_sr_sh = event.xpath("./Wheel[@id='2']/Sector[@id='right']/Segment[@id='high']")[0]  # 28
		wp2_sr_sl = event.xpath("./Wheel[@id='2']/Sector[@id='right']/Segment[@id='low']")[0]   # 29
		events_list =  [wm2_sl_sl,wm2_sl_sh,wm2_sr_sl,wm2_sr_sh,wm2_so_sl,wm2_so_sh,\
				wm1_sl_sl,wm1_sl_sh,wm1_sr_sl,wm1_sr_sh,wm1_so_sl,wm1_so_sh,\
				wh0_sl_sl,wh0_sl_sh,wh0_sr_sl,wh0_sr_sh,wh0_so_sl,wh0_so_sh,\
				wp1_so_sl,wp1_so_sh,wp1_sl_sl,wp1_sl_sh,wp1_sr_sl,wp1_sr_sh,\
				wp2_so_sl,wp2_so_sh,wp2_sl_sl,wp2_sl_sh,wp2_sr_sl,wp2_sr_sh]
		########################
		ll=0
		

		for e_list in events_list: #---------------------This will run 30 times/event ---------------
			############### INPUTS ###############
			ang_st1   = e_list.xpath("./info[@type='ph_emu']/ang_st1")[0].text
			b_ang_st1 = e_list.xpath("./info[@type='ph_emu']/b_ang_st1")[0].text
			code_st1  = e_list.xpath("./info[@type='ph_emu']/code_st1")[0].text
			ang_st2   = e_list.xpath("./info[@type='ph_emu']/ang_st2")[0].text
			b_ang_st2 = e_list.xpath("./info[@type='ph_emu']/b_ang_st2")[0].text
			code_st2  = e_list.xpath("./info[@type='ph_emu']/code_st2")[0].text
			ang_st3   = e_list.xpath("./info[@type='ph_emu']/ang_st3")[0].text
			code_st3  = e_list.xpath("./info[@type='ph_emu']/code_st3")[0].text
			ang_st4   = e_list.xpath("./info[@type='ph_emu']/ang_st4")[0].text
			b_ang_st4 = e_list.xpath("./info[@type='ph_emu']/b_ang_st4")[0].text
			code_st4  = e_list.xpath("./info[@type='ph_emu']/code_st4")[0].text
			hits_st1  = e_list.xpath("./info[@type='th_emu']/hits_st1")[0].text
			hits_st2  = e_list.xpath("./info[@type='th_emu']/hits_st2")[0].text
			hits_st3  = e_list.xpath("./info[@type='th_emu']/hits_st3")[0].text
			############### OUTPUT ###############
			emu_pt         = e_list.xpath("./info[@type='tr_emu']/pt")[0].text
			emu_phi        = e_list.xpath("./info[@type='tr_emu']/phi")[0].text
			emu_qual       = e_list.xpath("./info[@type='tr_emu']/qual")[0].text
			emu_tradd_st1  = e_list.xpath("./info[@type='tr_emu']/tradd_st1")[0].text
			emu_tradd_st2  = e_list.xpath("./info[@type='tr_emu']/tradd_st2")[0].text
			emu_tradd_st3  = e_list.xpath("./info[@type='tr_emu']/tradd_st3")[0].text
			emu_tradd_st4  = e_list.xpath("./info[@type='tr_emu']/tradd_st4")[0].text
			emu_sig        = e_list.xpath("./info[@type='tr_emu']/sig")[0].text # added
			emu_eta        = e_list.xpath("./info[@type='tr_emu']/eta")[0].text # added
			emu_tradd      = emu_tradd_st1 + emu_tradd_st2 + emu_tradd_st3 + emu_tradd_st4
			dttf_pt        = e_list.xpath("./info[@type='DTTF']/pt")[0].text
			dttf_phi       = e_list.xpath("./info[@type='DTTF']/phi")[0].text
			dttf_qual      = e_list.xpath("./info[@type='DTTF']/qual")[0].text
			dttf_tradd_st1 = e_list.xpath("./info[@type='DTTF']/tradd_st1")[0].text
			dttf_tradd_st2 = e_list.xpath("./info[@type='DTTF']/tradd_st2")[0].text
			dttf_tradd_st3 = e_list.xpath("./info[@type='DTTF']/tradd_st3")[0].text
			dttf_tradd_st4 = e_list.xpath("./info[@type='DTTF']/tradd_st4")[0].text
			dttf_sig       = e_list.xpath("./info[@type='DTTF']/sig")[0].text # added
			dttf_eta       = e_list.xpath("./info[@type='DTTF']/eta")[0].text # added
			dttf_tradd 	   = dttf_tradd_st1 + dttf_tradd_st2 + dttf_tradd_st3 + dttf_tradd_st4
			

			# ---------------------------------- Read only the WS muon 1 outputs ----------------------------#
			if(e_list == wm1_so_sl):
				dttf_pt_WS        = e_list.xpath("./info[@type='DTTF']/pt")[0].text
				dttf_phi_WS       = e_list.xpath("./info[@type='DTTF']/phi")[0].text
				dttf_qual_WS      = e_list.xpath("./info[@type='DTTF']/qual")[0].text
				dttf_tradd_st1_WS = e_list.xpath("./info[@type='DTTF']/tradd_st1")[0].text
				dttf_tradd_st2_WS = e_list.xpath("./info[@type='DTTF']/tradd_st2")[0].text
				dttf_tradd_st3_WS = e_list.xpath("./info[@type='DTTF']/tradd_st3")[0].text
				dttf_tradd_st4_WS = e_list.xpath("./info[@type='DTTF']/tradd_st4")[0].text
				dttf_sig_WS       = e_list.xpath("./info[@type='DTTF']/sig")[0].text # added
				dttf_eta_WS       = e_list.xpath("./info[@type='DTTF']/eta")[0].text # added
				dttf_tradd_WS 	  = dttf_tradd_st1_WS + dttf_tradd_st2_WS + dttf_tradd_st3_WS + dttf_tradd_st4_WS
				
				pt_ws_array.append(dttf_pt_WS) #--------- load the WS Pt values
				phi_ws_array.append(dttf_phi_WS) #------- load the WS Phi values
				qual_ws_array.append(dttf_qual_WS) #----- load the WS Quality values
				eta_ws_array.append(dttf_eta_WS) #------- load the WS Eta values
				traddr_ws_array.append(dttf_tradd_WS) #-- load the WS Track Addr values
				
				file_WS_Outputs.write(15*"-"+"\n")
				file_WS_Outputs.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n") #----------added
				if (ws_pt_wr == 1):
					filebad_events_pt.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				if (ws_phi_wr == 1):
					filebad_events_phi.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				if (ws_qual_wr == 1):
					filebad_events_qual.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				if (ws_eta_wr == 1):
					filebad_events_eta.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				if (ws_traddr_wr == 1):
					filebad_events_traddr.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
			
			# ---------------------------------- Read only the WS muon 2 outputs ----------------------------#
			if(e_list == wh0_so_sl):
				dttf_pt_WS2        = e_list.xpath("./info[@type='DTTF']/pt")[0].text
				dttf_phi_WS2       = e_list.xpath("./info[@type='DTTF']/phi")[0].text
				dttf_qual_WS2      = e_list.xpath("./info[@type='DTTF']/qual")[0].text
				dttf_tradd_st1_WS2 = e_list.xpath("./info[@type='DTTF']/tradd_st1")[0].text
				dttf_tradd_st2_WS2 = e_list.xpath("./info[@type='DTTF']/tradd_st2")[0].text
				dttf_tradd_st3_WS2 = e_list.xpath("./info[@type='DTTF']/tradd_st3")[0].text
				dttf_tradd_st4_WS2 = e_list.xpath("./info[@type='DTTF']/tradd_st4")[0].text
				dttf_sig_WS2       = e_list.xpath("./info[@type='DTTF']/sig")[0].text # added
				dttf_eta_WS2       = e_list.xpath("./info[@type='DTTF']/eta")[0].text # added
				dttf_tradd_WS2	   = dttf_tradd_st1_WS2 + dttf_tradd_st2_WS2 + dttf_tradd_st3_WS2 + dttf_tradd_st4_WS2
				
				# pt_ws_array.append(dttf_pt_WS) #--------- load the WS Pt values
				# phi_ws_array.append(dttf_phi_WS) #------- load the WS Phi values
				# qual_ws_array.append(dttf_qual_WS) #----- load the WS Quality values
				# eta_ws_array.append(dttf_eta_WS) #------- load the WS Eta values
				# traddr_ws_array.append(dttf_tradd_WS) #-- load the WS Track Addr values
				
				file_WS_Outputs.write("WS2  pt: "+str(dttf_pt_WS2)+"\t"+"phi: "+str(dttf_phi_WS2)+"\t "+"qual: "+str(dttf_qual_WS2)+"\t"+"tradd: "+str(dttf_tradd_WS2)+"\t"+"sig: "+str(dttf_sig_WS2)+"\t\t"+"eta: "+str(dttf_eta_WS2)+"\t\t"+"η: "+str(float(dttf_eta_WS2)*0.0109)+"\t"+"\n") #----------added
				# if (ws_pt_wr == 1):
				# 	filebad_events_pt.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_phi_wr == 1):
				# 	filebad_events_phi.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_qual_wr == 1):
				# 	filebad_events_qual.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_eta_wr == 1):
				# 	filebad_events_eta.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_traddr_wr == 1):
				# 	filebad_events_traddr.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added

			 #---------------------------------- Read only the WS muon 3 outputs ----------------------------#
			if(e_list == wp1_so_sl):
				dttf_pt_WS3        = e_list.xpath("./info[@type='DTTF']/pt")[0].text
				dttf_phi_WS3       = e_list.xpath("./info[@type='DTTF']/phi")[0].text
				dttf_qual_WS3      = e_list.xpath("./info[@type='DTTF']/qual")[0].text
				dttf_tradd_st1_WS3 = e_list.xpath("./info[@type='DTTF']/tradd_st1")[0].text
				dttf_tradd_st2_WS3 = e_list.xpath("./info[@type='DTTF']/tradd_st2")[0].text
				dttf_tradd_st3_WS3 = e_list.xpath("./info[@type='DTTF']/tradd_st3")[0].text
				dttf_tradd_st4_WS3 = e_list.xpath("./info[@type='DTTF']/tradd_st4")[0].text
				dttf_sig_WS3       = e_list.xpath("./info[@type='DTTF']/sig")[0].text # added
				dttf_eta_WS3       = e_list.xpath("./info[@type='DTTF']/eta")[0].text # added
				dttf_tradd_WS3	   = dttf_tradd_st1_WS3 + dttf_tradd_st2_WS3 + dttf_tradd_st3_WS3 + dttf_tradd_st4_WS3
				
				# pt_ws_array.append(dttf_pt_WS) #--------- load the WS Pt values
				# phi_ws_array.append(dttf_phi_WS) #------- load the WS Phi values
				# qual_ws_array.append(dttf_qual_WS) #----- load the WS Quality values
				# eta_ws_array.append(dttf_eta_WS) #------- load the WS Eta values
				# traddr_ws_array.append(dttf_tradd_WS) #-- load the WS Track Addr values
				
				file_WS_Outputs.write("WS3  pt: "+str(dttf_pt_WS3)+"\t"+"phi: "+str(dttf_phi_WS3)+"\t "+"qual: "+str(dttf_qual_WS3)+"\t"+"tradd: "+str(dttf_tradd_WS3)+"\t"+"sig: "+str(dttf_sig_WS3)+"\t\t"+"eta: "+str(dttf_eta_WS3)+"\t\t"+"η: "+str(float(dttf_eta_WS3)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_pt_wr == 1):
				# 	filebad_events_pt.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_phi_wr == 1):
				# 	filebad_events_phi.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_qual_wr == 1):
				# 	filebad_events_qual.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_eta_wr == 1):
				# 	filebad_events_eta.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added
				# if (ws_traddr_wr == 1):
				# 	filebad_events_traddr.write("WS   pt: "+str(dttf_pt_WS)+"\t"+"phi: "+str(dttf_phi_WS)+"\t "+"qual: "+str(dttf_qual_WS)+"\t"+"tradd: "+str(dttf_tradd_WS)+"\t"+"sig: "+str(dttf_sig_WS)+"\t\t"+"eta: "+str(dttf_eta_WS)+"\t\t"+"η: "+str(float(dttf_eta_WS)*0.0109)+"\t"+"\n\n\n") #----------added

			# ------------------------------------------ Read only the EMU/DTTF outputs --------------------------------#
			if(e_list == wm2_so_sl): 
				pt_emu_array.append(emu_pt) #--------- load the EMU PT values
				phi_emu_array.append(emu_phi) #------- load the EMU Phi values
				qual_emu_array.append(emu_qual) #----- load the EMU Quality values
				eta_emu_array.append(emu_eta) #------- load the EMU Eta values
				traddr_emu_array.append(emu_tradd) #-- load the EMU Track Addr values
				ws_pt_wr = ws_phi_wr = ws_qual_wr = ws_eta_wr = ws_traddr_wr = 0 #----- for WS write sync

				#------------------ Fill Histos for TFs -----------------#
				if (dttf_tradd == emu_tradd):
					traddr = 0
				elif (dttf_tradd != emu_tradd):
					traddr = 4
				if float(emu_pt) != 0:
					histo_pt.Fill((float(dttf_pt)-float(emu_pt))/float(emu_pt))
					histo_2d.Fill(float(emu_pt) ,(float(dttf_pt)-float(emu_pt))/float(emu_pt))
					histo_pt_mp7.Fill(float(dttf_pt))
					histo_pt_emu.Fill(float(emu_pt))
				if float(emu_phi) != 0:
					histo_phi.Fill((float(dttf_phi)-float(emu_phi))/float(emu_phi))
					histo_2d_phi.Fill(float(emu_phi) ,(float(dttf_phi)-float(emu_phi)))
				if float(emu_qual) != 0:
					histo_qual.Fill((float(dttf_qual)-float(emu_qual))/float(emu_qual))
				if float(emu_sig) < float(2): 					   # ------------------ added ------
					histo_sig.Fill(float(dttf_sig)-float(emu_sig)) # -------------------------------
				if float(emu_eta) != 0: 						   # ------------------ added ------
					histo_eta.Fill((float(dttf_eta)-float(emu_eta))/float(emu_eta)) # --------------
				histo_traddr.Fill(traddr)
				
				#-------------- Write Bad Event Files -----------------#
				if(float(emu_pt) != float(dttf_pt)) :#----------Pt
					bad_events_pt = bad_events_pt + 1
					write_bad_event(filebad_events_pt)
					ws_pt_wr = 1	

				if(emu_phi != dttf_phi) : #--------------------PHI
					bad_events_phi = bad_events_phi + 1
					write_bad_event(filebad_events_phi)
					ws_phi_wr =1

				if(emu_qual != dttf_qual) :#-------------------Quality
					bad_events_qual = bad_events_qual + 1
					write_bad_event(filebad_events_qual)
					ws_qual_wr = 1

				# if(emu_tradd_st1 != dttf_tradd_st1) :
				# 	bad_events_traddr_1 = bad_events_traddr_1 + 1
				# 	write_bad_event(filebad_events_traddr_1)

				# if(emu_tradd_st2 != dttf_tradd_st2) :
				# 	bad_events_traddr_2 = bad_events_traddr_2 + 1
				# 	write_bad_event(filebad_events_traddr_2)

				# if(emu_tradd_st3 != dttf_tradd_st3) :
				# 	bad_events_traddr_3 = bad_events_traddr_3 + 1
				# 	write_bad_event(filebad_events_traddr_3)

				# if(emu_tradd_st4 != dttf_tradd_st4) :
				# 	bad_events_traddr_4 = bad_events_traddr_4 + 1
				# 	write_bad_event(filebad_events_traddr_4)

				if(emu_tradd != dttf_tradd) :#----------------Track Address
					bad_events_traddr = bad_events_traddr + 1
					write_bad_event(filebad_events_traddr)
					ws_traddr_wr = 1
					
				if(emu_sig != dttf_sig) :
					bad_events_sig = bad_events_sig + 1
					write_bad_event(filebad_events_sig)

				if(float(dttf_eta) != float(emu_eta)) :#------Eta
					bad_events_eta = bad_events_eta + 1
					write_bad_event(filebad_events_eta)
					ws_eta_wr = 1
					
				if((float(emu_pt) != float(dttf_pt)) or (emu_phi != dttf_phi) or (emu_qual != dttf_qual) or (emu_tradd != dttf_tradd) or (emu_sig != dttf_sig) or (emu_eta != dttf_eta)) :
					bad_events = bad_events + 1
					# print 15*"+","Event #%s" %kk,15*"+"
					# print("MP7: pt, phi, qual, tradd, sig, eta: %s, \t%s,\t%s,\t%s, \t%s,\t%s" %(wm2_so_sl.xpath("./info[@type='DTTF']/pt")[0].text,wm2_so_sl.xpath("./info[@type='DTTF']/phi")[0].text,wm2_so_sl.xpath("./info[@type='DTTF']/qual")[0].text,wm2_so_sl.xpath("./info[@type='DTTF']/tradd_st1")[0].text+wm2_so_sl.xpath("./info[@type='DTTF']/tradd_st2")[0].text+wm2_so_sl.xpath("./info[@type='DTTF']/tradd_st3")[0].text+wm2_so_sl.xpath("./info[@type='DTTF']/tradd_st4")[0].text, wm2_so_sl.xpath("./info[@type='DTTF']/sig")[0].text, wm2_so_sl.xpath("./info[@type='DTTF']/eta")[0].text)) # added
					# print

				file_WS_Outputs.write(15*"+"+" ID: "+str(kk)+" "+15*"+"+"\n") 
				file_WS_Outputs.write("EMU  pt: "+str(emu_pt)+"\t"+"phi: "+str(emu_phi)+"\t "+"qual: "+str(emu_qual)+"\t"+"tradd: "+str(emu_tradd)+"\t"+"sig: "+str(emu_sig)+"\t\t"+"eta: "+str(emu_eta)+"\t\t"+"η: "+str(float(emu_eta)*0.0109)+"\n") #------------------added
				#file_WS_Outputs.write("MP7  pt: "+str(dttf_pt)+"\t"+"phi: "+str(dttf_phi)+"\t "+"qual: "+str(dttf_qual)+"\t"+"tradd: "+str(dttf_tradd)+"\t"+"sig: "+str(dttf_sig)+"\t\t"+"eta: "+str(dttf_eta)+"\t\t"+"η: "+str(float(dttf_eta)*0.0109)+"\t"+"\n") #----------added
			

		keepGoing = dialog.Update(kk)
		kk = kk + 1
#	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Here ENDS the 100 loop that runs through the 100 events^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




#############------------------------------------- Fill Histographs for WS ----------------------------------###################

	for aa in range(0,len(pt_ws_array)) :
		if float(pt_emu_array[aa]) != 0:
			histo_WS_pt.Fill((float(pt_ws_array[aa])-float(pt_emu_array[aa]))/float(pt_emu_array[aa]))
			histo_2d.Fill(float(pt_emu_array[aa]) ,(float(pt_ws_array[aa])-float(pt_emu_array[aa]))/float(pt_emu_array[aa]))
			histo_pt_mp7.Fill(float(pt_ws_array[aa]))
			histo_pt_emu.Fill(float(pt_emu_array[aa]))

	for bb in range(0,len(phi_ws_array)) :
		if float(phi_emu_array[bb]) != 0:
			histo_WS_phi.Fill((float(phi_ws_array[bb])-float(phi_emu_array[bb]))/float(phi_emu_array[bb]))
			histo_2d.Fill(float(phi_emu_array[bb]) ,(float(phi_ws_array[bb])-float(phi_emu_array[bb]))/float(phi_emu_array[bb]))

 	for cc in range(0,len(qual_ws_array)) :
 		if float(qual_emu_array[cc]) != 0:
			histo_WS_qual.Fill((float(qual_ws_array[cc])-float(qual_emu_array[cc]))/float(qual_emu_array[cc]))

	for dd in range(0,len(qual_ws_array)) :
		if float(eta_emu_array[dd]) != 0: #-------------------------------------------------added------
			histo_WS_eta.Fill((float(eta_ws_array[dd])-float(eta_emu_array[dd]))/float(eta_emu_array[dd])) #----------------

	for ee in range(0,len(traddr_ws_array)) :
		if (traddr_ws_array[ee] == traddr_emu_array[ee]):
			ws_traddr = 0
		else:
			ws_traddr = 4	
		histo_WS_traddr.Fill(ws_traddr)
	
	for ff in range(0,len(eta_ws_array)) :
		histo_WS_eta_distr.Fill(float(eta_ws_array[ff])) #----------------

	for wa in range(0,len(pt_ws_array)):
		if float(pt_emu_array[wa]) != float(pt_ws_array[wa]):
			print "ID :    " + str(wa)
			print "EMU Pt :" + str(pt_emu_array[wa])
			print "WS Pt : " + str(pt_ws_array[wa])


#############------------------------------------- END Fill Histographs for WS ---------------------------###################
			

 #------------------------------------------------ Write total bad events to every file ------------------------

	print "Total bad_events: "+str(bad_events)
	filebad_events_pt.write("Total pT bad_events: "+str(bad_events_pt)+"\n\n")
	filebad_events_phi.write("Total phi bad_events: "+str(bad_events_phi)+"\n\n")
	filebad_events_qual.write("Total qual bad_events: "+str(bad_events_qual)+"\n\n")
	filebad_events_traddr.write("Total traddr bad_events: "+str(bad_events_traddr)+"\n\n")
	filebad_events_traddr_1.write("Total traddr_st1 bad_events: "+str(bad_events_traddr_1)+"\n\n")
	filebad_events_traddr_2.write("Total traddr_st2 bad_events: "+str(bad_events_traddr_2)+"\n\n")
	filebad_events_traddr_3.write("Total traddr_st3 bad_events: "+str(bad_events_traddr_3)+"\n\n")
	filebad_events_traddr_4.write("Total traddr_st4 bad_events: "+str(bad_events_traddr_4)+"\n\n")
	filebad_events_sig.write("Total sign bad_events: "+str(bad_events_sig)+"\n\n") # added
	filebad_events_eta.write("Total eta bad_events: "+str(bad_events_eta)+"\n\n") # added


#==================================================================== END read_xml() function ============================================================================



#============= MAIN CODE ==============
read_xml()
dialog.Destroy()

print
filebad_events_pt.close()
filebad_events_phi.close()
filebad_events_qual.close()
filebad_events_traddr.close()
filebad_events_traddr_1.close()
filebad_events_traddr_2.close()
filebad_events_traddr_3.close()
filebad_events_traddr_4.close()
filebad_events_sig.close()
filebad_events_eta.close()
file_WS_Outputs.close()


print("file phtftests/report/bad_events_pt.txt has been created")
print("file phtftests/report/bad_events_phi.txt has been created")
print("file phtftests/report/bad_events_qual.txt has been created")
print("file phtftests/report/bad_events_traddr.txt has been created")
print("file phtftests/report/bad_events_traddr_st1.txt has been created")
print("file phtftests/report/bad_events_traddr_st2.txt has been created")
print("file phtftests/report/bad_events_traddr_st3.txt has been created")
print("file phtftests/report/bad_events_traddr_st4.txt has been created")
print("file phtftests/report/bad_events_sig.txt has been created") # -- added
print("file phtftests/report/bad_events_eta.txt has been created")# --- added
print("file phtftests/report/Wedge_Sorter_Outputs.txt has been created")# --- added for WS



# ------------------ Draw Histogram Plots ----------------------------
c1 = TCanvas( 'c1', 'Resolution', 200, 10, 700, 500 )
c1.SetBottomMargin(0.23)
c1.SetGridy()
c1.SetLogy()
histo_pt.GetXaxis().SetTitle("#frac{p_{T}(MP7) - p_{T}(EMU)}{p_{T}(EMU)}")
histo_pt.GetXaxis().SetTitleOffset(1.6)
histo_pt.GetYaxis().SetTitle("Events")
histo_pt.SetTitle("p_{T} validation")
histo_pt.Draw()
c1.Update()
c1.SaveAs("phtftests/report/histo_pt.png")
c1.SaveAs("phtftests/report/histo_pt.root")
##
histo_2d.SaveAs("phtftests/report/histo_2d.root")
histo_pt_mp7.SaveAs("phtftests/report/histo_pt_mp7.root")
histo_pt_emu.SaveAs("phtftests/report/histo_pt_emu.root")
############
d1 = TCanvas( 'd1', 'Resolution', 200, 10, 700, 500 )
d1.SetBottomMargin(0.23)
d1.SetGridy()
d1.SetLogy()
histo_phi.GetXaxis().SetTitle("#frac{Phi(MP7) - Phi(EMU)}{Phi(EMU)}")
histo_phi.GetXaxis().SetTitleOffset(1.6)
histo_phi.GetYaxis().SetTitle("Events")
histo_phi.SetTitle("Phi angle validation")
histo_phi.Draw()
d1.Update()
d1.SaveAs("phtftests/report/histo_phi.png")
d1.SaveAs("phtftests/report/histo_phi.root")
##
histo_2d_phi.SaveAs("phtftests/report/histo_2d_phi.root")
############
e1 = TCanvas( 'e1', 'Resolution', 200, 10, 700, 500 )
e1.SetBottomMargin(0.23)
e1.SetGridy()
e1.SetLogy()
histo_qual.GetXaxis().SetTitle("#frac{Qual(MP7) - Qual(EMU)}{Qual(EMU)}")
histo_qual.GetXaxis().SetTitleOffset(1.6)
histo_qual.GetYaxis().SetTitle("Events")
histo_qual.SetTitle("Quality bits validation")
histo_qual.Draw()
e1.Update()
e1.SaveAs("phtftests/report/histo_qual.png")
e1.SaveAs("phtftests/report/histo_qual.root")
############
f1 = TCanvas( 'f1', 'Resolution', 200, 10, 700, 500 )
f1.SetBottomMargin(0.23)
f1.SetGridy()
f1.SetLogy()
histo_traddr.GetXaxis().SetTitle("#frac{TrAddr(MP7) - TrAddr(EMU)}{TrAddr(EMU)}")
histo_traddr.GetXaxis().SetTitleOffset(1.6)
histo_traddr.GetYaxis().SetTitle("Events")
histo_traddr.SetTitle("Track address class validation")
histo_traddr.Draw()
f1.Update()
f1.SaveAs("phtftests/report/histo_traddr.png")
f1.SaveAs("phtftests/report/histo_traddr.root")
############ -------------------------------------------------------- addded
g1 = TCanvas( 'g1', 'Resolution', 200, 10, 700, 500 )
g1.SetBottomMargin(0.23)
g1.SetGridy()
g1.SetLogy()
histo_sig.GetXaxis().SetTitle("#frac{sig(MP7) - sig(EMU)}{sig(EMU)}")
histo_sig.GetXaxis().SetTitleOffset(1.6)
histo_sig.GetYaxis().SetTitle("Events")
histo_sig.SetTitle("Sign validation")
histo_sig.Draw()
g1.Update()
g1.SaveAs("phtftests/report/histo_sig.png")
g1.SaveAs("phtftests/report/histo_sig.root")
############ --------------------------------------------------------- added
h1 = TCanvas( 'h1', 'Resolution', 200, 10, 700, 500 )
h1.SetBottomMargin(0.23)
h1.SetGridy()
h1.SetLogy()
histo_eta.GetXaxis().SetTitle("#frac{eta(MP7) - eta(EMU)}{eta(EMU)}")
histo_eta.GetXaxis().SetTitleOffset(1.6)
histo_eta.GetYaxis().SetTitle("Events")
histo_eta.SetTitle("Eta validation")
histo_eta.Draw()
h1.Update()
h1.SaveAs("phtftests/report/histo_eta.png")
h1.SaveAs("phtftests/report/histo_eta.root")
############

############------------ Draw Plots for WS ---------------------###############
wc1 = TCanvas( 'wc1', 'Resolution', 200, 10, 700, 500 ) #----------- WS Pt
wc1.SetBottomMargin(0.23)
wc1.SetGridy()
wc1.SetLogy()
histo_WS_pt.GetXaxis().SetTitle("#frac{p_{T}(MP7_WS) - p_{T}(EMU)}{p_{T}(EMU)}")
histo_WS_pt.GetXaxis().SetTitleOffset(1.6)
histo_WS_pt.GetYaxis().SetTitle("Events")
histo_WS_pt.SetTitle("p_{T} validation")
histo_WS_pt.Draw()
wc1.Update()
wc1.SaveAs("phtftests/report/histo_WS_pt.png")
wc1.SaveAs("phtftests/report/histo_WS_pt.root")
##################
wd1 = TCanvas( 'wd1', 'Resolution', 200, 10, 700, 500 ) #----------- WS Phi
wd1.SetBottomMargin(0.23)
wd1.SetGridy()
wd1.SetLogy()
histo_WS_phi.GetXaxis().SetTitle("#frac{Phi(MP7_WS) - Phi(EMU)}{Phi(EMU)}")
histo_WS_phi.GetXaxis().SetTitleOffset(1.6)
histo_WS_phi.GetYaxis().SetTitle("Events")
histo_WS_phi.SetTitle("Phi angle validation")
histo_WS_phi.Draw()
wd1.Update()
wd1.SaveAs("phtftests/report/histo_WS_phi.png")
wd1.SaveAs("phtftests/report/histo_WS_phi.root")
###
histo_2d_phi.SaveAs("phtftests/report/histo_WS_2d_phi.root")
################
we1 = TCanvas( 'we1', 'Resolution', 200, 10, 700, 500 ) #----------- WS Quality
we1.SetBottomMargin(0.23)
we1.SetGridy()
we1.SetLogy()
histo_WS_qual.GetXaxis().SetTitle("#frac{Qual(MP7_WS) - Qual(EMU)}{Qual(EMU)}")
histo_WS_qual.GetXaxis().SetTitleOffset(1.6)
histo_WS_qual.GetYaxis().SetTitle("Events")
histo_WS_qual.SetTitle("Quality bits validation")
histo_WS_qual.Draw()
we1.Update()
we1.SaveAs("phtftests/report/histo_ws_qual.png")
we1.SaveAs("phtftests/report/histo_ws_qual.root")
############ -------------------------------------------- added
wh1 = TCanvas( 'wh1', 'Resolution', 200, 10, 700, 500 )  #----------- WS Eta
wh1.SetBottomMargin(0.23)
wh1.SetGridy()
wh1.SetLogy()
histo_WS_eta.GetXaxis().SetTitle("#frac{eta(MP7_WS) - eta(EMU)}{eta(EMU)}")
histo_WS_eta.GetXaxis().SetTitleOffset(1.6)
histo_WS_eta.GetYaxis().SetTitle("Events")
histo_WS_eta.SetTitle("Eta validation")
histo_WS_eta.Draw()
wh1.Update()
wh1.SaveAs("phtftests/report/histo_WS_eta.png")
wh1.SaveAs("phtftests/report/histo_WS_eta.root")
############
wf1 = TCanvas( 'wf1', 'Resolution', 200, 10, 700, 500 ) #----------- WS Track address
wf1.SetBottomMargin(0.23)
wf1.SetGridy()
wf1.SetLogy()
histo_WS_traddr.GetXaxis().SetTitle("#frac{TrAddr(MP7_WS) - TrAddr(EMU)}{TrAddr(EMU)}")
histo_WS_traddr.GetXaxis().SetTitleOffset(1.6)
histo_WS_traddr.GetYaxis().SetTitle("Events")
histo_WS_traddr.SetTitle("Track address class validation")
histo_WS_traddr.Draw()
wf1.Update()
wf1.SaveAs("phtftests/report/histo_WS_traddr.png")
wf1.SaveAs("phtftests/report/histo_WS_traddr.root")

wg1 = TCanvas( 'wf1', 'Resolution', 200, 10, 700, 500 )  #----------- WS Eta distribution
wg1.SetBottomMargin(0.23)
wg1.SetGridy()
wg1.SetLogy()
histo_WS_eta_distr.GetXaxis().SetTitle("#Eta Values")
histo_WS_eta_distr.GetXaxis().SetTitleOffset(1.6)
histo_WS_eta_distr.GetYaxis().SetTitle("Events")
histo_WS_eta_distr.SetTitle("Eta distribution)")
histo_WS_eta_distr.Draw()
wg1.Update()
wg1.SaveAs("phtftests/report/histo_WS_eta_distr.png")
wg1.SaveAs("phtftests/report/histo_WS_eta_distr.root")


# raw_input("Press any key to exit.")
