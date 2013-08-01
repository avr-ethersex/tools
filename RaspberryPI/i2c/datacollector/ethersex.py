import quick2wire.i2c as i2c
from quick2wire.i2c import I2CMaster, writing, reading
from time import sleep

address = 0x04

def get_temperature():
        i2c_cmd("1w convert 281efeeb020000c0")
        return ("281efeeb020000c0",i2c_cmd("1w get 281efeeb020000c0"))

def get_version():
        return i2c_cmd("version")

def get_hostname():
        return i2c_cmd("hostname")

def i2c_cmd(value):
        try:
                ecmd=value
                ecmdString=[]
                i=0
                ret_val=""

                for ecmdChar in ecmd:
                        ecmdString.append(ord(ecmdChar))

                with I2CMaster() as i2c:
                        i2c.transaction(writing(address,ecmdString))
                        sleep(.9)
                        i2c_results=i2c.transaction(reading(address,50))[0]

                while i2c_results[i] > 0 :
                        ret_val=ret_val+(chr(i2c_results[i]))
                        i+=1

                return ret_val
        except:
                print("i2c failed")
