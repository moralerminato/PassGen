# Date: 11/30/2017
# Author: Ethical-H4CK3R
# Description: Generator

from src.target import Target

from time import sleep
from queue import Queue
from src.numbers import Numbers
from os.path import splitext
from itertools import permutations as permute

class Generator(Target):

 def __init__(self):
  self.numbers = Numbers()
  self.passwords = Queue()
  super(Generator, self).__init__()
  self._symbols = ['!', '@', '#', '$']

 def permutate(self, samples):
  return [''.join([str(_) for _ in _]) for _ in list(permute(samples))]

 def name_formats(self, fn, ln):

  # mkevin, Mkevin, mKevin, MKevin
  yield fn[0] + ln
  yield fn[0].upper() + ln
  yield fn[0] + ln.title()
  yield fn[0].upper() + ln.title()

  # kevinm, kevinM, Kevinm,  KevinM
  yield ln + fn[0]
  yield ln + fn[0].upper()
  yield ln.title() + fn[0]
  yield ln.title() + fn[0].upper()

 def cases(self, word):
  if not word:return []
  return [word.lower(), word.title()]

 def combine(self, name, byear=[]):
  if not isinstance(byear, list):
   if byear:byear = byear.split()
   else:byear = []

  # mike123
  for num in byear + self.numbers.numbers:
   [(yield _) for _ in self.permutate([name, num])]

  # mike!
  for sym in self._symbols:
   [(yield _) for _ in self.permutate([name, sym])]

  # 123mike!
  for num in byear + self.numbers.numbers:
   for sym in self._symbols:
    [(yield _) for _ in self.permutate([name, num]) for _ in self.permutate([_, sym])]

 def generate(self):
  if self.is_empty:return
  print '\n Generating ...';sleep(1.5)
  [self.passwords.put(_) for _ in self.target_info]
  [self.passwords.put(_) for _ in self.spouse_info]
  [self.passwords.put(_) for _ in self.child_info]
  [self.passwords.put(_) for _ in self.pet_info]
  self.create()
