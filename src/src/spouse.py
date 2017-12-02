# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Holds information about target's spouse

class Spouse(object):
 ''' Holds information about target's spouse '''

 def __init__(self):
  super(Spouse, self).__init__()

 @property
 def spouse_info(self):
  for name in self.cases(self.info['spouse_firstname']) + self.cases(self.info['spouse_nickname']):
   yield name
   [(yield _) for _ in self.combine(name, self.info['spouse_year_of_birth'])]
