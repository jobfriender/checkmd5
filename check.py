import hashlib
import sys


def getmd5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

file = input("Enter file name:")
md5 = input("Enter md5 checksum to compare:")

if md5 == getmd5(file):
    print("MD5 Checksum passed.")
else:
    print("MD5 Checksum failed. Incorrect MD5.")
exit
