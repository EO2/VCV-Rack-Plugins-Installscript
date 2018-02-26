import os
import sys
import subprocess
#
# Update VCV Rack plugins from Github
# eirik.olsnes@gmail.com 2018
#
path = '/Users/eirik/Downloads/VCV-Rack/Rack'
plugins = path + '/plugins/'

# VERSION
version = '0.5.1'
ver_a = '5'
ver_b = '1'

ingit =      'git rev-parse --is-inside-work-tree 2>/dev/null'
tags = 	     'git tag'
checkout =   'git checkout tags/' # + version (detect)
reset =      'git reset HEAD --hard'
update =     'git pull origin master' # fetch..
submodules = 'git submodule update --init --recursive'
clean = 'make clean'
deps =  'make dep' # -j nProcs
make =  'make'

gits = 1 # files
os.chdir(plugins)
for file in os.listdir('.'):
    if os.path.isdir(file):	
	#print(file)
	os.chdir(file)
	closest_git_tag = None # closest to version
	version_found = False
	git_tags_raw = subprocess.check_output(tags, shell=True)
	split_tags_raw = git_tags_raw.split('\n')
	git_tags = git_tags_raw.replace('v', '')
	git_tags = git_tags.replace('VCV', '')
	split_tags = git_tags.split('\n')
	i = -1
	for git_tag in split_tags:
		i = i + 1
		if len(git_tag) > 1:
		    tag = git_tag.split('.')
		    if len(tag) > 1:
	                if tag[1] == ver_a:
			    if not version_found:
			        closest_git_tag = split_tags_raw[i]
			    if len(tag) > 2:
			        if tag[2] == ver_b:
				    version_found = True
				    continue # dont look for newer than current version
	if closest_git_tag:
	  print('\n\n\nRunning file: ' + str(gits) +' '+ file +' '+ closest_git_tag + '\n\n\n')
	  os.system(checkout + closest_git_tag)
	  os.system(reset)
	  os.system(update)
	  os.system(submodules)
	  os.system(clean) #
	  #os.system(deps) # only for Rack, not plugins?
	  os.system(make) #

	os.chdir(plugins)
	gits = gits +1
	#if gits == 5:
	#    exit()
	# todo: check tagles gits, log errors to file
