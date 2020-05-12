# CHILDES Processing

## Overview

This repository contains samples of the scripts I wrote and used for my
candidacy exam in March 2018. The primary focus is cleaning and extracting specifc data from [CHAT](https://talkbank.org/manuals/CHAT.pdf) (.cha) files available from the [Child Language Data Exchange System](https://childes.talkbank.org/browser/) (CHILDES) database.

### List of scripts and what they do:

**ChangeFileNames.py**<br/>
Prepends [CHAT](https://talkbank.org/manuals/CHAT.pdf) file with the name of the corpus it comes from for easier organization.

**ChildInfo.py**<br/>
Extracts participant information from clean corpus files.

**Counts.py**<br/>
Extracts utterance and word count information from clean corpus files.

**DataCleaning.py**<br/>
Reads in transcribe CHAT files and outputs clean, easily readable, text files.

**OnlyCounts.py**<br/>
Extracts counts of the word 'only' from clean corpus files.

**OnlyPlusContextPull.py**<br/>
Extracts all utterances containing the word 'only' along with 10 preceding
context utterances.
