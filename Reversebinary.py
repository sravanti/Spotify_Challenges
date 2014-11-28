#!/usr/bin/python
"""
Spotify Engineering challenge 1
The input contains a single line with an integer N, 1  N  1000000000.
Output one line with one integer, the number we get by reversing the binary representation of N.
"""
	
try:
	print int(bin(int(raw_input("enter a number: ")))[:1:-1], 2)
except Exception:
	print "Invalid input"

