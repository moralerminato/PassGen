# Date: 11/30/2017
# Author: Ethical-H4CK3R
# Description: Generates Possible Passwords

from os import getcwd, path
from platform import system
from src.update import Update
from src.console import Console
from src.generate import Generator

# current version
__version__ = 0.33

class PassGen(Update, Console, Generator):

 def __init__(self):
  self.version = __version__
  super(PassGen, self).__init__()
  self.path = path.dirname(__file__) if system() == 'Windows' else getcwd()

 def create(self):
  size = self.passwords.qsize()
  name = path.abspath('{}/pass.lst'.format(self.path))

  with open(name, 'w') as f:
   while self.passwords.qsize():
    pwd = self.passwords.get()
    f.write(pwd + '\n' if self.passwords.qsize() else pwd)
  self.display()
  raw_input('\n Generated: {}\n Lines: {}\n{}'.format(name, size, self.enter))

if __name__ == '__main__':
 PassGen().console()
