#!/usr/bin/env python

mapping = {

   'A' : '00',
   'T' : '01',
   'G' : '10',
   'C' : '11',
}


def decode_dna( string ):

 pieces = []
 for i in string:
  pieces.append( mapping[i] )

 return "".join(pieces)


string = 'TGGCTCATTGACTCTATGTGTCGCTGGTTCTATCACTTCCTGAGTGATTCACTGGTTGACTGATACATACATTCGTTTCCTGAGTGATTCACTGTTTTCCTGTGTGCCTCTTTCAGTCCT'
h = hex(int(decode_dna(string),2))
print(h)