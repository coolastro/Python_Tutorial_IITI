import sys

""" 
    This is simple python script to add numbers
    as input from the terminal
"""

def AddPositiveNumbers(a, b, c=None):
    if c == None: 
	c = 0
    	print "The sum of %f and %f is %f"%(a,b,a+b)
    else:    
    	print "The sum of %f, %f and %f is %f"%(a,b,c,a+b+c)

if __name__=="__main__":
   a = float(sys.argv[1])
   b = float(sys.argv[2])
   AddPositiveNumbers(a, b)
   

