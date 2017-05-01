#!/usr/bin/env python

from PIL import Image
from optparse import OptionParser
import glob, os, re, shutil

parser = OptionParser("Usage: %prog source-directory [options]")
filepattern = re.compile("([^\s]+(\.(jpeg|jpg|png|gif|bmp))$)")

#parser.add_option("-d", "--directory", dest="directory", help="Directory containing image files")
parser.add_option("-l", "--landscape", dest="landscape_dir", help="Directory to add landscape photos to")
parser.add_option("-p", "--portrait", dest="portrait_dir", help="Directory to add portrait photos to")
parser.add_option("-s", "--square", dest="square_dir", help="Directory to add square photos to")

(options, args) = parser.parse_args()

if(len(args) >= 1):
  os.chdir(args[0])

for f in os.listdir(args[0]):
  if(not filepattern.match(f)):
    continue

  image = Image.open(f)
  width,height = image.size

  if(width > height): #landscape
    if(options.landscape_dir is not None):
      shutil.copy(args[0] + "/" + f, options.landscape_dir)
    
    
  if(width < height): #portrait
    if(options.portrait_dir is not None):
      shutil.copy(args[0] + "/" + f, options.portrait_dir)

  if(width == height): #square
    if(options.squre_dir is not None):
      shutil.copy(args[0] + "/" + f, options.square)
      
