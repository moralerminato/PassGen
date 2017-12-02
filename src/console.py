# Date: 11/30/2017
# Author: Ethical-H4CK3R
# Description: Interactive Console

from os import system as shell
from platform import system as distro

class Console(object):
 ''' Interactive '''

 def __init__(self):
  self.is_alive = True
  super(Console, self).__init__()
  self.clear_cmd = 'cls' if distro() == 'Windows' else 'clear'

  # colors
  self.red = '\033[31m'
  self.null = '\033[0m'
  self.blue = '\033[34m'
  self.green = '\033[32m'
  self.yellow = '\033[33m'

  # display art
  self.symbols = {
   'fail': {'symbol': '!', 'color': self.red},
   'caution': {'symbol': '-', 'color': self.blue},
   'success': {'symbol': '+', 'color': self.green},
  }

  self.cmds = {
  'set': {'cmd': self.set, 'help': 'to assign a value'},
  'exit': {'cmd': self.exit, 'help': 'to terminate the script'},
  'help': {'cmd': self.help, 'help': 'to display this menu'},
  'reset': {'cmd': self.reset, 'help': 'to reset all of the fields'},
  'update': {'cmd': self.update, 'help': 'to update to a newer version'},
  'generate': {'cmd': self.generate, 'help': 'to generate a new password list'},
  }

  self.info = {
   'lastname': None,
   'firstname': None,
   'streetname': None,
   'favorite_team': None,
   'year_of_birth': None,

   'child_nickname': None,
   'child_firstname': None,
   'child_year_of_birth': None,

   'spouse_firstname': None,
   'spouse_nickname': None,
   'spouse_year_of_birth': None,
  }

  # press enter to continue
  self.enter = '\n Press {0}[{1}Enter{0}]{1} To Continue\n '.\
  format(self.green ,self.null)

 @property
 def clear(self):
  shell(self.clear_cmd)

 def display_msg(self, msg, code):
  self.clear
  symbol = self.symbols['fail' if code == -1 else 'caution' if not code else 'success']
  symbol = '{}{}{}'.format(symbol['color'], symbol['symbol'], self.null)

  # display message
  art = '{0}[{1}{0}]{2}'.format(self.yellow ,symbol, self.null)
  msg = ' {} {}\n{}'.format(art, msg, self.enter)
  try:raw_input(msg)
  except:return

 def display(self):
  self.clear
  print ' {0}\n || Name    {1}{1}||{1}{1}    Value ||\n {0}'.format('.'*45,''.ljust(5))

  for k in sorted(self.info, key=len):
   if self.info[k]:
    print ' || {}{}{}{}{}'.format(k, ''.ljust(34-len(k)%34), self.blue, self.info[k], self.null)
   else:print ' || {}{}{}{}{}'.format(k, ''.ljust(34-len(k)%34), self.red, self.info[k], self.null)
  print

 def help(self):
  self.clear
  print '\n Usage: {}set {}fieldname {}value{}\n'.format(self.blue, self.yellow, self.green, self.null)
  for key in sorted(self.cmds, key=len):
   print ' {}{}{}{}{}'.format(key, ''.ljust(10-len(key)%10), self.green, self.cmds[key]['help'], self.null)
  print ' version:  {}{}{}'.format(self.yellow, self.version, self.null)
  raw_input(self.enter)

 def reset(self):
  for _ in self.info:self.info[_] = None
  self.display()

 def exit(self):
  self.is_alive = False

 @property
 def is_empty(self):
  return False if any([self.info[_] for _ in self.info]) else True

 def set(self, key, value):
  if not key in self.info:return
  self.info[key] = value

 def console(self):
  while self.is_alive:
   try:
    self.display()
    print '\n type {}help{} for help'.\
    format(self.yellow, self.null) if self.is_empty else ''
    cmd = raw_input(' > ').lower().split()
    if not cmd:continue

    if cmd[0] in self.cmds:
     if all([cmd[0] == 'set', len(cmd) == 3]):
      if all([cmd[1] in self.info, cmd[2]]):
       self.cmds['set']['cmd'](cmd[1], cmd[2].title())
     else:self.cmds[cmd[0]]['cmd']()
   except KeyboardInterrupt:self.exit()
   except:pass
