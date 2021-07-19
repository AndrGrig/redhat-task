from enum import Enum, unique

@unique
class Style(Enum):
    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"
    reset = "\x1b[0m"

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
    
   
    @staticmethod
    def argparse(s):
        try:
            return Style[s]
        except KeyError:
            return s