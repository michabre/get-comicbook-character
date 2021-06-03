import hashlib
from datetime import datetime
import calendar

#
# Generate Hash based on the recommended method
# from: https://developer.marvel.com/documentation/authorization
#
def generateHash(timestamp, privateKey, publicKey):
  hash_string = timestamp + privateKey + publicKey
  return hashlib.md5(str.encode(hash_string)).hexdigest()


#
# Return Unix Timestamp as a string
#
def getUnixTimestamp():
  d = datetime.utcnow()
  unixtime = calendar.timegm(d.utctimetuple())
  return str(unixtime)