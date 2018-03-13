#coding=utf-8

import fileUtil
from pycrypto import prpcrypt

def readKey():
	key = fileUtil.readfile("key.ac")
	return key

def encryptfile():
	#加密
	pc = prpcrypt(readKey())
	pc.encryptfile("word.ac")

def decryptfile():
	#解密
	pc = prpcrypt(readKey())
	pc.decryptfile("word.ac")

encryptfile()