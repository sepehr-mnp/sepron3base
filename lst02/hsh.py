import sys
import hashlib
def hsh(strr):
    encoded_str = strr.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_str)
    return obj_sha3_256.hexdigest()
