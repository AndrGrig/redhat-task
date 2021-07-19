import argparse
import sys
from Color import *
from Style import *

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
    
    def parseArguments():
        # Create argument parser
        parser = argparse.ArgumentParser(description='Process script arguments.')

        # Mandatory arguments
        parser.add_argument("-r", '--regex', help="the regular expression to search for", type=str,required=True)

        # Optional arguments
        parser.add_argument('files', nargs='*', help='a list of files to search in. If this parameter is omitted, the script expects text input from STDIN')
        parser.add_argument('-c','--color', type=Color.argparse, choices=list(Color), help='the matched text is highlighted in color', default=Color.reset)
        parser.add_argument('-u','--underline', type=Style.argparse, choices=list(Style), help='is printed underneath the matched text', default=Style.reset)
        parser.add_argument('-m','--machine', type=str, choices=["False","True"], help='print the output in the format: "file_name:line_number:start_position:matched_text"')
        
        # Parse arguments
        args = parser.parse_args()

        return args