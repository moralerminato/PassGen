# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Holds target's information

from pet import Pet
from child import Child
from spouse import Spouse

class Target(Pet, Child, Spouse):
 ''' Holds information about the target '''

 def __init__(self):
  super(Target, self).__init__()

 @property
 def target_info(self):
  # kevin123
  for name in self.cases(self.info['firstname']) + self.cases(self.info['lastname']):
   yield name
   [(yield _) for _ in self.combine(name, self.info['year_of_birth'])]

  # kevinM123
  if all([self.info['firstname'], self.info['lastname']]):
   for name in self.name_formats(self.info['firstname'], self.info['lastname']):
    yield name
    [(yield _) for _ in self.combine(name, self.info['year_of_birth'])]

  # main123
  for name in self.cases(self.info['streetname']):
   yield name
   [(yield _) for _ in self.combine(name, self.info['year_of_birth'])]

  # 2015Giants!
  for name in self.cases(self.info['favorite_team']):
   yield name
   [(yield _) for _ in self.combine(name)]
