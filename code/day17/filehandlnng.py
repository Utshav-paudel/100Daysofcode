#read mode
file1=open('test.txt','r')
print(file1.read())
file1.close()

#write mode
file1=open('test.txt','w')
file1.write('this is added by write method ')  #this will overwrite previous data from test.txt
file1.close()

#append mode
file1=open('test.txt','a')
file1.write('append mode add it doesnot overwrite')
file1.close()