#!/usr/bin/python
'''
num=input("enter the number:")
#print num
x=y=z=num
if(x<=20):
 print x
elif num>20:
     print x
#    if(num<30):
#     print "number lessthan 30"   
else:
    a,b,c=12,342,'hello'
    print (a,b,c)
'''

#list
planets=["mercury","jupiter","earth","mars",12,'chenna']
planets[2]='saturn'
print planets
#print planets[1][0:2]
#print planets[3:]
#print planets[-1]

planets.append("reddy")
planets.insert(3,'chennaaaaaaa')
print planets
#tuples

tuples=("mercury","jupiter","earth","mars",12,'chenna')
#print tuples

print tuples[1]
print tuples[-1]

print tuples
#dictionary

dict={'course':'devops',1:'linux','rbi':'public','sbi':['sbm','sbt']}
print dict
print dict['course']
print dict['sbi'][0][0:2]
dict['sdf']='era'
print dict
