# jackhmmerParse
Python function to get info from jackhmmer hmmer3-text output file.
Created June 2015 by Grace Barkhuff.

Takes a manually edited jackhmmer3-text file and domain name as input, returns a dictionary of dictionaries
of parsed data. Each gi has its own dictionary containing: the gi, domain name given, start location, end location, and amino acid sequence.

The jackhmmer3-text file must be manually edited before being used as input to contain only the data for the final iteration. (e.g.: if jackhmmer ran 5 iterations, the hmmer3-text file contains information for iterations 1-5. The data for iterations 1-4 must be deleted before using jackhmmerParse.py, otherwise the program will unnecessarily parse each gi 5 times, and will not remove any gis which did not pass threshold in the final iteration but did pass in an earlier iteration.) An automated way to remove the earlier iterations still needs to be created.
