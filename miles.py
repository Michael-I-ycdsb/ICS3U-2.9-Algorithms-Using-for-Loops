"""
File: miles.py
Author: Michael Iacobelli
Date: 2024-03-19
Description: A program that outputs values for kilometres and equivalent miles 
             every 10 km up to 100 km.
"""

# loops for every 10 in range from 10 to 100
for kilometers in range(10, 110, 10):
    # calculates miles
    miles = kilometers * 0.625

    print(f'{kilometers} km = {miles} miles')