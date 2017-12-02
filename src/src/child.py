# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Holds information about target's baby

class Child(object):
 ''' Holds information about target's baby '''

 def __init__(self):
  super(Child, self).__init__()

 @property
 def child_info(self):
  for name in self.cases(self.info['child_firstname']) + self.cases(self.info['child_nickname']):
   yield name
   [(yield _) for _ in self.combine(name, self.info['child_year_of_birth'])]
