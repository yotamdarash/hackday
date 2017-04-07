#!/usr/bin/env python
from math import*

txt_file_B = open("TracksTwoSourceVectorsFromYoutubeToAmazon2.txt", "r")
vector_A = []
vector_B = []
for line in txt_file_B:
    vector_A.append(line.split()[0])
    vector_B.append(line.split()[1])
#
# vector_A = txt_file_A.read().split()
# vector_B = txt_file_B.read().split()

vector_A = list(map(int, vector_A))
vector_B = list(map(int, vector_B))
print vector_B
 
def square_rooted(x):
 
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
 
   numerator = sum(a*b for a,b in zip(x,y))
   denominator = square_rooted(x)*square_rooted(y)
   return round(numerator/float(denominator),3)
 
print cosine_similarity(vector_A, vector_B)