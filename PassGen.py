#!/usr/bin/env python -w
#
#
import sys,os,time
os.system('rm Pass.lst')
os.system('clear')
E = raw_input('Input a num or Symbol: ')
if len(E) !=  0:
	M = E
else:
	M =  '@'
Pass_list = open('Pass.lst','a');

def lower(Text):
	global Pass_list
	Keys=[M,123,456,143]
	for key in Keys:
		if key is '@':
			Pass_list.write('%s%s\n'%(Text.lower(),key))
		if key != '@':
			Pass_list.write('%s%d\n'%(Text.lower(),int(key)))
 




os.system('clear')
name = str(raw_input('Enter First name: '));time.sleep(0.7);os.system('clear')
last = str(raw_input('Enter Last  name: '));time.sleep(0.7)



if len(name) != 0:
	lower(name)
	lower(last)
	os.system('clear');print'[+] Done'
