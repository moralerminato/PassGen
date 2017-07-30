# Date: 06/19/2017
# Author: Ethical-H4CK3R
# Description: Generates possible passwords
#
# imports
import os
import sys
import time
import urllib2
import subprocess

# current version
__version__ = 0.2

class Update(object):
 def __init__(self):
  self.vers = __version__
  self.html = None # src code
  self.file = '.code.txt' # hidden file for reading for updates
  self.code = 'https://raw.githubusercontent.com/Ethical-H4CK3R/PassGen/master/passGen.py'

 def check(self):
  print 'Checking for an update ...'
  try:self.open()
  except:
   subprocess.call(['clear'])
   raw_input('Unable to update, please check your connection\n\n[Press Enter To Continue]')
   return
  self.fetch()
  self.read()
  self.remove()

 def remove(self):
  os.remove(self.file)

 def open(self):
  self.html = urllib2.urlopen(self.code).read()

 def fetch(self):
  with open(self.file,'w+') as fwrite:
   fwrite.write(self.html)

 def read(self):
  with open(self.file,'r') as fread:
   for line in fread:
    line = line.replace('\n','').split()
    if line:
     if line[0] == '__version__':
      try:
       if eval(line[2]) > self.vers:
        subprocess.call(['clear'])
        update = raw_input('Found an update, would you like to install it?\n\nEnter (y/n): ')
        if update:
         if update[0].lower() == 'y':self.update()
         return
      except:pass
   else:
    subprocess.call(['clear'])
    raw_input('No updates found\n\n[Press Enter To Continue]')

 def update(self):
  with open(sys.argv[0],'w') as fwrite:
   fwrite.write(self.html)
  subprocess.call(['clear'])
  raw_input('Restart program to install updates\n\n[Press Enter To Continue]')

class Generator(object):
 def __init__(self):
  self.name  = None
  self.list  = [] # holds numbers, don't mix with numbers or symbols
  self.word  = [] # holds words, mix with numbers and symbols
  self.file  = [] # the passwords to write
  self.symb  = ['!@#','!','@','#','!!!']
  self.nums  = [123,1234,143,1,2,3,69,6969,420,111,123456,321,12,23,24,34,2468]

 def now(self):
  return time.strftime('%m-%d-%Y_%I:%M:%S',time.localtime())

 def cases(self,word):
  # firstname, Firstname, FIRSTNAME
  return word.lower(),word,word.upper()

 def numbers(self,word):
  # firstname123
  return ['{}{}'.format(''.join(word),num) for word in self.cases(word) for num in self.nums]

 def symbols(self,word):
  # firstname!@#
  return ['{}{}'.format(''.join(word),sym) for word in self.cases(word) for sym in self.symb]

 def comb(self,word):
  # firstname123!@#
  return ['{}{}{}'.format(''.join(word),num,sym) for word in self.cases(word) for num in self.nums for sym in self.symb]

 def default(self,essid,bssid):
  # default passkey on routers
  return '{}{}{}'.format(essid[:-2],''.join([k for i,k in enumerate(bssid) if any([i==9,i==10,i==12,i==13])]),essid[-2:])

 def writefile(self):
  self.name = 'wordlist-{}.lst'.format(self.now())
  with open(self.name,'w') as fwrite:
   for item in self.file:
    fwrite.write('{}\n'.format(item))

 def generate(self):
  print 'Generating ...'
  [self.file.append(_) for _ in self.list if _]
  for word in self.word:
   # generate passwords
   self.file.append(word)
   self.file = self.file + [num for num in self.numbers(word) if not num in self.file] # words & numbers
   self.file = self.file + [sym for sym in self.symbols(word) if not sym in self.file] # words & symbols
   self.file = self.file + [comb for comb in self.comb(word) if not comb in self.file] # words, numbers, & symbols
  self.writefile()

class Questions(object):
 def __init__(self):
  self.vends = ['TG1','DVW','DG8','U10','TC8']
  self.questions = {

            # target info
            'firstname':None,
            'middlename':None,
            'lastname':None,
            'nickname':None,
            'yearOfBirth':None,

            # child info
            'childFN':None,
            'childMN':None,
            'childLN':None,
            'childYOB':None,
            'childNN':None,

            # spouse info
            'spouseFN':None,
            'spouseMN':None,
            'spouseLN':None,
            'spouseYOB':None,
            'spouseNN':None,

            # pet info
            'petname':None,
            'petYOB':None,

            # numbers
            'ssn':None,
            'pin':None,
            'phone':None,

            # wifi info
            'essid':None,
            'bssid':None

              }

 def cmds(self):
  # help
  print 'usage: [fieldname] = [value]'
  print '*Do Not Use Any Symbols\n'
  print 'help              \tdisplay help'
  print 'exit              \tto exit'
  print 'reset             \tclear fields'
  print 'update            \tcheck for update'
  print 'generate          \tgenerate password list'
  print 'current version   \t{}'.format(__version__)
  raw_input('\n[Press Enter To Continue]')

 def mklist(self):
  for q in self.questions:
   v = self.questions[q]
   n = q

   if v:
    # are we looking at a pin
    if n=='pin':
     generator.nums.append(v)
     generator.list.append(v)

    # are we looking at wifi info
    elif n == 'essid' or n == 'bssid':
      if n != 'essid':continue
      essid = v
      bssid = [key for key in self.questions if key == 'bssid']
      bssid = bssid[0] if bssid else bssid
      if not bssid:continue
      bssid = self.questions[bssid]

      # generate default password
      if len(essid)>3:
       if essid[:3] in self.vends:
        passkey = generator.default(essid,bssid)
        if not passkey in generator.list:
         generator.list.append(passkey)

    # full name
    elif n == 'firstname':
     firstname,lastname = v,self.questions['lastname']
     generator.word.append(firstname)

     if lastname:
      generator.word.append('{}{}'.format(firstname,lastname.lower()))
      generator.word.append('{}{}'.format(firstname,lastname))

    elif n == 'spouseFN' or n == 'childFN':
     # love makes people weak
     generator.word.append(v)
     generator.word.append('ilove{}'.format(v))
     generator.word.append('love{}'.format(v))
     generator.word.append('iloveU{}'.format(v))
     generator.word.append('mylove{}'.format(v))
     generator.word.append('{}143'.format(v))

    # are we looking basic info
    else:
     if v.isdigit():
      if any([n=='yearOfBirth',n=='spouseYOB',n=='childYOB','petYOB']):
       rev  = ''.join([n for n in reversed([n for n in v])])
       end  = v[-2:]

       # different formats of year
       if not v in generator.nums:
        generator.nums.append(v)
       if not rev in generator.nums:
        generator.nums.append(rev)
       if not end in generator.nums:
        generator.nums.append(end)

      else:
       if not v in generator.list:
        generator.list.append(v)
     else:
      if not v in generator.word:
       generator.word.append(v)

  # generate password list & reset
  generator.generate()
  self.reset()

 def fresh(self):
  # fresh start ?
  return False if [_  for _ in self.questions if self.questions[_]] else True

 def display(self):
  subprocess.call(['clear'])
  for n,q in enumerate(self.questions):
   if not n:
    print '-------------------------------'
    print '||    Name     ||    Value   ||'
    print '-------------------------------'
   n,v = q.ljust(11),str(self.questions[q]).ljust(7)
   print '|| {} || {}'.format(n,v)
  passwords = len(generator.file)
  if passwords:
   print '\nGenerated: {}\nSize: {}'.format(generator.name,passwords)

 def reset(self,item=None):
  del generator.list[:]
  del generator.word[:]
  for q in self.questions:
   self.questions[q] = None

def main():
 while 1:
  answers.display()
  if not generator.file:
   print '\ntype: \'help\' for help' if answers.fresh() else ''
  if generator.file:
   del generator.file[:]
  cmd = raw_input('\n> ')
  subprocess.call(['clear'])

  # check for assignments
  if '=' in cmd:
   try:
    name = cmd.split()[0].lower().strip().replace('\n','')
    value = cmd.split()[2].lower().strip().replace('\n','')
   except:continue
   key = [_ for _ in answers.questions if _.lower() == name.lower()]
   if not key:continue
   key = key[0]
   if key != 'bssid' and key != 'essid':
    answers.questions[key] = str(value).title()
   else:
    answers.questions[key] = str(value).upper()

  else:
   # check for key words, such as help, reset, and generate
   cmd = cmd.lower()
   [answers.cmds() if cmd=='help' else answers.reset() if cmd=='reset' else answers.mklist() if cmd=='generate' else exit() if cmd=='exit' else Update().check() if cmd=='update' else None]


if __name__ == '__main__':
 answers = Questions()
 generator = Generator()
 try:
  main()
 except KeyboardInterrupt:
  exit('\n')
