#!/usr/bin/python3

import MySQL
import ethersex as ecmd
from time import sleep

hostname=ecmd.get_hostname()
version=ecmd.get_version()

print("Data collector i2c\n")
print("------------------\n")
print(hostname,version)


while True :
        sensor_id,temperature=ecmd.get_temperature()
        database.insert_temperature(sensor_id,temperature)
