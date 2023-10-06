# -*- coding: utf-8 -*-
from ROOT import *
def Create_Branches(out_tree_emu):
  global emu_pt
  emu_pt = vector('float')()
  global emu_quality 
  emu_quality = vector('float')()
  global emu_phi 
  emu_phi = vector('float')()
  global emu_tradd
  emu_tradd = vector('float')()

  out_tree_emu.Branch('pt',emu_pt)
  out_tree_emu.Branch('quality',emu_quality)
  out_tree_emu.Branch('phi',emu_phi)
  out_tree_emu.Branch('tradd',emu_tradd)
