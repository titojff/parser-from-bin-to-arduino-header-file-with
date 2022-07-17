#!/usr/bin/env python3

import sys

#ficheiro .bin to string >> header file
with open(sys.argv[2],'wb') as result_file:
  result_file.write(b'char %s[] = ' % sys.argv[3].encode('utf-8'))
  for b in open(sys.argv[1], 'rb').read():
    result_file.write(b'%02X' % b)
  result_file.write(b'')
  
##transform to array de ints para o arduino  
co =open("code.h", "r+")
coresult =open("Code.h", "w")
line = co.read()
line2=line[14:]#so'hexadecimals seguidos
line3="int code[] = {"
print (line2)
i = 0
while i < len(line2):
    hexH= line2[i]
    hexL= line2[(i+1)]
    hex=hexH+hexL
    print(hex)
    dec=int(hex,16)
    print(dec)
    decS=str(dec)
    line3 = line3 + decS + ","
    i = i+2
line3=line3[:-1] + "};"    
print (line3)
coresult.write(line3)

coresult.close()
co.close()


