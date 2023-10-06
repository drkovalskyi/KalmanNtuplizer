#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import os
#from libs.termcolor import colored
from libs.rw_ntuple import *
import libs.VF
from libs.Write_txt import *
from libs import xml_writer
from ROOT import *

fileName="/afs/cern.ch/work/g/gflouris/TriggerUpgrade/Development/BMTF/Emulator_Unpacker/CMSSW_8_0_7/src/KalmanNtuplizer/TrUpS/test/Ntuple_l1tbmtf_mc_etam08p08_pt115120_etahitsrev.root"
name_of_xml="./output_xml/test_mc.xml"


infile=TFile(fileName)

newfile = TFile("new_file.root","RECREATE")

# Make a tree for the emulator
out_tree_emu = TTree('Emulator','Emulator')
VF.Create_Emulator_Branches(out_tree_emu)

# Make a tree for the mp7
out_tree_mp7 = TTree('MP7','MP7')
VF.Create_MP7_Branches(out_tree_mp7)


#new_muon_file("output_muon_80.txt")
VF.txt_output = False
comments = " -- Sim file produced from Tree_from_RAW_20kevents_new_LUTs_100GeV_phi0275.root\n -- 5 hundred events \n "
if ( VF.txt_output ) :
    VF.fileHadlr.write_file("mu_sim_100GeV_phi0275_500events_2_Apr.DAT", comments)

#hundred_events=10

#for i in range(0,hundred_events):
#	min_i = (i * 100)
#	max_i = ((i+1) * 100-1)

xml_writer.output_file =  open(name_of_xml, 'w') 
rw_ntuple( 0, 1000, infile, out_tree_emu, out_tree_mp7 )
xml_writer.output_file.write(xml_writer.etree.tostring(xml_writer.doc, pretty_print = True))
xml_writer.output_file.close()
#	xml_writer.output_file.close()
#	os.system('cat testbench/report_file/phtf_output.txt >> testbench/report_file/trad_output.txt')
#	print colored(45*"=", 'red')
#	print colored("--> %d/%d events testing completed <--" %((i+1)*100,hundred_events*100), 'red')
#	print colored(45*"=", 'red')

#xml_writer.name_of_xml = "out1.xml"
#events=20
#rw_ntuple( 0, events, infile, out_tree_emu, out_tree_mp7 )

newfile.Write("", TObject.kOverwrite)
newfile.Close()  
