import math
import re
from num_class import Num
from sym_class import Sym

class Cols:
    def __init__(self, names = {}):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        col = None
        for c, s in names.items():
            if re.search("^[A-Z]*", s):
                col = push(self.all, Num(c,s))
            else
                col = push(self.all, Sym(c,s))
            if not re.search(":$", s):
                if re.search("[!+-]$", s):
                    push(self.y, col)
                else:
                    push(self.x, col)
                if re.search("!$", s):
                    self.klass = col