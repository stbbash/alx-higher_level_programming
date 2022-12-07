#!/usr/bin/python3

 if name == "main":
     
     import sys
     
 lenght = len(sys.argv) - 1
 
 sum = 0
 
 if lenght == 0:
     
     print("0")
     
 else:
     
     for i in range(lenght):
         
         sum += int(sys.argv[i + 1])
         
     print("{}".format(sum))
