# Processing files from CHILDES database
# The following script is used to prepend filenames with the corpus name
# and "clean" designation	
# Author/contributor: Lindsay Hracs
# Date: 25.11.17
# Python ver. 3.6.0

import os
import glob 

# you need to specify file path; this will search recursively through folders
files = glob.glob('YOUR FILE PATH GOES HERE/**/*.cha', recursive=True)


for f in files:
    if f.endswith('.cha'):
    	# os.path.split method creates and ordered pair	    
        filename = (os.path.split(f)[1])
        pathname = (os.path.split(f)[0])
        # split at each folder level so that corpus parent folder  		 
            # (i.e. corpus name) can be separated out and used in rename
        x = pathname.split('/')
        # os.rename method moves files to working directory; specifies    
            # full destination filepath in rename
        os.rename(f,  pathname + '/' + x[5] + '_Clean_' + filename) 
 	
		
