from enum import Enum, unique

@unique
class Color(Enum):
   red="\033[0;31m"
   green="\033[0;32m"
   blue = "\033[0;34m"
   yellow = "\033[1;33m"
   white = "\033[1;37m"
   reset = "\x1b[0m"
   
   def __str__(self):
        return self.name

   def __repr__(self):
      return str(self)
    
   
   @staticmethod
   def argparse(s):
      try:
         return Color[s]
      except KeyError:
         return s