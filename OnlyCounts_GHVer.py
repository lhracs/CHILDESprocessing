# Processing corpora form the CHILDES database
# The following script is used to extract 'only' count information from clean corpus files
# Author/contributor: Lindsay Hracs
# Date (last updated): 12.01.18
# Python ver. 3.6.0


from __future__ import division
import os
import glob
import nltk
import re
from nltk.tokenize import *
porter = nltk.PorterStemmer()

outfile = open('OnlyCounts.txt', 'w')

outfile.write('Filename' + ',' + 'Speaker' + ',' + 'OnlyCount' + '\n')

# you need to specify file path; this will search recursively through folders
files = glob.glob('YOUR FILE PATH GOES HERE/**/*.cha', recursive=True)

# set file count variable as integer

FileCount = 0

# open and read in content of each file

for file in files:
    f = open(file)
    raw = f.read()
    filename = os.path.split(file)[1]
    FileCount = FileCount + 1 

	# set count variables as integer
	
    CHIOnlyCount = 0
    CGOnlyCount = 0

    # .replace() method used to find line headers and add [SPLIT_HERE];     
        # marker added to simplify processing below
    # sentence tokenizing and splitting on new lines is problematic with     
        # ID and situation tags
    newcontent = raw.replace('\n*', '[SPLIT_HERE]' + '\n' + '*').replace('\n@', '[SPLIT_HERE]' + '\n' + '\@')

    # .split() method returns a list of strings; split on '[SPLIT_HERE]'
    splitdata = newcontent.split('[SPLIT_HERE]')

    
    # calculates number of "onlys" in child utterances
    for sentence in splitdata:
        if sentence.startswith('\n*CHI'):
            words = word_tokenize(sentence)
            for word in words:
            # stemmer removes common English inflection; not necessary for this search, but helpful for others (e.g. negation)
                stem = porter.stem(word) 
                if word == 'only':
                	CHIOnlyCount = CHIOnlyCount + 1
                	
	# calculates number of "onlys" in caregiver utterances
    for sentence in splitdata:
        if sentence.startswith('\n*MOT') or sentence.startswith('\n*FAT'):
            words = word_tokenize(sentence)
            for word in words:
             # stemmer removes common English inflection; not necessary for this search, but helpful for others (e.g. negation)
                stem = porter.stem(word) 
                if word == 'only':
                	CGOnlyCount = CGOnlyCount + 1
		
	# write child data line   
    outfile.write(filename + ',' + 'child' + ',' + str(CHIOnlyCount) + '\n') 
     
    # write caregiver data line   
    outfile.write(filename + ',' + 'caregiver' + ',' + str(CGOnlyCount) + '\n')
                 
# included to ensure all files processed
print ('Total Number of Files:' + str(FileCount))	

outfile.close()
