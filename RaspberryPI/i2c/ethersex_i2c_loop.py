#!/usr/bin/env python3
import quick2wire.i2c as i2c
from quick2wire.i2c import I2CMaster, writing, reading

from time import sleep

address = 0x04

#hexstrings = ['0x76', '0x65', '0x72', '0x73', '0x69', '0x6f', '0x6e', '0x0']
while True :
 ecmdString = []
 read_results=[]

 with I2CMaster() as i2c:
  while True:
 
   ecmd = "version"
   for ecmdChar in ecmd:
    ecmdString.append(ord(ecmdChar))
   i2c.transaction(writing(address,ecmdString))
   print (ecmd)
   print (ecmdString)
   sleep(1)
   read_results=i2c.transaction(reading(address,37))
   print(read_results)
   ecmdString = []
   print ("---------")

   ecmd = "fuse"
   for ecmdChar in ecmd:
    ecmdString.append(ord(ecmdChar))
   i2c.transaction(writing(address,ecmdString))
   print (ecmd)
   print (ecmdString)
   sleep(1)
   read_results=i2c.transaction(reading(address,37))
   print(read_results)
   ecmdString = []
   print ("---------")

   ecmd = "1w convert 281efeeb020000c0"
   for ecmdChar in ecmd:
    ecmdString.append(ord(ecmdChar))
   i2c.transaction(writing(address,ecmdString))
   print (ecmd)
   print (ecmdString)
   sleep(1)
   read_results=i2c.transaction(reading(address,37))
   print(read_results)
   ecmdString = []
   print ("---------")

   ecmd = "1w get 281efeeb020000c0"
   for ecmdChar in ecmd:
    ecmdString.append(ord(ecmdChar))
   i2c.transaction(writing(address,ecmdString))
   print (ecmd)
   print (ecmdString)
   sleep(1)
   read_results=i2c.transaction(reading(address,37))
   print(read_results)
   ecmdString = []
   print ("---------")


   ecmd = "hostname"
   for ecmdChar in ecmd:
    ecmdString.append(ord(ecmdChar))
   i2c.transaction(writing(address,ecmdString))
   print (ecmd)
   print (ecmdString)
   sleep(1)
   read_results=i2c.transaction(reading(address,37))
   print(read_results)
   ecmdString = []
   print ("---------")

