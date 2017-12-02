# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Holds information about target's pet

class Pet(object):
 ''' Holds information about target's pet '''

 def __init__(self):
  super(Pet, self).__init__()

  self.pet_name = None
  self.pet_year_of_birth = None

 @property
 def pet_info(self):
  for name in self.cases(self.pet_name):
   yield name
   [(yield _) for _ in self.combine(name, self.pet_year_of_birth)]
