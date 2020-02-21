#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#import ROOT
#from Create_Branches import *
from ROOT import *
import VF
from Write_txt import *
import os
from Global_Dicts_For_XML import *
import xml_writer
	
from itertools import cycle
  
SECTORS = [0,1,2,3,4,5,6,7,8,9,10,11]

fill_bool = False
def rw_ntuple( min_i, max_i, infile, out_tree_emu, out_tree_mp7 ):


	#Read L1Tree
	dir=infile.Get("L1TProducerEmulator")
	read_tree=dir.Get("L1Tree")
	leaves = read_tree.GetListOfLeaves()
	# define dynamically a python class containing root Leaves objects
	class PyListOfLeaves(dict) :
		pass
	# create an istance
	pyl = PyListOfLeaves()
	# add leaves as attributes
	for i in range(0,leaves.GetEntries() ) :
		leaf = leaves.At(i)
		name = leaf.GetName()
		#print name
		# add dynamically attribute to my class 
		pyl.__setattr__(name,leaf)
	#end of read L1Tree

#Read L1Tree
	dir_gen=infile.Get("GENTProducer")
	read_tree_gen=dir_gen.Get("GENTree")
	genleaves = read_tree_gen.GetListOfLeaves()
	# define dynamically a python class containing root Leaves objects
	class PyListOfLeaves_GEN(dict) :
		pass
	# create an istance
	pyl_gen = PyListOfLeaves_GEN()
	# add leaves as attributes
	for i in range(0,genleaves.GetEntries() ) :
		leafgen = genleaves.At(i)
		namegen = leafgen.GetName()
		#print namegen
		# add dynamically attribute to my class 
		pyl_gen.__setattr__(namegen,leafgen)
	#end of read L1Tree

	eta_cut = 0
	no_of_iterations = 0
	#Loop over Tree
	nev = read_tree.GetEntries()
	print "Reading tree with "+str(nev)+" events."
# 	print "From "+str(min_i)+" to "+str(max_i)
#        for iev in range(min_i, max_i) :
	for iev in range(min_i, max_i*2) :
		if((iev % 100) == 0) :	
		  print iev
		fill_bool = False
		read_tree.GetEntry(iev)
		read_tree_gen.GetEntry(iev)
		#print tree.phSize
		VF.clear_all()
		phSize = int(pyl.phSize.GetValue()) 
		# 1 - Check if there are hit at all four stations
		good_m_ph = 0
		for iph in range(0,phSize) :

			phBxRAW = int(pyl.phBxRAW.GetValue(iph))	
			phTs2Tag = int(pyl.phTs2Tag.GetValue(iph))
			phWh = int(pyl.phWh.GetValue(iph))
			phSe = int(pyl.phWh.GetValue(iph))
  
			if ( phBxRAW == 0 and phTs2Tag==0 ):
				good_m_ph += 1

		gen_pt = round(float(pyl_gen.genPt_Mu.GetValue(0)),3)
		gen_eta = round(float(pyl_gen.genEta_Mu.GetValue(0)),3)
		gen_phi = round(float(pyl_gen.genPhi_Mu.GetValue(0)),3)
		

		dict_all['tree_event'] = str(iev)
		dict_all['nmuons'] = "1"

		dict_all['dict_m2_own_low']['gen_pt'] = gen_pt
		dict_all['dict_m2_own_low']['gen_phi'] = gen_phi
		dict_all['dict_m2_own_low']['gen_eta'] = gen_eta

		if ( VF.txt_output == True ) : 
			VF.fileHadlr.write_line("1","","","","","","")
			VF.fileHadlr.write_line("6",iev,gen_pt,gen_eta,gen_phi,"","")   
			VF.fileHadlr.write_line(good_m_ph,"","","","","","")   

		own_sector = 0
		Init_dict_all()
		str_sector = "own"

                trSize = int(pyl.bmtfSize.GetValue())
                if(trSize==0) :
		  continue
                if(trSize!=0) :
                  for itr in range(0,trSize) :

                          trBx = int(pyl.bmtfbx.GetValue(itr))
                         # trTag = int(pyl.t.bmtfTag.GetValue(itr))
                          tr_add_1 = int(pyl.bmtftrAddress.GetValue(0))
                          tr_add_2 = int(pyl.bmtftrAddress.GetValue(1))
                          tr_add_3 = int(pyl.bmtftrAddress.GetValue(2))
                          tr_add_4 = int(pyl.bmtftrAddress.GetValue(3))
                          trWh = int(pyl.bmtfwh.GetValue(itr))
        	          if ( trBx==0 ) :
			  	  own_sector = pyl.bmtfprocessor.GetValue(itr)
                                  break
		#print "Own = "+str(own_sector)
		if(tr_add_1==0 and tr_add_2==0 and tr_add_3==0 and tr_add_4==0):
			continue
		#print iev	
		for iph in range(0,phSize) :
		      
			phBxRAW = int(pyl.phBxRAW.GetValue(iph))
			phTs2Tag = int(pyl.phTs2Tag.GetValue(iph))
			phWh = int(pyl.phWh.GetValue(iph))
			phSe = int(pyl.phSe.GetValue(iph))
			phSt = int(pyl.phSt.GetValue(iph))
			
			phCode = 7
			phBandAng = -512
			phAng = -2048

			phCode = int(pyl.phCode.GetValue(iph))
			phBandAng = int(pyl.phBandAng.GetValue(iph))
			phAng = int(pyl.phAng.GetValue(iph))
	
			str_sector = "own"
			
			if (phSe == own_sector+1):
				 str_sector = "right"
                                 #str_sector = "left"
			elif (phSe == own_sector-1):
				 str_sector = "left"
                                 #str_sector = "right"
			elif (own_sector == 11 and phSe==0):
				str_sector = "right"
                                #str_sector = "left"
  			elif (own_sector == 0 and phSe==11):
				str_sector = "left"
                                #str_sector = "right"
			#if ( phBxRAW == 0 and phTs2Tag==0 and phWh==0 ):
			#if ( iev == 95 or iev == 96) :
			 # print "own = "+str(own_sector)+"   sect = "+str(phSe)+"  phi = "+str(phAng)

			if ( phBxRAW == 0 and phTs2Tag==0 ):                                                    
				fill_bool = True
				if ( phSt != 3 ) :
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['b_ang_st'+str(phSt)] = phBandAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['ang_st'+str(phSt)] = phAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['code_st'+str(phSt)] = phCode
				if ( phSt == 3 ) :
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['ang_st3'] = phAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['code_st3'] = phCode
			if ( phBxRAW == 10 and phTs2Tag==1):                          
				fill_bool = True
				if ( phSt != 3 ) :
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_high']['b_ang_st'+str(phSt)] = phBandAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_high']['ang_st'+str(phSt)] = phAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_high']['code_st'+str(phSt)] = phCode
				if ( phSt == 3 ) :
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_high']['ang_st3'] = phAng
					dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_high']['code_st3'] = phCode
		#	print dict_wheels[phWh]
			if ( VF.txt_output == True and phBxRAW == 0 and phTs2Tag==0 ) : 
				VF.fileHadlr.write_line(phSt, phWh, phSe, phTs2Tag, phCode, phAng, phBandAng)  
                thSize = int(pyl.thSize.GetValue())

	        for thitr in range(0,thSize) :
			  if(int(pyl.thBx.GetValue(thitr))==0):
			      thWh = int(pyl.thWh.GetValue(thitr))
			      thSe = int(pyl.thSe.GetValue(thitr))
			      thSt = int(pyl.thSt.GetValue(thitr))

			      str_sector = "own"

			      if (phSe == own_sector+1):
				 str_sector = "right"
                                 #str_sector = "left"
			      elif (phSe == own_sector-1):
				 str_sector = "left"
                                 #str_sector = "right"
			      elif (own_sector == 11 and phSe==0):
				 str_sector = "right"
                                #str_sector = "left"
			      elif (own_sector == 0 and phSe==11):
				 str_sector = "left"

			      dict_all['dict_'+dict_wheels[thWh]+'_'+str(str_sector)+'_low']['hits_st'+str(thSt)] =  int(pyl.thTheta.GetValue(thitr))
			      dict_all['dict_'+dict_wheels[thWh]+'_'+str(str_sector)+'_high']['hits_st'+str(thSt)] = int(pyl.thCode.GetValue(thitr))
			      #print int(pyl.thTheta.GetValue(thitr))
			      #print str(thSt)

		trSize = int(pyl.bmtfSize.GetValue())
		ptpck = 0
		bx_tr_offset = 0
		tr_add_1 = 3
		tr_add_2 = 15
		tr_add_3 = 15
		tr_add_4 = 15
		phi = "-1"
		eta = "-1"
		qual = "0"
		sig  = "-9"
		count_tr = 0
		if(trSize!=0) :
		  for itr in range(0,trSize) :

			  trBx = int(pyl.bmtfbx.GetValue(itr))
			  trProcessor = int(pyl.bmtfprocessor.GetValue(itr))
			  #trTag = int(pyl.bmtfTag.GetValue(itr))
			  #trPtPck = int(pyl.trPtPck.GetValue(itr))
			  #tr_add_1 = int(pyl.bmtftrAddress.GetValue(0))
			  #tr_add_2 = int(pyl.bmtftrAddress.GetValue(1))
			  #tr_add_3 = int(pyl.bmtftrAddress.GetValue(2))
			  #tr_add_4 = int(pyl.bmtftrAddress.GetValue(3))
			  #trQual = int(pyl.bmtfqual.GetValue(itr))
			  #trSig  = int(pyl.trbmqual.GetValue(itr))
			  #trPhiPck = int(pyl.trPhiPck.GetValue(itr))
			  trWh = int(pyl.bmtfwh.GetValue(itr))
			  if ( trBx==0 and trProcessor==0) :

                                  ptpck =  int(pyl.bmtfPt.GetValue(itr))
                                  VF.emu_pt.push_back(ptpck/2.)

				  qual =  int(pyl.bmtfqual.GetValue(itr))
				  VF.emu_quality.push_back(qual)

				  phi =  int(pyl.bmtfPhi.GetValue(itr))
				  eta =  int(pyl.bmtfEta.GetValue(itr))
				  sig  = int(pyl.bmtfFineBit.GetValue(itr))
				  VF.emu_phi.push_back(phi)
				  count_tr = itr
		                  tr_add_1 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) ) )	
		                  tr_add_2 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +1))
		                  tr_add_3 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +2))
		                  tr_add_4 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +3))

				  #break

  		#  tr_add_1 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) ) )
		#  tr_add_2 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +1))
		#  tr_add_3 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +2))
		#  tr_add_4 = int(pyl.bmtftrAddress.GetValue( 4*(count_tr) +3))

                  dict_all['dict_m2_own_low']['tremu_pt'] = ptpck/2.
                  
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tradd_st1'] = hex(tr_add_1)[2:]
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tradd_st2'] = hex(tr_add_2)[2:]
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tradd_st3'] = hex(tr_add_3)[2:]
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tradd_st4'] = hex(tr_add_4)[2:]
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tremu_phi'] = phi
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tremu_phi'] = eta
		  #dict_all['dict_'+dict_wheels[phWh]+'_'+str(str_sector)+'_low']['tremu_qual'] = qual

		  dict_all['dict_m2_own_low']['tradd_st1'] = hex(tr_add_1)[2:]
		  dict_all['dict_m2_own_low']['tradd_st2'] = hex(tr_add_2)[2:]
		  dict_all['dict_m2_own_low']['tradd_st3'] = hex(tr_add_3)[2:]
		  dict_all['dict_m2_own_low']['tradd_st4'] = hex(tr_add_4)[2:]
		  dict_all['dict_m2_own_low']['tremu_phi'] = phi
		  dict_all['dict_m2_own_low']['tremu_eta'] = eta
		  dict_all['dict_m2_own_low']['tremu_sig'] = sig
		  dict_all['dict_m2_own_low']['tremu_qual'] = qual

			
		xml_writer.write_event(str(no_of_iterations))
                VF.passed_events = VF.passed_events + 1
                no_of_iterations = no_of_iterations + 1

		#xml_writer.write_event(str(iev))
		if( fill_bool == True ):
			out_tree_emu.Fill()
		############################################################################################################
		if ( max_i == no_of_iterations) :
			#print eta_cut			
			return None 
