#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom import minidom
from ROOT import gROOT, TCanvas, TH1F
gROOT.Reset()

histo1 = TH1F("histo1","histo1",100,-1,1)

doc = minidom.parse("new_luts_20kevents.xml")
#doc = minidom.parse("output_new_luts_500events.xml")
print
events = doc.getElementsByTagName("Event")
k = errors = 0
n_events = 16994
pt_tr_emu=[]
pt_DTTF=[]
resolution = 0
jj=0

for event in events:
	resolution=0
	if int(event.getAttribute("id")) < n_events:
		infos = event.getElementsByTagName("info")
		for info in infos:
			if info.getAttribute("type") == "tr_emu":
				pt_tr_emu.append(info.getElementsByTagName("pt")[0].firstChild.data)

			if info.getAttribute("type") == "DTTF":
				pt_DTTF.append(info.getElementsByTagName("pt")[0].firstChild.data)
			    
				resolution = (1./float(pt_tr_emu[k]) - 1./float(pt_DTTF[k])) / (1./float(pt_tr_emu[k]))
				histo1.Fill(resolution)
                        if info.getAttribute("type") == "event":
                                 jj = info.getElementsByTagName("tree_event")[0].firstChild.data
		if resolution!=0: 
			print jj 
			#print k
				#print("%d  %s  %s" %(k,pt_tr_emu[k],pt_DTTF[k]))

		k=k+1
 
c1 = TCanvas( 'c1', 'Resolution', 200, 10, 700, 500 )
#fun1 = TF1( 'fun1', 'abs(sin(x)/x)', 0, 10 )
c1.SetGridx()
c1.SetGridy()
histo1.Draw()
c1.Update()

raw_input("Press any key to exit.")
