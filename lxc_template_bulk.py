#!/usr/bin/env python3

# simple python script to bulk-download proxmox lxc templates
# uses threads to download multiple templates at once

# bash oneliner to be converted
# pveam available | xargs -0 | awk '{print $2;}' | while read template; do pveam download local $template; done


# imports
#import subprocess   # running shell commands
import threading     # for doing multiple things at the same time
from sultan.api import Sultan
import time
from numpy import numpy.split # unsure if the is correct syntax

# some variables
s = Sultan() # for running commands
download_group_size = 4
	
#def confirm_dialog():

	# ask for user to confirm install
	# returns True if `y`
	
#	answer = ""

#	while answer not in ["y", "n"]:
#		answer = input(
#			"This will take up a good amount of space on your system, continue? (y/n) "
#		
#		).lower()
#
#	return answer == "y"
#
#	if answer == "y":
#
#		get_available_templates()
#		
#		else:
#			
#			print("Cancelling Install")
#			exit()
			
			
# find all available templates, then divide into groups
def get_available_templates:
    
    # get available templates, store as var (?)
#	raw_available_templates = subprocess.run(
#		
#		['pveam', 'available'],
#		
#		stdout=subprocess.PIPE,
#		shell=True,
#		check=True,
#		text=True
#
#	)
	
	print('Fetching available templates')
	
	with Sultan.load(sudo=False) as s: # does this need to be here?
        # get available templates with pveam
        raw_available_templates = s.pveam('available').run()
		
		# convert to utf, and an array. TODO: remove the location and spacing prepending the template name
		available_templates = raw_available_templates.stdout.decode('utf-8').splitlines()
		
		# scrub the unneeded stuff (THIS MAY BE UNNECESSARY)
		clean_available_templates = for i in available_templates: # unsure about making it a variable, is this allowed?
			
			# stuff to remove
			available_templates.replace('system          ', '')
			available_templates.replace('turnkey         ', '')
			
		# convert array to chunks	
		global chucked_templates = numpy.array_split(clean_available_templates, int(download_group_size))
		
		# print number of available templates
		print('Found ' len(clean_available_templates) 'templates') 
			  
		
			  
	
# install the templates
def install_templates:
	
	with Sultan.load(sudo=True) as s:
		
		# select list of templates to download		
			s.pveam('download', download_location, to_install).run()
			
			
			
			
			
# set the download location
download_location = input("Set Download Location (This will be the name of the disk in Proxmox's web GUI): ")



















