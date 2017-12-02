# Date: 12/01/2017
# Author: Ethical-H4CK3R
# Description: Queue that prevents duplicates

class Queue(object):
 ''' A queue that prevents duplicates '''

 def __init__(self):
  self.queue = []

 def qsize(self):
  return len(self.queue)

 def put(self, item):
  if not item in self.queue:
   self.queue.append(item)

 def get(self):
  if not self.queue:return
  item = self.queue[0]
  del self.queue[0]
  return item
