# Processing files from CHILDES database
# The following script is used to extract utterance and word count
	# information from clean corpus files
# Author/contributor: Lindsay Hracs
# Date (last updated): 12.01.18
# Purpose: Candidacy paper
# Running Python 3.6.0


from __future__ import division
import os
import glob
import nltk
import re
from nltk.tokenize import *

outfile = open('Counts.txt', 'w')

outfile.write('Filename' + ',' + 'Speaker' + ',' + 'TotalUtteranceCount' + ',' + 'TotalWordCount' + ',' + 'SpeakerUtteranceCount' + ',' + 'SpeakerWordCount' + ',' + 'SpeakerMLU' + '\n')

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
	
    UtteranceCount = 0
    WordCount = 0
    CHIUtteranceCount = 0
    CHIWordCount = 0
    CHIMLU = 0
    CGUtteranceCount = 0
    CGWordCount = 0
    CGMLU = 0
    
    # set speaker variable as string
    
    speaker = ''

    # .replace() method used to find line headers and add [SPLIT_HERE];     
        # marker added to simplify processing below
    # sentence tokenizing and splitting on new lines is problematic with     
        # ID and situation tags
    newcontent = raw.replace('\n*', '[SPLIT_HERE]' + '\n' + '*').replace('\n@', '[SPLIT_HERE]' + '\n' + '\@')

    # .split() method returns a list of strings; split on '[SPLIT_HERE]'
    splitdata = newcontent.split('[SPLIT_HERE]')

	# calculates number of utterances in the file
    for sentence in splitdata: 
    	# searchers for all utterances   
        if re.search(r'\n\*', sentence): 
            UtteranceCount = UtteranceCount + 1
    
    # calculates number of words in the file
    for sentence in splitdata:
        if sentence.startswith('\n*'):
            words = word_tokenize(sentence)
            for word in words:
                # searchers for alphanumeric char at start of string
                if re.search(r'^\w', word):
                    WordCount = WordCount + 1
                   
    # calculates number of CHILD utterances in the file
    for sentence in splitdata: 
    	# searchers for all utterances   
        if re.search(r'(\n\*CHI)', sentence):
            speaker = 'child' 
            CHIUtteranceCount = CHIUtteranceCount + 1
    
    # calculates number of CHILD words in the file
    for sentence in splitdata:
        if sentence.startswith('\n*CHI'):
            words = word_tokenize(sentence)
            for word in words:
                # searchers for alphanumeric char at start of string
                if re.search(r'^\w', word):
                    CHIWordCount = CHIWordCount + 1       

	# set MLU to zero if no child utterances; can't divide by zero!           
    if CHIUtteranceCount != 0:
    	CHIMLU = CHIWordCount/CHIUtteranceCount    
    else:
        CHIMLU = 0          
		  
    # calculates number of CAREGIVER utterances in the file
    for sentence in splitdata: 
    	# searchers for all utterances   
        if re.search(r'(\n\*MOT|\n\*FAT)', sentence):
            speaker = 'caregiver' 
            CGUtteranceCount = CGUtteranceCount + 1
    
    # calculates number of CAREGIVER words in the file
    for sentence in splitdata:
        if sentence.startswith('\n*MOT') or  sentence.startswith('\n*FAT'):
            words = word_tokenize(sentence)
            for word in words:
                # searchers for alphanumeric char at start of string
                if re.search(r'^\w', word):
                    CGWordCount = CGWordCount + 1  
                        
    # set MLU to zero if no caregiver utterances; can't divide by zero!                  
    if CGUtteranceCount != 0:
    	CGMLU = CGWordCount/CGUtteranceCount    
    else: 
        CGMLU = 0
		
	#write child data line   
    outfile.write(filename + ',' + 'child' + ',' + str(UtteranceCount) + ',' + str(WordCount) + ',' + str(CHIUtteranceCount) + ',' + str(CHIWordCount) + ',' + str(CHIMLU) + '\n') 
    
    #write caregiver data line   
    outfile.write(filename + ','+ 'caregiver' + ',' + str(UtteranceCount) + ',' + str(WordCount) + ',' + str(CGUtteranceCount) + ',' + str(CGWordCount) + ',' + str(CGMLU) + '\n') 
                 
# included to ensure all files processed
print ('Total Number of Files:' + str(FileCount))	

outfile.close()
