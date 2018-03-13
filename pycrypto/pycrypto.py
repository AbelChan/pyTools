#coding: utf8
import sys

import fileUtil
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():
	def __init__(self, key):
		self.key = key
		self.mode = AES.MODE_CBC

	def encrypt(self, text):
		#加密方法
		cryptor = AES.new(self.key, self.mode, self.key)
		length = 16
		count = len(text)
		add = length - (count % length)
		text = text + ('\0' * add)
		self.ciphertext = cryptor.encrypt(text)

		return b2a_hex(self.ciphertext)

	def decrypt(self, text):
		#解密方法
		cryptor = AES.new(self.key, self.mode, self.key)
		plain_text = cryptor.decrypt(a2b_hex(text))
		return plain_text.rstrip('\0')

	def encryptfile(self, fileName):
		#加密文件
		str = fileUtil.readfile(fileName)
		password = self.encrypt(str)
		fileUtil.writefile(fileName, password)

	def decryptfile(self, fileName):
		#解密文件
		str = fileUtil.readfile(fileName)
		password = self.decrypt(str)
		fileUtil.writefile(fileName, password)