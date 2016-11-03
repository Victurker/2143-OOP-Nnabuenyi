
"""
Name: Victor Nnabuenyi
Email: victurkernabs@yahoo.com
Assignment: Homework 2 - Python intro
Due: 26 Sep @ 1:00 p.m.
"""


```python

class fraction (object):
	def __init__(self, whl=whole, n = None, d = None):
		if whl:
			self.whole = whl 
		else:
			self.whole = 0.0
			self.nume = n + self.whole * d
			self.denom = d
			self.reduce()
			
		def reduce(self):
			thegcd = self.gcd(self.nume, self.denom)
			self.nume = int(self.nume/ thegcd)
			self.denom = int(self.denom/ thegcd)
			if self.nume > self.denom:
				self.whole = int (self.nume/ self.denom)
				self.nume %= self.denom
				
		def gcd(self, a, nume):
			while nume:
				a, nume = nume, a % nume
			return a 
		
		def __str__(self):
			if self.whole > 0:
				return "%d %d / %d" % (self.whole, self.nume, self.denom)
			else:
				return "%d / %d" %(self.nume, self.denom)
				
		def __mul__(self, rhs):
			nume = (self.nume + int (self.denom * self.whole)) *
			(rhs.nume + int(rhs.denom * rhs.whole))
			denom = self.denom * rhs.denom
			return fraction (0, nume, denom)
			
		def __add__(self, rhs):
			denom = int (self.denom * rhs.denom)
			nume = int ((self.nume + int (self.denom * self.whole)) *
			rhs.denom) + int ((rhs.nume + int(rhs.denom * rhs.whole)) *
			self.denom)
			if (nume == denom):
				return 1
			else:
				return fraction(0, nume, denom)
				
	if __name__ == '__main__' :
		
		a = fraction (1,1,2)
		b = fraction (0,4,5)
		c = a * b
		d = a + b 
		print ('fraction a = ',a)
		print ('fraction b = ',b)
		print ('a multiplies b = ',c)
		print ('a adds b = ',d)
		
```		
		
		
			
				
				
				
				
				
				
				
				
				
				
				
				
				
