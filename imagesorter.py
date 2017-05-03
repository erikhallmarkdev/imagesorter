#!/usr/bin/env python

from PIL import Image
from optparse import OptionParser
import os, re, shutil, sys

parser = OptionParser("Usage: %prog source-directory [options]")
filepattern = re.compile("([^\s]+(\.(jpeg|jpg|png|gif|bmp))$)", re.IGNORECASE)

parser.add_option("-l", "--landscape", dest="landscape_dir", help="Directory to add landscape photos to")
parser.add_option("-p", "--portrait", dest="portrait_dir", help="Directory to add portrait photos to")
parser.add_option("-s", "--square", dest="square_dir", help="Directory to add square photos to")

(options, args) = parser.parse_args()

i = 0

files = os.listdir(os.path.abspath(args[0]))

#Credit for the progess bar goes to https://gist.github.com/vladignatyev/06860ec2040cb497f0f3

def progress(count, total, status=''):
  bar_len = 60
  filled_len = int(round(bar_len * count / float(total)))

  percents = round(100.0 * count / float(total), 1)
  bar = '=' * filled_len + '-' * (bar_len - filled_len)

  sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
  sys.stdout.flush() 


for f in files:
  if(not filepattern.match(f)):
    continue

  image = Image.open(os.path.abspath(args[0]) + "/" + f)
  width,height = image.size

  progress(i, len(files), '')

  i = i + 1

  if(width > height): #landscape
    if(options.landscape_dir is not None):
      shutil.copy(os.path.abspath(args[0]) + "/" + f, os.path.abspath(options.landscape_dir))
    
    
  if(width < height): #portrait
    if(options.portrait_dir is not None):
      shutil.copy(os.path.abspath(args[0]) + "/" + f, os.path.abspath(options.portrait_dir))

  if(width == height): #square
    if(options.squre_dir is not None):
      shutil.copy(os.path.abspath(args[0]) + "/" + f, os.path.abspath(options.square))

print('')
