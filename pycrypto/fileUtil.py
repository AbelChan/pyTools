#coding=utf-8
import os

def readfile(fileName):
	fp = open(fileName)
	str = fp.read()
	fp.close()
	return str

def readlines(fileName):
	fp = open(fileName)
	lines = fp.readlines()
	fp.close()
	return lines

def writefile(fileName, str):
	fp = open(fileName, 'w')
	fp.write(str)
	fp.close()

def getFiles(rootdir, regex=None):
	files = list()
	for parent, dirnames, filesnames in os.walk(rootdir):
		for filename in filesnames:
			fullPath = os.path.join(parent, filename)
			if(not regex) or regex.match(fullPath):
				files.append(fullPath)
	return files

def getFileNames(rootdir):
	names = list()
	for parent, dirnames, filesnames in os.walk(rootdir):
		for filename in filesnames:
			names.append(filename)
	return names


