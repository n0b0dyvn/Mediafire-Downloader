import urllib
import sys
import os
import string
import subprocess

### Function to use
def Usage():
	print "python2 main.py <link>"

### Begin with Check Link
try:
	urlDownload	=	sys.argv[1]
except IndexError:
	print "URL is wrong"
	Usage()
	sys.exit(0)
except ValueError:
	print urlDownload,"is deadlink."
	Usage()
	sys.exit(0)
### Main of program
try:
	#os.chdir('/home/n0b0dy/Download/')
	if "http://" not in urlDownload:
		urlDownload	=	"http://"+urlDownload		
	link		=	urllib.urlopen(urlDownload)
	link		=	str(link.read())
	name		=	link[link.index("<title>")+len("<title>"):link.index("</title>")]

	### if in name have space , remove space
	if " " in name:
		name	=	string.replace(name," ","+")
	
	### locate your download link
	lastIndexofDownload		=	link.index("/"+name)	+	len(name)	+	1
	subLink					=	link[:lastIndexofDownload]
	linkDownload			=	subLink[subLink.rfind("http://"):]
	print "Downloading",linkDownload
	p	=	subprocess.Popen(["wget", linkDownload])
	print 
except IndexError:
	print "URL is wrong"
	Usage()
