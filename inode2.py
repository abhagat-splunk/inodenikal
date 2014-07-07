import os,sys,time
class inodeni(object):
	def __init__(self):
		global path
		paths= raw_input("Enter the path")
		os.chdir(paths)
		listkar= os.listdir(paths)
		print "Listing the files.."
		for file in listkar:
			print file
	def getInode(self):
		x = raw_input("Enter the name of the file you want to find the information about:\n>")
		global ankit		
		ankit = os.stat(x)
		
	def printdet(self):
		global ankit
		print "1. Inode Number is: ",ankit.st_ino
		print "2. User ID is:  ",ankit.st_uid
		print "3. Group ID is  ",ankit.st_gid
		print "4. Size of the file in bytes is: ",ankit.st_size
		print "5. Modify Time is:  ",time.ctime(ankit.st_mtime)
		print "6. Access time is:  ",time.ctime(ankit.st_atime)
		print "7. Mode is:  ",ankit.st_mode
		print "8. Block Size: ",ankit.st_blksize
		print "9. Device ID is: ",ankit.st_dev
		print "10. Link type is: ",ankit.st_nlink
		
xy = inodeni()
xy.getInode()
xy.printdet()

		
