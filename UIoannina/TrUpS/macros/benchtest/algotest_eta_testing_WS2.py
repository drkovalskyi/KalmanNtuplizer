#!/usr/bin/python
import os
import string
import argparse
from lxml import etree
from termcolor import colored
# from report_output_eta import bmtf_output
# from report_output_eta_WS import bmtf_output
from report_output_eta_WS2 import bmtf_output
#from report_output_80mhz import bmtf_output
#from report_output_160mhz import bmtf_output

parser = argparse.ArgumentParser()
parser.add_argument("-pu", type=str, default='none', help="Choose an event xml from /afs/cern.ch/work/g/gflouris/public/")
parser.add_argument("-pr", type=str, default='none', help="Choose an event xml from ./phtftests/primitives/")
parser.add_argument("-ls", type=str, default='none', help="TYPE y --> available XMLs")
args = parser.parse_args()
if args.ls=='y': os.system('echo ; echo INPUTS_FROM: /afs/cern.ch/work/g/gflouris/public/ ; ls -ltr /afs/cern.ch/work/g/gflouris/public/ | grep .xml ; echo ; echo INPUTS_FROM: ./phtftests/primitives/ ; ls -ltr phtftests/primitives/ ; echo'); quit()
#print 'args.pu:', args.pu
#print 'args.pr:', args.pr

if   args.pr=='none' : tree = etree.parse('/afs/cern.ch/work/g/gflouris/public/'+args.pu)
else                 : tree = etree.parse('phtftests/primitives/'+args.pr)

#tree = etree.parse('/afs/cern.ch/work/g/gflouris/public/'+args.pr)
#tree = etree.parse(args.pr)

#tree = etree.parse('phtftests/primitives/'+args.pr)
events = tree.getroot()
xmlout = open('phtftests/report/xmlout.xml','w')
zeros='00000000'
print colored(" Testing %d events" %(len(events)), 'red')
#os.system('mp7butler.py reset BMTF_XE_180 --clksrc internal')
#os.system('mp7butler.py mgts  BMTF_XE_180 --loopback')

Pt_dttf_output = tr_addr_output = ph_dttf_output = qu_dttf_output = [] #---- TF outputs
Pt_dttf_WS_output  = tr_addr_WS_output  = ph_dttf_WS_output  = qu_dttf_WS_output  = si_ettf_WS_output  = va_ettf_WS_output  =[] #---- WS outputs muon 1
Pt_dttf_WS_output2 = tr_addr_WS_output2 = ph_dttf_WS_output2 = qu_dttf_WS_output2 = si_ettf_WS_output2 = va_ettf_WS_output2 =[] #---- WS outputs muon 2
Pt_dttf_WS_output3 = tr_addr_WS_output3 = ph_dttf_WS_output3 = qu_dttf_WS_output3 = si_ettf_WS_output3 = va_ettf_WS_output3 =[] #---- WS outputs muon 3

hxnb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
global hexline
events_list_names = [30]
#_Wheels____________|_________________________________-2___________________________________|__________________________________-1____________________________________|___________________________________0___________________________________|__________________________________1____________________________________|___________________________________2___________________________________|
#                   |         left         |         right         |          own          |         left          |          right         |          own          |         left          |         right         |           own         |          own          |         left          |         right         |          own          |         left          |         right         |
#                   |   low         high   |    low         high   |    low         high   |   low         high    |     low         high   |    low         high   |    low         high   |    low         high   |    low         high   |     low        high   |    low         high   |    low         high   |    low         high   |    low         high   |    low         high   |
# link:             |     0           1    |      4           5    |      2           3    |     8           9     |      12          13    |     10          11    |     16          17    |     20          21    |     18          19    |      22         23    |     24          25    |     26          27    |     28          29    |     32          33    |     34          35    |
events_list_names = 'wm2_sl_sl','wm2_sl_sh','wm2_sr_sl','wm2_sr_sh','wm2_so_sl','wm2_so_sh','wm1_sl_sl','wm1_sl_sh','wm1_sr_sl','wm1_sr_sh' ,'wm1_so_sl','wm1_so_sh','wh0_sl_sl','wh0_sl_sh','wh0_sr_sl','wh0_sr_sh','wh0_so_sl','wh0_so_sh','wp2_so_sl','wp2_so_sh','wp2_sl_sl','wp2_sl_sh','wp2_sr_sl','wp2_sr_sh','wp2_so_sl','wp2_so_sh','wp2_sl_sl','wp2_sl_sh','wp2_sr_sl','wp2_sr_sh'
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#hundred_events= 1
hundred_events= len(events)/100
hexlist = [[] for i in range(hundred_events*100)]
word1 = []
word2 = []
word3 = []
word4 = []
word5 = []
word6 = []

def hxstr (inbin):
	if inbin == "0000": hexa = "0"
	if inbin == "0001": hexa = "1"
	if inbin == "0010": hexa = "2"
	if inbin == "0011": hexa = "3"
	if inbin == "0100": hexa = "4"
	if inbin == "0101": hexa = "5"
	if inbin == "0110": hexa = "6"
	if inbin == "0111": hexa = "7"
	if inbin == "1000": hexa = "8"
	if inbin == "1001": hexa = "9"
	if inbin == "1010": hexa = "A"
	if inbin == "1011": hexa = "B"
	if inbin == "1100": hexa = "C"
	if inbin == "1101": hexa = "D"
	if inbin == "1110": hexa = "E"
	if inbin == "1111": hexa = "F"
	return hexa

def num_to_12bin (in_num):
	num = in_num & 0xFFF
	num_str = []
	for i in range (0,12):
		num_str.append (str (num % 2))
		num = num / 2
	num_list = [num_str[11], num_str[10], num_str[ 9], num_str[ 8],\
				num_str[ 7], num_str[ 6], num_str[ 5], num_str[ 4],\
				num_str[ 3], num_str[ 2], num_str[ 1], num_str[ 0]]
	num_outstr = string.join (num_list, '')
	return num_outstr

def num_to_10bin (in_num):
	num = in_num & 0x3FF
	num_str = []
	for i in range (0,10):
		num_str.append (str (num % 2))
		num = num / 2
	num_list = [                          num_str[ 9], num_str[ 8],\
				num_str[ 7], num_str[ 6], num_str[ 5], num_str[ 4],\
				num_str[ 3], num_str[ 2], num_str[ 1], num_str[ 0]]
	num_outstr = string.join (num_list, '')
	return num_outstr

# def num_to__7bin (in_num):
# 	num = in_num & 0x7F
# 	num_str = []
# 	for i in range (0,7):
# 		num_str.append (str (num % 2))
# 		num = num / 2
# 	num_list = [             num_str[ 6], num_str[ 5], num_str[ 4],\
# 				num_str[ 3], num_str[ 2], num_str[ 1], num_str[ 0]]
# 	num_outstr = string.join (num_list, '')
# 	return num_outstr

def num_to__4bin (in_num):
	if in_num ==  7: num_outstr = "0111"
	if in_num ==  6: num_outstr = "0110"
	if in_num ==  5: num_outstr = "0101"
	if in_num ==  4: num_outstr = "0100"
	if in_num ==  3: num_outstr = "0011"
	if in_num ==  2: num_outstr = "0010"
	if in_num ==  1: num_outstr = "0001"
	if in_num ==  0: num_outstr = "0000"
	if in_num == -7: num_outstr = "0000"
	return num_outstr

#	num = in_num & 0x7
#	num_str = []
#	for i in range (0,4):
#		num_str.append (str (num % 2))
#		num = num / 2
#	num_list = [ num_str[ 3], num_str[ 2], num_str[ 1], num_str[ 0]]
#	num_outstr = string.join (num_list, '')
#	return num_outstr

def create_mu ():
	global phi_ts1_par, phib_ts1_par, q_ts1_par
	global phi_ts2_par, phib_ts2_par, q_ts2_par
	global phi_ts3_par,               q_ts3_par
	global phi_ts4_par, phib_ts4_par, q_ts4_par

	global hits_st1_par,hits_st2_par, hits_st3_par

	global outline, bin_str, hexline

	twozeros  = "00"
	fivezeros = "00000"
	sixzeros  = "000000"
	tenzeros  = "0000000000"
	elevenzeros = "00000000000"

	phi_ts1_bin  = num_to_12bin( phi_ts1_par  )
	phib_ts1_bin = num_to_10bin( phib_ts1_par )
	q_ts1_bin    = num_to__4bin( q_ts1_par    )

	phi_ts2_bin  = num_to_12bin( phi_ts2_par  )
	phib_ts2_bin = num_to_10bin( phib_ts2_par )
	q_ts2_bin    = num_to__4bin( q_ts2_par    )

	phi_ts3_bin  = num_to_12bin( phi_ts3_par  )
	q_ts3_bin    = num_to__4bin( q_ts3_par    )

	phi_ts4_bin  = num_to_12bin( phi_ts4_par  )
	phib_ts4_bin = num_to_10bin( phib_ts4_par )
	q_ts4_bin    = num_to__4bin( q_ts4_par    )

	hits_st1_bin = hits_st1_par#num_to__7bin( hits_st1_par )
	hits_st2_bin = hits_st2_par#num_to__7bin( hits_st2_par )
	hits_st3_bin = hits_st3_par#num_to__7bin( hits_st3_par )
	#print "hits_st1_bin: %s" %(hits_st1_bin)

	#160 bits in total
	bin_list = [sixzeros,    q_ts4_bin, phib_ts4_bin, phi_ts4_bin,\
				sixzeros,    tenzeros , q_ts3_bin   , phi_ts3_bin,\
				sixzeros,    q_ts2_bin, phib_ts2_bin, phi_ts2_bin,\
				sixzeros,    q_ts1_bin, phib_ts1_bin, phi_ts1_bin,\
				elevenzeros, hits_st3_bin, hits_st2_bin, hits_st1_bin]

	bin_str  = string.join (bin_list, '')

#	print 'PHTF_160b',
#	print bin_str
#################
#	print bin_str[159-159:160-158],
#	print bin_str[159-158:160-156],
#	print bin_str[159-155],
#	print bin_str[159-154],
#	print bin_str[159-153:160-150],
#	print bin_str[159-149:160-140],
#	print bin_str[159-139:160-128], '\t',
#################
#	print bin_str[159-128:160-126],
#	print bin_str[159-125:160-114],
#	print bin_str[159-113],
#	print bin_str[159-112],
#	print bin_str[159-111:160-108],
#	print bin_str[159-107:160- 36], '\t',
#################
#	print bin_str[159- 95:160- 94],
#	print bin_str[159- 93:160- 92],
#	print bin_str[159- 91],
#	print bin_str[159- 90],
#	print bin_str[159- 89:160- 86],
#	print bin_str[159- 85:160- 76],
#	print bin_str[159- 75:160- 64], '\t',
#################
#	print bin_str[159- 63:160- 62],
#	print bin_str[159- 61:160- 60],
#	print bin_str[159- 59],
#	print bin_str[159- 58],
#	print bin_str[159- 57:160- 54],
#	print bin_str[159- 53:160- 44],
#	print bin_str[159- 43:160- 32] '\t',
#################
	#print bin_str[159- 31:160- 21],
	#print bin_str[159- 20:160- 14],
	#print bin_str[159- 13:160-  7],
	#print bin_str[159-  6:160-  0]

	hex_list = ''
	i = int(0)
	for counter in range (0,40):
		first =  4 * i
		last  = (4 * i) + 4
		tmp_bin = bin_str [first:last]
		hex_list += hxstr (tmp_bin)
		i = i + 1
	outline += string.join (hex_list, '')

def store_inpattern (
	ang_st1 = "-2048", b_ang_st1 = "-512", code_st1 = "-7",
	ang_st2 = "-2048", b_ang_st2 = "-512", code_st2 = "-7",
	ang_st3 = "-2048",                     code_st3 = "-7",
	ang_st4 = "-2048", b_ang_st4 = "-512", code_st4 = "-7",
	hits_st1 = "-64"  , hits_st2   = "-64" , hits_st3  = "-64"
):
	global phi_ts1_par , phib_ts1_par, q_ts1_par
	global phi_ts2_par , phib_ts2_par, q_ts2_par
	global phi_ts3_par ,               q_ts3_par
	global phi_ts4_par , phib_ts4_par, q_ts4_par
	global hits_st1_par, hits_st2_par, hits_st3_par

	global outline, bin_str, hexline

	outline = ""

	phi_ts1_par  = int( ang_st1   )
	phib_ts1_par = int( b_ang_st1 )
	q_ts1_par    = int( code_st1  )

	phi_ts2_par  = int( ang_st2   )
	phib_ts2_par = int( b_ang_st2 )
	q_ts2_par    = int( code_st2  )

	phi_ts3_par  = int( ang_st3   )
	q_ts3_par    = int( code_st3  )

	phi_ts4_par  = int( ang_st4   )
	phib_ts4_par = int( b_ang_st4 )
	q_ts4_par    = int( code_st4  )

	hits_st1_par = hits_st1[1:]#int( hits_st1  )
	hits_st2_par = hits_st2[1:]#int( hits_st2  )
	hits_st3_par = hits_st3[1:]#int( hits_st3  )
	#print "hits_st1,2,3: %s %s %s" %(hits_st1, hits_st2, hits_st3)###################################
	#print "hits_st1,2,3_par: %s %s %s" %(hits_st1_par, hits_st2_par, hits_st3_par)###################################

	create_mu()

	hexline = outline
	#print "hexline : ",hexline#######################################
	outline = ""

def frame_str (x):
	if                 (x<10)  : y = '000'+str(x)
	elif ((x>= 10) and (x<100)): y = '00'+str(x)
	else                       : y = '0'+str(x)
	return y

def read_xml_100(n):
	kk=0
	#########################################################################################
	for event in events:
		if ((n-1)*100 <= int(event.get("id")) <= (n*100)-1):
			#print((n-1)*100, int(event.get("id")), (n*100)-1)
			muon      = event.xpath("./info[@type='event' ]/muon")[0].text

			wm2_sl_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='left']/Segment[@id='low']")[0]   # 0
			wm2_sl_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='left']/Segment[@id='high']")[0]  # 1
			wm2_sr_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='right']/Segment[@id='low']")[0]  # 2
			wm2_sr_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='right']/Segment[@id='high']")[0] # 3
			wm2_so_sl = event.xpath("./Wheel[@id='-2']/Sector[@id='own']/Segment[@id='low']")[0]    # 4
			wm2_so_sh = event.xpath("./Wheel[@id='-2']/Sector[@id='own']/Segment[@id='high']")[0]   # 5

			wm1_sl_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='left']/Segment[@id='low']")[0]   # 6
			wm1_sl_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='left']/Segment[@id='high']")[0]  # 7
			wm1_sr_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='right']/Segment[@id='low']")[0]  # 8
			wm1_sr_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='right']/Segment[@id='high']")[0] # 9
			wm1_so_sl = event.xpath("./Wheel[@id='-1']/Sector[@id='own']/Segment[@id='low']")[0]    # 10
			wm1_so_sh = event.xpath("./Wheel[@id='-1']/Sector[@id='own']/Segment[@id='high']")[0]   # 11

			wh0_sl_sl = event.xpath("./Wheel[@id='0']/Sector[@id='left']/Segment[@id='low']")[0]    # 12
			wh0_sl_sh = event.xpath("./Wheel[@id='0']/Sector[@id='left']/Segment[@id='high']")[0]   # 13
			wh0_sr_sl = event.xpath("./Wheel[@id='0']/Sector[@id='right']/Segment[@id='low']")[0]   # 14
			wh0_sr_sh = event.xpath("./Wheel[@id='0']/Sector[@id='right']/Segment[@id='high']")[0]  # 15
			wh0_so_sl = event.xpath("./Wheel[@id='0']/Sector[@id='own']/Segment[@id='low']")[0]     # 16
			wh0_so_sh = event.xpath("./Wheel[@id='0']/Sector[@id='own']/Segment[@id='high']")[0]    # 17

			wp1_sl_sl = event.xpath("./Wheel[@id='1']/Sector[@id='left']/Segment[@id='low']")[0]    # 18
			wp1_sl_sh = event.xpath("./Wheel[@id='1']/Sector[@id='left']/Segment[@id='high']")[0]   # 19
			wp1_sr_sl = event.xpath("./Wheel[@id='1']/Sector[@id='right']/Segment[@id='low']")[0]   # 20
			wp1_sr_sh = event.xpath("./Wheel[@id='1']/Sector[@id='right']/Segment[@id='high']")[0]  # 21
			wp1_so_sl = event.xpath("./Wheel[@id='1']/Sector[@id='own']/Segment[@id='low']")[0]     # 22
			wp1_so_sh = event.xpath("./Wheel[@id='1']/Sector[@id='own']/Segment[@id='high']")[0]    # 23

			wp2_sl_sl = event.xpath("./Wheel[@id='2']/Sector[@id='left']/Segment[@id='low']")[0]    # 24
			wp2_sl_sh = event.xpath("./Wheel[@id='2']/Sector[@id='left']/Segment[@id='high']")[0]   # 25
			wp2_sr_sl = event.xpath("./Wheel[@id='2']/Sector[@id='right']/Segment[@id='low']")[0]   # 26
			wp2_sr_sh = event.xpath("./Wheel[@id='2']/Sector[@id='right']/Segment[@id='high']")[0]  # 27
			wp2_so_sl = event.xpath("./Wheel[@id='2']/Sector[@id='own']/Segment[@id='low']")[0]     # 28
			wp2_so_sh = event.xpath("./Wheel[@id='2']/Sector[@id='own']/Segment[@id='high']")[0]    # 29

			events_list =  [wm2_sl_sl,wm2_sl_sh,wm2_sr_sl,wm2_sr_sh,wm2_so_sl,wm2_so_sh,\
							wm1_sl_sl,wm1_sl_sh,wm1_sr_sl,wm1_sr_sh,wm1_so_sl,wm1_so_sh,\
							wh0_sl_sl,wh0_sl_sh,wh0_sr_sl,wh0_sr_sh,wh0_so_sl,wh0_so_sh,\
							wp1_so_sl,wp1_so_sh,wp1_sl_sl,wp1_sl_sh,wp1_sr_sl,wp1_sr_sh,\
							wp2_so_sl,wp2_so_sh,wp2_sl_sl,wp2_sl_sh,wp2_sr_sl,wp2_sr_sh]
			########################
			ll=0
			for e_list in events_list:
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
			#	print
			#	print((n-1)*100)+kk
			#	print events_list_names[ll]
			#	print 10*"+","Event #%s" %kk,10*"+"
			#	print("Muons per sector:%s\t" %(muon))
			#	print("ST1: ang, b_ang, code : %s,\t%s,\t%s" %(ang_st1,b_ang_st1,code_st1))
			#	print("ST2: ang, b_ang, code : %s,\t%s,\t%s" %(ang_st2,b_ang_st2,code_st2))
			#	print("ST3: ang,      , code : %s,\t\t%s"    %(ang_st3,          code_st3))
			#	print("ST4: ang, b_ang, code : %s,\t%s,\t%s" %(ang_st4,b_ang_st4,code_st4))
				# if ll==7 :
				# 	print e_list
				# 	print("ET1: hits/quality     : %s"           %(hits_st1))
				# 	print("ET2: hits/quality     : %s"           %(hits_st2))
				# 	print("ET3: hits/quality     : %s"           %(hits_st3))
				store_inpattern(ang_st1, b_ang_st1, code_st1,\
								ang_st2, b_ang_st2, code_st2,\
								ang_st3,            code_st3,\
								ang_st4, b_ang_st4, code_st4,\
								hits_st1, hits_st2, hits_st3)
				#print("%2s"%(ll)), hexline
				hexlist[kk].append(hexline)
				ll=ll+1
		kk=kk+1
	return hexlist

def create_muon_patt(hexlist,j):
	# Allocating data to the inputs #
	#print "hexist : ", hexlist[0]
	xx = 0
	patout.write("Board BMTF_XE_180\n");
	patout.write(" Quad/Chan :    q00c0      q00c1      q00c2      q00c3      q01c0      q01c1      q01c2      q01c3      q02c0      q02c1      q02c2      q02c3      q03c0      q03c1      q03c2      q03c3      q04c0      q04c1      q04c2      q04c3      q05c0      q05c1      q05c2      q05c3      q06c0      q06c1      q06c2      q06c3      q07c0      q07c1      q07c2      q07c3      q08c0      q08c1      q08c2      q08c3      q09c0      q09c1      q09c2      q09c3      q10c0      q10c1      q10c2      q10c3      q11c0      q11c1      q11c2      q11c3      q12c0      q12c1      q12c2      q12c3      q13c0      q13c1      q13c2      q13c3      q14c0      q14c1      q14c2      q14c3      q15c0      q15c1      q15c2      q15c3      q16c0      q16c1      q16c2      q16c3      q17c0      q17c1      q17c2      q17c3  \n");
	patout.write("      Link :     00         01         02         03         04         05         06         07         08         09         10         11         12         13         14         15         16         17         18         19         20         21         22         23         24         25         26         27         28         29         30         31         32         33         34         35         36         37         38         39         40         41         42         43         44         45         46         47         48         49         50         51         52         53         54         55         56         57         58         59         60         61         62         63         64         65         66         67         68         69         70         71    \n");
	for yy in range((j-1)*100, (j*100)):    #100 loop
		for jj in range(0, 30): # 30 loop
			#print "event:",yy,"\t","line:",xx,"\t","sector:",jj
			#print hexlist[yy][jj]+'   ','00000000',hexlist[yy][jj][0:8],hexlist[yy][jj][8:16],hexlist[yy][jj][16:24],hexlist[yy][jj][24:32],hexlist[yy][jj][32:40]
			#print
			# word1.append(str(hexlist[yy][jj][32:40]))
			# word2.append(str(hexlist[yy][jj][24:32]))
			# word3.append(str(hexlist[yy][jj][16:24]))
			# word4.append(str(hexlist[yy][jj][8:16]))
			# word5.append(str(hexlist[yy][jj][0:8]))
			# word6.append('00000000')
			word1.append(str(hexlist[yy][jj][24:32]))
			word2.append(str(hexlist[yy][jj][16:24]))
			word3.append(str(hexlist[yy][jj][8:16]))
			word4.append(str(hexlist[yy][jj][0:8]))
			word5.append(str(hexlist[yy][jj][32:40]))
			word6.append('00000000')
		x1 = xx + 0; x2 = xx + 1; x3 = xx + 2; x4 = xx + 3; x5 = xx + 4; x6 = xx + 5
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x1),\
					word1[0] ,word1[1] ,word1[2] ,word1[3] ,word1[4] ,word1[5] ,\
					word1[6] ,word1[7] ,word1[8] ,word1[9] ,word1[10],word1[11] ,\
					word1[12],word1[13],word1[14],word1[15],word1[16],word1[17],\
					word1[18],word1[19],word1[20],word1[21],word1[22],word1[23],\
					word1[24],word1[25],word1[26],word1[27],word1[28],word1[29]));
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x2),\
					word2[0] ,word2[1] ,word2[2] ,word2[3] ,word2[4] ,word2[5] ,\
					word2[6] ,word2[7] ,word2[8] ,word2[9] ,word2[10],word2[11] ,\
					word2[12],word2[13],word2[14],word2[15],word2[16],word2[17],\
					word2[18],word2[19],word2[20],word2[21],word2[22],word2[23],\
					word2[24],word2[25],word2[26],word2[27],word2[28],word2[29]));
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x3),\
					word3[0] ,word3[1] ,word3[2] ,word3[3] ,word3[4] ,word3[5] ,\
					word3[6] ,word3[7] ,word3[8] ,word3[9] ,word3[10],word3[11] ,\
					word3[12],word3[13],word3[14],word3[15],word3[16],word3[17],\
					word3[18],word3[19],word3[20],word3[21],word3[22],word3[23],\
					word3[24],word3[25],word3[26],word3[27],word3[28],word3[29]));
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x4),\
					word4[0] ,word4[1] ,word4[2] ,word4[3] ,word4[4] ,word4[5] ,\
					word4[6] ,word4[7] ,word4[8] ,word4[9] ,word4[10],word4[11] ,\
					word4[12],word4[13],word4[14],word4[15],word4[16],word4[17],\
					word4[18],word4[19],word4[20],word4[21],word4[22],word4[23],\
					word4[24],word4[25],word4[26],word4[27],word4[28],word4[29]));
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x5),\
					word5[0] ,word5[1] ,word5[2] ,word5[3] ,word5[4] ,word5[5] ,\
					word5[6] ,word5[7] ,word5[8] ,word5[9] ,word5[10],word5[11] ,\
					word5[12],word5[13],word5[14],word5[15],word5[16],word5[17],\
					word5[18],word5[19],word5[20],word5[21],word5[22],word5[23],\
					word5[24],word5[25],word5[26],word5[27],word5[28],word5[29]));
		patout.write("Frame %s : 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s 1v%s "\
					"1v%s 1v%s 1v%s 0v00000000 0v00000000 1v%s 1v%s 1v%s 1v%s "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 "\
					"0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000 0v00000000\n"%(frame_str(x6),\
					word6[0] ,word6[1] ,word6[2] ,word6[3] ,word6[4] ,word6[5] ,\
					word6[6] ,word6[7] ,word6[8] ,word6[9] ,word6[10],word6[11] ,\
					word6[12],word6[13],word6[14],word6[15],word6[16],word6[17],\
					word6[18],word6[19],word6[20],word6[21],word6[22],word6[23],\
					word6[24],word6[25],word6[26],word6[27],word6[28],word6[29]));
		xx = xx + 6
		for ee in range(0, 30): # 30 loop
			word1.pop(0); word2.pop(0); word3.pop(0); word4.pop(0); word5.pop(0); word6.pop(0)
	return

def run_butler():
	os.system('rm -fr data_uri/muon_patt.txt')
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '598,598p'| sed -e 's@.*:@Frame 0600 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '599,599p'| sed -e 's@.*:@Frame 0601 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '600,600p'| sed -e 's@.*:@Frame 0602 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '601,601p'| sed -e 's@.*:@Frame 0603 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '602,602p'| sed -e 's@.*:@Frame 0604 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | sed -n '603,603p'| sed -e 's@.*:@Frame 0605 :@g' >> phtftests/temp/muon_patt.txt")
	os.system("cat phtftests/temp/muon_patt.txt | grep Frame | sed -e 's@.*:@@g' | sed -e 's@1v@@g' |sed -e 's@0v@@g' | perl -lape 's/\s+//sg' > phtftests/temp/muon_patt.dat")
	os.system('cp phtftests/temp/muon_patt.txt data_uri/muon_patt.txt')
	os.system('mp7butler.py buffers BMTF_R1_180 algoPlay --inject file://data_uri/muon_patt.txt') ###### added : This is where I choose which file to inject to RX_Buffer (Stavros)muon1_99GeV.txt or (Janos)mp7_in.tst
	os.system('mp7butler.py capture BMTF_R1_180')
	os.system('rm -fr phtftests/temp/tx_summary.txt')
	os.system('cp data/tx_summary.txt phtftests/temp/tx_summary.txt')

def read_tx_summary(n):
	zz=0
	report_bmtf = bmtf_output()
	Pt_dttf_output = report_bmtf[0]
	tr_addr_output = report_bmtf[1]
	ph_dttf_output = report_bmtf[2]
	qu_dttf_output = report_bmtf[3]
	va_ettf_output = report_bmtf[4]
	si_ettf_output = report_bmtf[5]
	#-----------------WS----------------#
	Pt_dttf_WS_output = report_bmtf[6] #---------- muon 1
	tr_addr_WS_output = report_bmtf[7]
	ph_dttf_WS_output = report_bmtf[8]
	qu_dttf_WS_output = report_bmtf[9]
	va_ettf_WS_output = report_bmtf[10]
	si_ettf_WS_output = report_bmtf[11]
	Pt_dttf_WS_output2 = report_bmtf[12] #------ muon 2
	tr_addr_WS_output2 = report_bmtf[13]
	ph_dttf_WS_output2 = report_bmtf[14]
	qu_dttf_WS_output2 = report_bmtf[15]
	va_ettf_WS_output2 = report_bmtf[16]
	si_ettf_WS_output2 = report_bmtf[17]
	Pt_dttf_WS_output3 = report_bmtf[18] #------ muon 3
	tr_addr_WS_output3 = report_bmtf[19]
	ph_dttf_WS_output3 = report_bmtf[20]
	qu_dttf_WS_output3 = report_bmtf[21]
	va_ettf_WS_output3 = report_bmtf[22]
	si_ettf_WS_output3 = report_bmtf[23]
	
	# print Pt_dttf_output;
	# print tr_addr_output;
	# print ph_dttf_output;
	# print qu_dttf_output;
	# print va_ettf_output;
	# print si_ettf_output;
	# print Pt_dttf_WS_output;
	# print tr_addr_WS_output;
	# print ph_dttf_WS_output;
	# print qu_dttf_WS_output;
	# print va_ettf_WS_output;
	# print si_ettf_WS_output;
	for event in events:
		if ((n-1)*100 <= int(event.get("id")) <= (n*100)-1):#if ((n-1)*100 <= int(event.get("id")) <= (n*100)-1):
			info_dttf=event.xpath("./Wheel[@id='-2']/Sector[@id='own']/Segment[@id='low']/info[@type='DTTF']")[0] #------ TF outputs
			info_dttf.xpath("./pt"       )[0].text = Pt_dttf_output[zz]
			info_dttf.xpath("./tradd_st1")[0].text = tr_addr_output[zz][0:1]
			info_dttf.xpath("./tradd_st2")[0].text = tr_addr_output[zz][1:2]
			info_dttf.xpath("./tradd_st3")[0].text = tr_addr_output[zz][2:3]
			info_dttf.xpath("./tradd_st4")[0].text = tr_addr_output[zz][3:4]
			info_dttf.xpath("./phi"      )[0].text = ph_dttf_output[zz]
			info_dttf.xpath("./qual"     )[0].text = qu_dttf_output[zz]
			info_dttf.xpath("./sig"  )[0].text     = si_ettf_output[zz]
			info_dttf.xpath("./eta"  )[0].text     = va_ettf_output[zz]
			#--------------------- WS ----------------------------------------#
			info_dttf_WS=event.xpath("./Wheel[@id='-1']/Sector[@id='own']/Segment[@id='low']/info[@type='DTTF']")[0] #----- WS muon 1
			info_dttf_WS.xpath("./pt"       )[0].text = Pt_dttf_WS_output[zz]
			info_dttf_WS.xpath("./tradd_st1")[0].text = tr_addr_WS_output[zz][0:1]
			info_dttf_WS.xpath("./tradd_st2")[0].text = tr_addr_WS_output[zz][1:2]
			info_dttf_WS.xpath("./tradd_st3")[0].text = tr_addr_WS_output[zz][2:3]
			info_dttf_WS.xpath("./tradd_st4")[0].text = tr_addr_WS_output[zz][3:4]
			info_dttf_WS.xpath("./phi"      )[0].text = ph_dttf_WS_output[zz]
			info_dttf_WS.xpath("./qual"     )[0].text = qu_dttf_WS_output[zz]
			info_dttf_WS.xpath("./sig"  )[0].text     = si_ettf_WS_output[zz]
			info_dttf_WS.xpath("./eta"  )[0].text     = va_ettf_WS_output[zz]
			info_dttf_WS2=event.xpath("./Wheel[@id='0']/Sector[@id='own']/Segment[@id='low']/info[@type='DTTF']")[0] #----- WS muon 2
			info_dttf_WS2.xpath("./pt"       )[0].text = Pt_dttf_WS_output2[zz]
			info_dttf_WS2.xpath("./tradd_st1")[0].text = tr_addr_WS_output2[zz][0:1]
			info_dttf_WS2.xpath("./tradd_st2")[0].text = tr_addr_WS_output2[zz][1:2]
			info_dttf_WS2.xpath("./tradd_st3")[0].text = tr_addr_WS_output2[zz][2:3]
			info_dttf_WS2.xpath("./tradd_st4")[0].text = tr_addr_WS_output2[zz][3:4]
			info_dttf_WS2.xpath("./phi"      )[0].text = ph_dttf_WS_output2[zz]
			info_dttf_WS2.xpath("./qual"     )[0].text = qu_dttf_WS_output2[zz]
			info_dttf_WS2.xpath("./sig"  )[0].text = si_ettf_WS_output2[zz]
			info_dttf_WS2.xpath("./eta"  )[0].text = va_ettf_WS_output2[zz]	
			info_dttf_WS3=event.xpath("./Wheel[@id='1']/Sector[@id='own']/Segment[@id='low']/info[@type='DTTF']")[0] #----- WS muon 3
			info_dttf_WS3.xpath("./pt"       )[0].text = Pt_dttf_WS_output3[zz]
			info_dttf_WS3.xpath("./tradd_st1")[0].text = tr_addr_WS_output3[zz][0:1]
			info_dttf_WS3.xpath("./tradd_st2")[0].text = tr_addr_WS_output3[zz][1:2]
			info_dttf_WS3.xpath("./tradd_st3")[0].text = tr_addr_WS_output3[zz][2:3]
			info_dttf_WS3.xpath("./tradd_st4")[0].text = tr_addr_WS_output3[zz][3:4]
			info_dttf_WS3.xpath("./phi"      )[0].text = ph_dttf_WS_output3[zz]
			info_dttf_WS3.xpath("./qual"     )[0].text = qu_dttf_WS_output3[zz]
			info_dttf_WS3.xpath("./sig"  )[0].text = si_ettf_WS_output3[zz]
			info_dttf_WS3.xpath("./eta"  )[0].text = va_ettf_WS_output3[zz]		
			zz=zz+1
	return

## MAIN ##
for i in range(1,hundred_events+1):
	read_xml_100(i)
	patout = open('phtftests/temp/muon_patt.txt','wb')
	create_muon_patt(hexlist,i)
	patout.close()
	run_butler()
	read_tx_summary(i)
	print colored(44*"=", 'red')
	print colored("--> %d/%d events testing completed <--" %(i*100,hundred_events*100), 'red')
	print colored(44*"=", 'red')
	print
if   args.pr=='none' : print colored("Inputs taken from here: /afs/cern.ch/work/g/gflouris/public/%s" %(args.pu), 'green')
else                 : print colored("Inputs taken from here: ./phtftests/primitives/%s" %(args.pr), 'green')
print colored("Output are stored here: ./phtftests/report/xmlout.xml", 'green')
print
tree.write(xmlout)
