#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#VF - Variables and Functions
from array import array
from ROOT import *
from Write_txt import *
import os

global passed_events
passed_events = 0

global fileHadlr
fileHadlr = FileOps()

global report_main
report_main = []

global txt_output 
txt_output = False

#DTTF PCK to PT
global  PCKtoPHYS
PCKtoPHYS = (-100, 0.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10., 12., 14., 16., 18., 20., 25., 30., 35., 40., 45., 50., 60., 70., 80., 90., 100., 120., 140.,160.)

#Global Emulator Variables
global emu_pt
emu_pt = vector('float')()
global emu_quality
emu_quality = vector('float')()
global emu_phi
emu_phi = vector('float')()
global emu_tradd
emu_tradd = vector('float')()
#Function for branch creation, for the emu
def Create_Emulator_Branches(out_tree_emu):
	out_tree_emu.Branch('pt',emu_pt)
	out_tree_emu.Branch('quality',emu_quality)
	out_tree_emu.Branch('phi',emu_phi)
	out_tree_emu.Branch('tradd',emu_tradd)

#Global MP7 Variables
global mp7_pt
mp7_pt = vector('float')()
global mp7_quality 
mp7_quality = vector('float')()
global mp7_phi
mp7_phi = vector('float')()
global mp7_tradd
mp7_tradd = vector('float')()
#Function for branch creation, for the mp7
def Create_MP7_Branches(out_tree_emu):
	out_tree_emu.Branch('pt',mp7_pt)
	out_tree_emu.Branch('quality',mp7_quality)
	out_tree_emu.Branch('phi',mp7_phi)
	out_tree_emu.Branch('tradd',mp7_tradd)

#Function that calls clear() for all vectors
def clear_all():
	emu_pt.clear()
	emu_quality.clear()
	emu_phi.clear()
	emu_tradd.clear()
	mp7_pt.clear()
	mp7_quality.clear()
	mp7_phi.clear()
	mp7_tradd.clear()

#Global variables for store_inpattern()
global phi_m1_ts1_tx
global phib_m1_ts1_tx
global q_m1_ts1_tx

global phi_m1_ts2_tx
global phib_m1_ts2_tx
global q_m1_ts2_tx

global phi_m1_ts3_tx
global q_m1_ts3_tx

global phi_m1_ts4_tx
global phib_m1_ts4_tx
global q_m1_ts4_tx

#Function that calls clear() for variables used in store_inpattern()
def Clear_SIPV():
	phi_m1_ts1_tx  = -2048
	phib_m1_ts1_tx = -512
	q_m1_ts1_tx    = 7

	phi_m1_ts2_tx  = -2048
	phib_m1_ts2_tx = -512
	q_m1_ts2_tx    = 7

	phi_m1_ts3_tx  = --2048
	q_m1_ts3_tx    = 7

	phi_m1_ts4_tx  = -2048
	phib_m1_ts4_tx = -512
	q_m1_ts4_tx    = 7

def Check_if_exists(out_file) :
	nr_file = "new"

	if(os.path.exists(out_file)):
		print "File Exist - Do you want to recreate the file? (y/n)"
		yes = set(['yes','y', 'ye', ''])
		no = set(['no','n'])
		choice = raw_input().lower()
		if choice in yes:
			nr_file="recreate"
		elif choice in no:
			#print "Give new name for the output file."
			out_file = raw_input("Give new name for the output file:  ")
			if ( out_file == "new_file.root"):
				print("Doing nothing...bye!")
				exit()
		else:
			sys.stdout.write("Please respond with 'yes' or 'no'")
			return nr_file
