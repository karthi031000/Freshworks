import threading 
from threading import*
import time
d={} # d is a dictionary used to store key-value datastore

# Create operation

def create(key,value,timeout=0):
    if key in d:
        print("error: Key already exist")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")


# Read operation
def read(key):
    if key not in d:
        print("error: Key doesn't exist. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                print(stri)
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

# Delete operation

def delete(key):
    if key not in d:
        print("error: key doesn't exist. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
                print("key successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key",key,"successfully deleted")
