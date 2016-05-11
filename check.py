import hashlib
import sys


def getmd5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

if sys.argv[2] == getmd5(sys.argv[1]):
    print("MD5 Checksum passed.")
else:
    print("MD5 Checksum failed. Incorrect MD5.")
exit
