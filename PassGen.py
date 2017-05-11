#!/usr/bin/env python
#
#  Generate Possible Passwords
# 

class Generator(object):
 def __init__(self,name):
  self.name  = self.filter(name)
  self.keys  = []
  self.list  = ''
  self.nums  = [123,1234,143,1,2,3,69,6969,420,111,123456,321,'!@#','!','@','#']
  self.com   = ['shadow','love','iloveyou','iloveU','password','p@ssword','p@ssw0rd','admin']
  
 def toFile(self):
  with open('Pass.lst','w+') as file:
   file.write(self.list)

 def filter(self,text):
  return text.replace('\n','')

 def read(self):
  for passwrd in self.keys:
   yield '{}\n'.format(passwrd) 

 def generate(self,text,num):  
  self.keys.append('{}{}'.format(text.lower(),num))
  self.keys.append('{}{}'.format(text.title(),num)) 
  #
  self.keys.append('{}.{}'.format(text.lower(),num))  
  self.keys.append('{}.{}'.format(text.title(),num))
    
 def ai(self):
  for num in self.nums:
   self.generate(self.name,num)
  
  for text in self.com:
   self.keys.append('{}'.format(text))
   for num in self.nums:
    self.generate(text,num)

  for key in self.read():
   self.list=self.list+key
  self.toFile() 

if __name__ == '__main__':
 name = raw_input('Enter name: ')
 Generator(name).ai()
