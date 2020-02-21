TrUpS
=====

Twiki Page:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/TrUpS

=======================================================

Set-up enviroment:

cmsrel CMSSW_8_0_2

cd CMSSW_8_0_2/src

cmsenv

git clone https://github.com/gflouris/UIoannina/

scram b

=======================================================

Create Ntuples:

CMSSW_8_0_2/src/UIoannina/TrUpS/test

=======================================================

Create patterns in XML format:

CMSSW_8_0_2/src/UIoannina/TrUpS/macros/root_to_xml

=======================================================

Run hardware tests:

CMSSW_8_0_2/src/UIoannina/TrUpS/macros/benchtest



