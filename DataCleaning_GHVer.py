# Cleaning CHILDES Corpus Data
# This code is used for reading in transcribed CHAT files and creating a                  
    # text file output
# Author/contributor: Lindsay Hracs 
# Date (last updated): 12.01.18
# Python ver. 3.6.0

import glob
import re


# specify files to process
# recursive folder structure used to account for variation in folder structure for each corpus
# you need to specify your file path
files = glob.glob('YOUR FILE PATH GOES HERE/**/*.cha', recursive=True)

# open and read in content of each file
for file in files:
    f = open(file)
    raw = f.read()
    outfile1 = open(file, 'w') 
    
    # .replace() method used to find line headers and add [SPLIT_HERE]; 
        # marker added to simplify processing below
    # sentence tokenizing and splitting on new lines resulted in messy, 
        # incomplete data
    newcontent = raw.replace('\n*', '[SPLIT_HERE]' 
        + '\n' + '*').replace('\n@', '[SPLIT_HERE]' + '\n' 
        + '@').replace('\n%', '[SPLIT_HERE]' + '\n' + '%')
   	# .split() method returns a list of strings; split on '[SPLIT_HERE]'
    splitdata = newcontent.split('[SPLIT_HERE]')
    
    # clean data (and ignore unwanted data) before writing to new file
    for chunk in splitdata:
        # grab ID, situation, and all participant utterances; 
        # code ignores annotated tiers
        if chunk.startswith(('\n@ID', '\n@Sit', '\n*')): 
            # clean *CHI ID info
            clean1 = re.sub(r'\|{3}', '|', chunk) 
            # clean remaining ID info
            clean2 = re.sub(r'\|{3}', '|', clean1)
            # removes markers and comments that are not part of the utterance using re.VERBOSE for human readability
            clean3regex = re.compile(
            r'''\s+(\[|\(|\<)+.+(\]|\)|\>)+\s+ 
            |\s*\d+_*\d+\s* 
            |\_
            |\s*\[\/\/\]\s* 
            |\+ 
            |\@(q|c)\s 
            |\s\(.+\)''', re.VERBOSE)
            clean3 = re.sub(clean3regex, ' ', clean2)
			# removes various idiosyncratic notation using re.VERBOSE
            clean4regex = re.compile(
            r'''‡\s*
            |\s(\"|\<)\s
            |\/
            |\"
            |&.?\w+\s*
            |-
            |\s\+\"\/''', re.VERBOSE)
            clean4 = re.sub(clean4regex, '', clean3)
            outfile1.write(clean4)	
            #outfile1 = io.StringIO(chunk)

    outfile1.close()

	
