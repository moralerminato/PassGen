# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Holds the numbers that will be used

from time import ctime 

class Numbers(object):
 ''' Holds commonly used numbers '''

 def __init__(self):
  super(Numbers, self).__init__()

 @property
 def zero_nums(self):
  # 09, 10
  return ['{:02}'.format(_) for _ in range(1, 13)]

 @property
 def _zero_nums(self):
  # 09, 010
  return ['0{}'.format(_) for _ in range(1, 13)]

 @property
 def nums(self):
  # 1, 2
  return [_ for _ in range(13)]

 @property
 def common_nums(self):
  year = eval(ctime().split()[-1])
  return [123, 321, 111, 143, 420, 69, 619, 1234, 123456, year, year-1, year-2]

 @property
 def _common_nums(self):
  # 0123, 0143
  return ['0{}'.format(_) for _ in self.common_nums]

 @property
 def numbers(self):
  return self.common_nums + self._common_nums + list(set(self.nums + self.zero_nums + self._zero_nums))
