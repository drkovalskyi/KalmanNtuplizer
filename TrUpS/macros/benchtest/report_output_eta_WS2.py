#!/usr/bin/python

#---------------- Stavros Mallios ---------------------
#15/02/2016 : 1. We can read the WS outout now      ---
#                                                   ---
#17/02/2016 : 1. Choose witch muon to read by 		---
#				 comment/uncomment lines 265-291  	---
#------------------------------------------------------

import string
from bitstring import Bits

#def bits(number, size_in_bits):
#	"""
#	The bin() function is *REALLY* unhelpful when working with negative numbers.
#	It outputs the binary representation of the positive version of that number
#	with a '-' at the beginning. Woop-di-do. Here's how to derive the two's-
#	complement binary of a negative number:
#		complement(bin(+n - 1))
#	`complement` is a function that flips each bit. `+n` is the negative number
#	made positive.
#	"""
#	if number < 0:
#		return compliment(bin(abs(number) - 1)[2:]).rjust(size_in_bits, '1')
#	else:
#		return bin(number)[2:].rjust(size_in_bits, '0')

def bmtf_output():
	txfile = open('phtftests/temp/tx_summary.txt','r');tx_string=txfile.readlines();txfile.close()
	frames=[];muon_1=[];muon_2=[];trac_d=[];eta_n2=[];muon_1_val=[];muon_2_val=[];eta_n2_val=[];d=[];e=[]
	m_2_qu_list=[];m_2_pt_list=[];m_2_ph_list=[];m_1_qu_list=[];m_1_pt_list=[];m_1_ph_list=[]
	e_n2_sig2_list=[];e_n2_val2_list=[];e_n2_sig1_list=[];e_n2_val1_list=[];tr_addr_1=[];tr_addr_2=[]
	Pt_dttf_up=[];phi_dttf_up=[];qual_dttf_up=[];addr_dttf_up=[];ettf_val=[];ettf_sig=[]

	#----------------------------------------------for WS---------------------------------------------------------------------
	muon_1_ws=[];traddr_1_ws=[];muon_2_ws=[];traddr_2_ws=[];muon_3_ws=[];traddr_3_ws=[];
	muon_1_ws_val=[];traddr_1_ws_list=[];m_1_ph_ws_list=[];m_1_fine_bit_ws_list=[];m_1_eta_ws_list=[];m_1_qu_ws_list=[];m_1_pt_ws_list=[]
	muon_2_ws_val=[];traddr_2_ws_list=[];m_2_ph_ws_list=[];m_2_fine_bit_ws_list=[];m_2_eta_ws_list=[];m_2_qu_ws_list=[];m_2_pt_ws_list=[]
	muon_3_ws_val=[];traddr_3_ws_list=[];m_3_ph_ws_list=[];m_3_fine_bit_ws_list=[];m_3_eta_ws_list=[];m_3_qu_ws_list=[];m_3_pt_ws_list=[]
	addr_dttf_up_ws =[];phi_dttf_up_ws =[];qual_dttf_up_ws= [];ettf_val_ws =[];ettf_sig_ws =[];Pt_dttf_up_ws =[];ettf_fineb_ws  = [] # ---- WS muon 1 outputs
	addr_dttf_up_ws2=[];phi_dttf_up_ws2=[];qual_dttf_up_ws2=[];ettf_val_ws2=[];ettf_sig_ws2=[];Pt_dttf_up_ws2=[];ettf_fineb_ws2 = [] # ---- WS muon 2 outputs
	addr_dttf_up_ws3=[];phi_dttf_up_ws3=[];qual_dttf_up_ws3=[];ettf_val_ws3=[];ettf_sig_ws3=[];Pt_dttf_up_ws3=[];ettf_fineb_ws3 = [] # ---- WS muon 3 outputs
	#-------------------------------------------------------------------------------------------------------------------------
	# 
###################################------------CONVERT Pt, Phi, q, Traddr, Eta VALUES TO INTEGERS-------------------#######################
	def inver(nums):
		fstr="f"
		for i in range(0, len(nums)):
			if nums[i] == '1':
				s=str(0)
				fstr += s
			else:
				s=str(1) 
				fstr += s
		return fstr[1:]

	def val_Pt( inbin ):
#		ibin = inver(inbin)
		ibin = inbin
		tmp = int(ibin,2)*0.5
		return str(tmp);

	def val_Phi( inbin ):
#		ibin = inver(inbin)
		ibin = inbin
		tmp = Bits(bin=ibin)
		tmp_n = tmp
		outPhi=tmp_n.int
		return str(outPhi)#;*((2*math.pi)/576));

	def val_Qul( inbin ):
#		ibin = inver(inbin)
		ibin = inbin
		if   ibin[1:] == "111": outQul = "7" #"   T1234   " #"Null_Track"
		elif ibin[1:] == "110": outQul = "6" #"T123_T124  " #"T34"
		elif ibin[1:] == "101": outQul = "5" #"   T134    " #"T23_T24"
		elif ibin[1:] == "100": outQul = "4" #"   T234    " #"T12_T13_T14"
		elif ibin[1:] == "011": outQul = "3" #"T12_T13_T14" #"T234"
		elif ibin[1:] == "010": outQul = "2" #" T23_T24   " #"T134"
		elif ibin[1:] == "001": outQul = "1" #"   T34     " #"T123_T124"
		elif ibin[1:] == "000": outQul = "0" #"Null_Track " #"T1234"
		else                   : outQul = "  eRRoR    "
		return outQul;

	def val_Et( inbin ):
#		ibin = inver(inbin)
		ibin = inbin
		tmp = Bits(bin=ibin)
		tmp_n = tmp
		outEta=tmp_n.int
		return str(outEta)#;*((2*math.pi)/576));

###################################-------------------------------------------------------------------------#######################


###############################----------- GETTING INFO FROM TX_SUMMARY ----------------###############################
###############################--------------- CHOOSE WHEEL TO READ  --------------------###############################

	for string in tx_string:
		frames.append(string),
	frames.pop(0);frames.pop(0);frames.pop(0)
	#print frames
	num = -1
	for frame in frames:
		# muon_1.append(frame[15+11* 0:12+11*1 ])#;	prints muon_1--------------------
		# muon_2.append(frame[15+11* 6:12+11*7 ])#;	prints muon_2-------------------- for n2
		# trac_d.append(frame[15+11*12:12+11*13])#;	prints track_add-----------------
		# eta_n2.append(frame[15+11*18:12+11*19])#;	prints eta_n2--------------------
		# # muon_1.append(frame[15+11* 1:12+11*2 ])#;	prints muon_1 -------------------
		# muon_2.append(frame[15+11* 7:12+11*8 ])#;	prints muon_2-------------------- for n1
		# trac_d.append(frame[15+11*13:12+11*14])#;	prints track_add-----------------
		# eta_n2.append(frame[15+11*19:12+11*20])#;	prints eta_n2--------------------
		# muon_1.append(frame[15+11* 2:12+11*3 ])#;	prints muon_1 -------------------
		# muon_2.append(frame[15+11* 8:12+11*9 ])#;	prints muon_2-------------------- for n0
		# trac_d.append(frame[15+11*14:12+11*15])#;	prints track_add-----------------
		# eta_n2.append(frame[15+11*20:12+11*21])#;	prints eta_n2--------------------
		# muon_1.append(frame[15+11* 3:12+11*4 ])#;	prints muon_1 -------------------
		# muon_2.append(frame[15+11* 9:12+11*10])#;	prints muon_2-------------------- for p0
		# trac_d.append(frame[15+11*15:12+11*16])#;	prints track_add-----------------
		# eta_n2.append(frame[15+11*21:12+11*22])#;	prints eta_n2--------------------
		muon_1.append(frame[15+11* 4:12+11*5 ])#;	prints muon_1 -------------------
		muon_2.append(frame[15+11*10:12+11*11])#;	prints muon_2-------------------- for p1
		trac_d.append(frame[15+11*16:12+11*17])#;	prints track_add-----------------
		eta_n2.append(frame[15+11*22:12+11*23])#;	prints eta_n2--------------------
		# muon_1.append(frame[15+11* 5:12+11*6 ])#;	prints muon_1 -------------------
		# muon_2.append(frame[15+11*11:12+11*12])#;	prints muon_2-------------------- for p2
		# trac_d.append(frame[15+11*17:12+11*18])#;	prints track_add-----------------
		# eta_n2.append(frame[15+11*23:12+11*24])#;	prints eta_n2--------------------
		
		#-----------------------Wedge Sorter Output (link 61)------------------------#
		if num == -1 :
			num += 1
		elif num%6 == 0 :
			muon_1_ws.append(frame[15+11*61:12+11*62])
			# print muon_1_ws[len(muon_1_ws)-1]
			# print num
			num+=1
		elif num%6 == 1 :
			traddr_1_ws.append(frame[15+11*61:12+11*62])
			# print traddr_2_ws[len(traddr_2_ws)-1]
			# print num
			num+=1
		elif num%6 == 2 :
			muon_2_ws.append(frame[15+11*61:12+11*62])
			# print muon_2_ws[len(muon_2_ws)-1]
			# print num
			num+=1
		elif num%6 == 3 :
			traddr_2_ws.append(frame[15+11*61:12+11*62])
			# print traddr_3_ws[len(traddr_3_ws)-1]
			# print num
			num+=1
		elif num%6 == 4 :
			muon_3_ws.append(frame[15+11*61:12+11*62])
			# print muon_3_ws[len(muon_3_ws)-1]
			# print num
			num+=1
		elif num%6 == 5 :
			traddr_3_ws.append(frame[15+11*61:12+11*62])
			# print traddr_1_ws[len(traddr_1_ws)-1]
			# print num
			num+=1
		else:
			num+=1


###########################------------- Converting to binaries --------------##########################	

# ---------------------------------------------------------------for WS muon 1
	for frame in traddr_1_ws:
		traddr_1_ws_list.append(frame[3:7]) 

	for frame in muon_1_ws:
		muon_1_ws_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))

	for binary in muon_1_ws_val:
		m_1_ph_ws_list.append(binary[1:9])
		m_1_fine_bit_ws_list.append(binary[9])
		m_1_eta_ws_list.append(binary[10:19])  
		m_1_qu_ws_list.append(binary[19:23])   
		m_1_pt_ws_list.append(binary[23:32]) 
# ---------------------------------------------------------------for WS muon 2
	for frame in traddr_2_ws:
		traddr_2_ws_list.append(frame[3:7]) 
		#print len(traddr_2_ws_list)
	for frame in muon_2_ws:
		muon_2_ws_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))

	for binary in muon_2_ws_val:
		m_2_ph_ws_list.append(binary[1:9])
		m_2_fine_bit_ws_list.append(binary[9])
		m_2_eta_ws_list.append(binary[10:19])  
		m_2_qu_ws_list.append(binary[19:23])   
		m_2_pt_ws_list.append(binary[23:32]) 
	
# ---------------------------------------------------------------for WS muon 3
	for frame in traddr_3_ws:
		traddr_3_ws_list.append(frame[3:7]) 

	for frame in muon_3_ws:
		muon_3_ws_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))

	for binary in muon_3_ws_val:
		m_3_ph_ws_list.append(binary[1:9])
		m_3_fine_bit_ws_list.append(binary[9])
		m_3_eta_ws_list.append(binary[10:19])  
		m_3_qu_ws_list.append(binary[19:23])   
		m_3_pt_ws_list.append(binary[23:32]) 
# -------------------------------------------------------------------------
	# print m_1_ph_ws_list
	# print m_1_fine_bit_ws_list
	# print m_1_eta_ws_list
	# print m_1_qu_ws_list
	# print m_1_pt_ws_list
	#print muon_1, muon_2, trac_d, eta_n2
	#
	for frame in muon_1:
		muon_1_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))
	#print muon_1_val
	for frame in muon_2:
		muon_2_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))
	#print muon_2_val
	for frame in eta_n2:
		eta_n2_val.append((bin(int(frame, 16))[2:]).rjust(32, '0'))
	#print eta_n2_val
	for frame in trac_d:
		tr_addr_1.append(frame[4:8])
		tr_addr_2.append(frame[0:4])
	#print tr_addr_1
	#print tr_addr_2
	for binary in muon_1_val:
		m_1_qu_list.append(binary[7:11])   # 31-h  32-l
		m_1_pt_list.append(binary[13:22])  # 31-h  32-l
		m_1_ph_list.append(binary[24:32])  # 31-h  32-l
	for binary in muon_2_val:
		m_2_qu_list.append(binary[7:11])   # 31-h  32-l
		m_2_pt_list.append(binary[13:22])  # 31-h  32-l
		m_2_ph_list.append(binary[24:32])  # 31-h  32-l
	for binary in eta_n2_val:
		e_n2_sig2_list.append(binary[6])      # 31-h  32-l
		e_n2_val2_list.append(binary[7:16])   # 31-h  32-l
		e_n2_sig1_list.append(binary[22])     # 31-h  32-l
		e_n2_val1_list.append(binary[23:32])  # 31-h  32-l

	i=-1
	j=0
	for bina in m_1_qu_list:
		i+=1
#		if ((i%6 == 0) & (i>68) & (i<674)): #100 events
		# if ((i%6 == 0) & (i>86) & (i<692)): #100 events ------------ FOR 40 Mhz ALGO -------------
		if ((i%6 == 0) & (i>54) & (i<660)): #100 events -------------- FOR 80 Mhz ALGO -------------
#		if ((i%6 == 0) & (i>96) & (i<702)): #100 events
		#	print j,"\t",i

			Pt_dttf_up.append(val_Pt(m_1_pt_list[i]))
			# addr_dttf_up.append(tr_addr_1[i-18]) #--- for 40Mhz algo -- 
			addr_dttf_up.append(tr_addr_1[i-9]) #---- for 80Mhz algo -- 
			#print tr_addr_1[i-18],
			phi_dttf_up.append(val_Phi(m_1_ph_list[i]))
			qual_dttf_up.append(val_Qul(m_1_qu_list[i]))
			ettf_val.append(val_Et(e_n2_val1_list[i]))
			ettf_sig.append(e_n2_sig1_list[i])#ettf_sig.append(val_Et(e_n2_sig1_list[i]))
			#print e_n2_val1_list[i], i
			
	#------------------------------------ Wedge Sorter -------------------------------------#
	ni=11
	for binb in traddr_1_ws_list:
	# ------------------------------------------------------------------output WS muon 1			
		Pt_dttf_up_ws.append(val_Pt(m_1_pt_ws_list[ni]))
		# addr_dttf_up.append(tr_addr_1[i-18]) #--- for 40Mhz algo -- 
		addr_dttf_up_ws.append(traddr_1_ws_list[ni]) #---- for 80Mhz algo -- 
		phi_dttf_up_ws.append(val_Phi(m_1_ph_ws_list[ni]))
		qual_dttf_up_ws.append(val_Qul(m_1_qu_ws_list[ni]))
		ettf_val_ws.append(val_Et(m_1_eta_ws_list[ni]))
		ettf_fineb_ws.append(m_1_fine_bit_ws_list[ni])
		#print addr_dttf_up_ws[ni-11], ni
		# # # # --------------------------------------------------------output WS muon 2			
		Pt_dttf_up_ws2.append(val_Pt(m_2_pt_ws_list[ni]))
		#addr_dttf_up2.append(tr_addr_1[i-18]) #--- for 40Mhz algo -- 
		addr_dttf_up_ws2.append(traddr_2_ws_list[ni]) #---- for 80Mhz algo -- 
		phi_dttf_up_ws2.append(val_Phi(m_2_ph_ws_list[ni]))
		qual_dttf_up_ws2.append(val_Qul(m_2_qu_ws_list[ni]))
		ettf_val_ws2.append(val_Et(m_2_eta_ws_list[ni]))
		ettf_fineb_ws2.append(m_2_fine_bit_ws_list[ni])
		# #print addr_dttf_up_ws[ni-11], ni
		# --------------------------------------------------------------output WS muon 3			
		Pt_dttf_up_ws3.append(val_Pt(m_3_pt_ws_list[ni]))
		# addr_dttf_up3.append(tr_addr_1[i-18]) #--- for 40Mhz algo -- 
		addr_dttf_up_ws3.append(traddr_3_ws_list[ni]) #---- for 80Mhz algo -- 
		phi_dttf_up_ws3.append(val_Phi(m_3_ph_ws_list[ni]))
		qual_dttf_up_ws3.append(val_Qul(m_3_qu_ws_list[ni]))
		ettf_val_ws3.append(val_Et(m_3_eta_ws_list[ni]))
		ettf_fineb_ws3.append(m_3_fine_bit_ws_list[ni])
		# # print addr_dttf_up_ws3[ni-11], ni
		ni+=1
		if ni == 111  :
			break
	# print Pt_dttf_up_ws
	# print addr_dttf_up_ws
	# print phi_dttf_up_ws
	# print qual_dttf_up_ws
	# print ettf_val_ws
	# print ettf_fineb_ws
	# print len(ettf_val_ws)



	return Pt_dttf_up,     addr_dttf_up,     phi_dttf_up,     qual_dttf_up,     ettf_val,     ettf_sig,\
		   Pt_dttf_up_ws,  addr_dttf_up_ws,  phi_dttf_up_ws,  qual_dttf_up_ws,  ettf_val_ws,  ettf_fineb_ws,\
		   Pt_dttf_up_ws2, addr_dttf_up_ws2, phi_dttf_up_ws2, qual_dttf_up_ws2, ettf_val_ws2, ettf_fineb_ws2,\
		   Pt_dttf_up_ws3, addr_dttf_up_ws3, phi_dttf_up_ws3, qual_dttf_up_ws3, ettf_val_ws3, ettf_fineb_ws3
 