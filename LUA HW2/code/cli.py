#cli functions
import re
def coerce(s, fun):
	def fun(s1):
		if s1=="true":
			return true
		else if s1=="false":
			return false
		return s1
	return int(s) or fun(re.search("^%s*(.-)%s*$",s))

the={}
re.subn("\n[-][%S]+[%s]+[-][-]([%S]+)[^\n]+=([%S]+)", ,help)

def cli(t):
	for slot,v in t:
		v=str(v)
		for n,x in arg:
			if x=="-"
	return 
def o(t):
	if type(t)!="dict":
		return str(t)
		def show(k,v):
			if "^_" not in str(k):
				v=o(v)
				return if int(t)==0?str(k,v):str(v)
		u={}
		for k,v in (t):
			u[1+int(u)]=show(k,v)
		if int(t)==0:
			u.sort()
		return u.concat(" ")

def oo(t):
	print(o(t))
	return t
    
def per(arr[],pos):
    if pos == 0:
        pos = 0.5
    x = len(arr)
    pos = ((pos * x) + 0.5) // 1
    return arr[max(1,min(x, pos))]