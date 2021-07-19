#!/usr/bin/python3

#import standart libraries
import sys
import fileinput
import re

#import classes
from Color import *
from Style import *
from MyParser import *

#This function verify if provided by user values are not default and return proper replacement
#It will allow us to color or underline matched pattern
def replace_match_string(userColor, userStyle, regex, default):
    if (userColor.name == "reset"):
        ret_val = userStyle.value + regex + default
    elif(userStyle.name == "reset"):
        ret_val = userColor.value + regex + default
    elif(userStyle.name == "reset" and userColor.name == "reset"):
        ret_val = regex
    else:
        ret_val = userColor.value + userStyle.value + regex + default
    
    return ret_val

#This function will search for pattern with regelur experession
#In case pattern found, function will apply provided locale arguments to this match
#If no locale were provided, default values will use
#Function will read line by line from provided list of files(or simple file) or from STDIN if no files were provided
def search(regex, inputFile, userColor, userStyle, userMachine):
    default = "\x1b[0m" #Set sefault for locale settings 
    
    current_linenumber = 0 #In case we're reading STDIN, we'll use local counter and not filelineno()

    pattern = re.compile(regex, re.IGNORECASE)  # Compile a case-insensitive regex
    input = fileinput.input(inputFile) if len(inputFile) else sys.stdin
    
    for line in input:
        current_linenumber += 1
        res = pattern.search(line)
        if res != None:      # If a match is found
            replacement = replace_match_string(userColor, userStyle, regex, default)            
            line = re.sub(re.escape(regex), replacement, line, flags=re.I)
            current_filename = fileinput.filename() if len(inputFile) else "STDIN"
            current_linenumber = fileinput.filelineno() if len(inputFile) else current_linenumber
            if(userMachine == "True"):
                print(current_filename, ":",userColor.value, current_linenumber, default, ":", res.start(),":",res.group())
            else:
                print("Input name is: ", current_filename, " Line number: ", userColor.value, current_linenumber, default, line.rstrip('\n'))
        else:
            print("Pattern not found")


if __name__ == '__main__':
    # Parse the arguments parseArguments class
    args = MyParser.parseArguments()
   
    # Raw print arguments
    for a in args.__dict__:
        print(str(a) + ": " + str(args.__dict__[a]))

    # Run function
    search(args.regex, args.files, args.color, args.underline, args.machine)
    