# Date: 11/30/2017
# Author: Ethical-H4CK3R
# Description: Handles Updates

import os
import time
import shutil

from zipfile import ZipFile
from requests import get as urlopen

class Update(object):

 def __init__(self):
  self.dir = '.passGen.zip'
  super(Update, self).__init__()

  # repo links
  self.repo = 'https://github.com/Ethical-H4CK3R/PassGen/archive/master.zip'
  self.script = 'https://raw.githubusercontent.com/Ethical-H4CK3R/PassGen/master/passGen.py'

 @property
 def is_online(self):
  try:return urlopen('https://github.com').ok
  except:
   self.display_msg('Error: Connection failure', -1)
   return

 @property
 def online_version(self):
  try:
   code = urlopen(self.script).text
   return eval(code.split()[code.split().index('__version__')+2])
  except:return

 def download(self):
  with open(self.dir, 'wb') as f:
   try:f.write(urlopen(self.repo).content)
   except:
    self.display_msg('Error: Failed to download', -1)
    return
   return True

 def unzip(self):
  with ZipFile(self.dir, 'r') as zipfile:
   try:zipfile.extractall(os.path.splitext(self.dir)[0])
   except:
    self.display_msg('Error: Failed to unzip', -1)
    os.remove(self.dir)
    return
   return True

 def extract(self):
  # remove
  try:os.remove(self.dir)
  except:pass

  # set path
  fldr = os.path.splitext(self.dir)[0] + \
  os.path.sep + os.listdir(os.path.splitext(self.dir)[0])[0]

  # extract
  for item in os.listdir(fldr):
   item = fldr + os.path.sep + item
   destin = self.path + os.path.sep + os.path.basename(item)

   # move
   if os.path.isfile(item):shutil.copyfile(item, destin)
   else:shutil.copytree(item, destin)

  # remove
  shutil.rmtree(os.path.splitext(self.dir)[0])
  self.display_msg('Restart the program to install update', 1)

 def update(self):
  print '\n Searching for an update ...'
  time.sleep(1.5)

  # test connection
  if not self.is_online:return
  online_version = self.online_version

  # compare versions
  if online_version > self.version:
   self.clear
   print '\n Newer Version: {}\n Current Version: {}'.\
   format(online_version, self.version)

   # get permission
   try:
    if raw_input('\n Do you want to continue? [Y/n]: ')[0].lower() == 'y':
     self.install_update()
   except:return
  else:self.display_msg('No updates found', 0)

 def install_update(self):
  if not self.download():return
  if not self.unzip():return
  self.extract()
