# Processes files from CHILDES database
# The following script is used to extract participant information from 
# clean corpus files
# Author/contributor: Lindsay Hracs
# Date (last updated): 12.01.18
# Python ver. 3.6.0


from __future__ import division
import os
import glob
import nltk
import re
from nltk.tokenize import *
# sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

outfile = open('ChildInfo.txt', 'w')

outfile.write('Filename' + ',' + 'ChildAgeYearsMonths' + ',' + 'ChildSex' + '\n')

# you need to specify file path; this will search recursively through folders
files = glob.glob('YOUR FILE PATH GOES HERE/**/*.cha', recursive=True)


# set counts as integers

FileCount = 0

# open and read in content of each file

for file in files:
    f = open(file)
    raw = f.read()
    filename = os.path.split(file)[1]
    FileCount = FileCount + 1 
    UtteranceCount = 0
    WordCount = 0
    # .replace() method used to find line headers and add [SPLIT_HERE];     
        # marker added to simplify processing below
    # sentence tokenizing and splitting on new lines is problematic with     
        # ID and situation tags
    newcontent = raw.replace('\n*', '[SPLIT_HERE]' + '\n' + '*').replace('\n@', '[SPLIT_HERE]' + '\n' + '\@')

    # .split() method returns a list of strings; split on '[SPLIT_HERE]'
    splitdata = newcontent.split('[SPLIT_HERE]')

	# finds target child age and sex
    for sentence in splitdata: 
    	# searchers for all utterances   
        if sentence.startswith('\n\@ID'):
            split = sentence.split('|')
            if 'CHI' in split: 
            	# 4th item in list is target child's age	
            	# files are missing info, so full age being pulled; 
            	    # missing info will be added and months calculated 
            	    # in spreadsheet
      	        ChildAge = split[3]
      	        ChildSex = split[4] 	              	        			      
            
            	
    # writing two lines to sync up with 'only' output
    outfile.write(filename + ',' + str(ChildAge) + ',' + ChildSex + '\n' + filename + ',' + str(ChildAge) + ',' + ChildSex + '\n') 

# added to ensure all files are being processed
print ('Total Number of Files:' + str(FileCount))	

outfile.close()
