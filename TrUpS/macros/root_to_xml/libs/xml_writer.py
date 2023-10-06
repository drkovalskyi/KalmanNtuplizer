#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
from Global_Dicts_For_XML import *
page = etree.Element('Data')
doc = etree.ElementTree(page)
dict_wheels = {-2:'m2', -1:'m1', 0:'c', 1:'p1', 2:'p2'}
global output_file

def write_gen(segment,segment_id, wheel_id) :

  info = etree.SubElement(segment, 'info',type="GEN")
  pt = etree.SubElement(info, 'pt')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gen_pt'])
  eta = etree.SubElement(info, 'eta')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gen_eta'])
  phi = etree.SubElement(info, 'phi')
  phi.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gen_phi'])

#def write_gmt(segment,segment_id, wheel_id) :
#
#  info = etree.SubElement(segment, 'info',type="GMT")
#  pt = etree.SubElement(info, 'pt')
#  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gmt_pt'])
#  eta = etree.SubElement(info, 'eta')
#  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gmt_eta'])
#  phi = etree.SubElement(info, 'phi')
#  phi.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['gmt_phi'])

def write_tr_emu(segment,segment_id, wheel_id) :
  info = etree.SubElement(segment, 'info',type="tr_emu")
  pt = etree.SubElement(info, 'pt')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tremu_pt'])
  eta = etree.SubElement(info, 'tradd_st1')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tradd_st1'])
  eta = etree.SubElement(info, 'tradd_st2')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tradd_st2'])
  eta = etree.SubElement(info, 'tradd_st3')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tradd_st3'])
  eta = etree.SubElement(info, 'tradd_st4')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tradd_st4'])
  eta = etree.SubElement(info, 'phi')
  eta.text =str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tremu_phi'])
  eta = etree.SubElement(info, 'eta')
  eta.text =str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tremu_eta'])
  eta = etree.SubElement(info, 'qual')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tremu_qual'])
  eta = etree.SubElement(info, 'sig')
  eta.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_own_'+str(segment_id)]['tremu_sig'])


def write_ph_emu(segment,segment_id, sector_id, wheel_id) :
  info = etree.SubElement(segment, 'info',type="ph_emu")
  pt = etree.SubElement(info, 'b_ang_st1')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['b_ang_st1'])
  pt = etree.SubElement(info, 'b_ang_st2')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['b_ang_st2'])
  pt = etree.SubElement(info, 'b_ang_st4')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['b_ang_st4'])
  pt = etree.SubElement(info, 'ang_st1')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['ang_st1'])
  pt = etree.SubElement(info, 'code_st1')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['code_st1'])
  pt = etree.SubElement(info, 'ang_st2')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['ang_st2'])
  pt = etree.SubElement(info, 'code_st2')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['code_st2'])
  pt = etree.SubElement(info, 'ang_st3')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['ang_st3'])
  pt = etree.SubElement(info, 'code_st3')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['code_st3'])
  pt = etree.SubElement(info, 'ang_st4')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['ang_st4'])
  pt = etree.SubElement(info, 'code_st4')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['code_st4'])

def write_th_emu(segment,segment_id, sector_id, wheel_id) :
  info = etree.SubElement(segment, 'info',type="th_emu")
  pt = etree.SubElement(info, 'hits_st1')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['hits_st1'])

  pt = etree.SubElement(info, 'hits_st2')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['hits_st2'])

  pt = etree.SubElement(info, 'hits_st3')
  pt.text = str(dict_all['dict_'+dict_wheels[wheel_id]+'_'+str(sector_id)+'_'+str(segment_id)]['hits_st3'])


def write_dttf(segment):
  info = etree.SubElement(segment, 'info',type="DTTF")
  pt = etree.SubElement(info, 'pt')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'tradd_st1')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'tradd_st2')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'tradd_st3')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'tradd_st4')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'phi')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'qual')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'eta')
  pt.text = '-999999'
  pt = etree.SubElement(info, 'sig')
  pt.text = '-99999'



def write_segment(sector,segment_id,sector_id, wheel_id):
  segment = etree.SubElement(sector, 'Segment',id=segment_id)
  write_gen(segment,segment_id, wheel_id)
#  write_gmt(segment,segment_id,wheel_id)
  write_tr_emu(segment,segment_id,wheel_id)
  write_ph_emu(segment,segment_id,sector_id, wheel_id)
  write_th_emu(segment,segment_id,sector_id, wheel_id)
  write_dttf(segment)


def write_sector(wheel,sector_id, wheel_id):
  sector = etree.SubElement(wheel, 'Sector',id=sector_id)
  write_segment(sector,"high",sector_id, wheel_id)
  write_segment(sector,"low",sector_id, wheel_id)

def write_wheel(event,wheel_id):
  wheel = etree.SubElement(event, 'Wheel', id=wheel_id)
  write_sector(wheel,"left",int(wheel_id))
  write_sector(wheel,"own",int(wheel_id))
  write_sector(wheel,"right",int(wheel_id))

def write_event(event_id) :

  event = etree.SubElement(page, 'Event', id=event_id)

  info = etree.SubElement(event, 'info',type="event")
  tree_event = etree.SubElement(info, 'tree_event')
  tree_event.text = dict_all['tree_event']

  muon = etree.SubElement(info, 'muon')
  muon.text = dict_all['nmuons']

  write_wheel(event,'-2')
  write_wheel(event,'-1')
  write_wheel(event,'0')
  write_wheel(event,'1')
  write_wheel(event,'2')

#write_event(i_event,dict_'+dict_wheels[wheel_id]+'own_l) 
  
#name_of_xml = "out.xml"
  #with open('output_100GeV_20kevents.xml', 'w') as output_file:
  #with open(name_of_xml, 'w') as output_file:
#  output_file.write(etree.tostring(doc, pretty_print = True))
