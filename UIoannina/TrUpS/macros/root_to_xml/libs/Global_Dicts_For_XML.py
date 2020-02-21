#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

global i_event

global dict_wheels
dict_wheels = {-2:'m2', -1:'m1', 0:'c', 1:'p1', 2:'p2'}


global dict_all

dict_all = {'tree_event':'-1', 'nmuons':'-1',

	   'dict_m2_own_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	  'dict_m2_own_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',	
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m2_left_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m2_right_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m2_left_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m2_right_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},


#########
	   'dict_m1_own_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	  'dict_m1_own_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',	
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m1_left_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m1_right_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m1_left_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_m1_right_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},
#######
	   'dict_c_own_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	  'dict_c_own_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',	
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_c_left_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_c_right_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_c_left_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_c_right_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},
#####

	   'dict_p1_own_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	  'dict_p1_own_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',	
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p1_left_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p1_right_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p1_left_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p1_right_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},
#####
	   'dict_p2_own_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	  'dict_p2_own_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',	
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p2_left_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p2_right_low':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '0','tremu_eta': '0', 'tremu_sig': '0', 'tremu_qual': '0'},

	   'dict_p2_left_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '-999999','tremu_eta': '-999999', 'tremu_sig': '-999999', 'tremu_qual': '-999999'},

	   'dict_p2_right_high':{
              'hits_st1': '90000000', 'hits_st2': '90000000','hits_st3': '90000000','eta':'-999999','sig':'-999999',
	      'gen_pt': '-100', 'gen_phi': '-999999', 'gen_eta': '-999999',
	      #'gmt_pt': '-100', 'gmt_phi': '-999999', 'gmt_eta': '-999999',
	      'b_ang_st1': '-512', 'b_ang_st2': '-512','b_ang_st4': '-512',
	      'ang_st1': '-2048','ang_st2': '-2048','ang_st3': '-2048','ang_st4': '-2048',
	      'code_st1': '7','code_st2': '7','code_st3': '7','code_st4': '7',
	      'tremu_pt': '0.0', 'tradd_st1': '3', 'tradd_st2': 'F', 'tradd_st3': 'F', 'tradd_st4': 'F', 'tremu_phi': '-999999','tremu_eta': '-999999', 'tremu_sig': '-999999', 'tremu_qual': '-999999'}

}


#class PyListOfXML(dict) :
	#pass
## create an istance
#pyl = PyListOfXML()
## add leaves as attributes
#for i in range(0,24 ) :
	#leaf = leaves.At(i)
	#name = leaf.GetName()
	##print name
	## add dynamically attribute to my class 
	#pyl.__setattr__(name,leaf)


def Init_dict_all():
  #print "Init Dictionary\n"
  sectors = ("left","own","right")
  for j in range(-2,3) :
    for i in range(0, 3) :
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['hits_st1'] = '90000000'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['hits_st2'] = '90000000'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['hits_st3'] = '90000000'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['hits_st1'] = '90000000'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['hits_st2'] = '90000000'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['hits_st3'] = '90000000'


      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['b_ang_st1'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['ang_st1'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['code_st1'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['b_ang_st2'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['ang_st2'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['code_st2'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['ang_st3'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['code_st3'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['b_ang_st4'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['ang_st4'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['code_st4'] = '-7'
    
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tremu_pt'] = '0.0'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tradd_st1'] = '3'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tradd_st2'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tradd_st3'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tradd_st4'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tremu_phi'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tremu_eta'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tremu_sign'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_low']['tremu_qual'] = '-999999'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['b_ang_st1'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['ang_st1'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['code_st1'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['b_ang_st2'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['ang_st2'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['code_st2'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['ang_st3'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['code_st3'] = '-7'

      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['b_ang_st4'] = '-512'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['ang_st4'] = '-2048'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['code_st4'] = '-7'
    
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tremu_pt'] = '0.0'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tradd_st1'] = '3'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tradd_st2'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tradd_st3'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tradd_st4'] = 'f'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tremu_phi'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tremu_eta'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tremu_sign'] = '-999999'
      dict_all['dict_'+dict_wheels[j]+'_'+str(sectors[i])+'_high']['tremu_qual'] = '-999999'
