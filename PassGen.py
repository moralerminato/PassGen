#!/usr/bin/env python
#
#  Generate Possible Passwords
# 

class Generator(object):
 def __init__(self,name):
  self.name  = self.filter(name)
  self.keys  = []
  self.list  = ''
  self.nums  = [1,2,3,4,5,6,7,12,24,34,69,123,143,420]
  self.com   = ['mustang','dragon','baseball','football',
                'money','monkey','shadow','master','soccer',
                'jordan','love','iloveyou','iloveU','mylove']
 
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
