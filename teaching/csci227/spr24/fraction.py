"""
The Fraction class and gcd helper function from 
ThinkCS Chapter 18:  https://runestone.academy/ns/books/published//thinkcspy/
"""

def gcd(m, n):
    """
    Helper function that computes the GCD of two numbers.
    """
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    """
    The Fraction class from ThinkCS Chapter 18.
    """
    def __init__(self, top, bottom):
        """
        Initializes a fraction object.
        """
        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        """
        Makes a nice string of the fraction for printing.
        """
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        """
        Simplifies (cancels common factors) of the fraction.
        """
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def __add__(self,otherfraction):
        """
        Adds two fractions (overloads +) and returns simplified sum.
        """
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
