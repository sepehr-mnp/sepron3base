import hashlib
import struct
def hsh32(text):
    return hashlib.blake2s(text.encode(), digest_size=16).hexdigest()
def double_to_hex(f):
    return hex(struct.unpack('<Q', struct.pack('<d', f))[0])
def hx(inp):
    s = float(inp)
    s = str(inp)
    poslist = [pos for pos, char in enumerate(s) if char == "."]
    if(len(poslist)>1):
        return "invalid!"
    else:
        poslist = poslist[0]
        return str(s[0:poslist])+"p"+str(s[poslist:])
 
