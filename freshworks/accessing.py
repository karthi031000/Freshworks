
import code as c
# importing the code file as a library 


c.create("karthi",25)# to create a key with no time-to-live property


c.create("lee",70,5) # to create a key with time-to-live property


c.read("karthi")# it returns the value of the respective key in Jasonobject format 'key_name:value'

c.read("lee")# it returns the value of respective key in jasonobject format if time-to-live property is not expired else it returns error message

c.delete("karthi")#it deletes the key and its value from datastore

#we can access the code using multi-thread by following code

t1=c.threading.Thread(target=c.create,args=("karthi",21,))
t1.start()
t2=c.threading.Thread(target=c.read,args=("lee",))
t2.start()
