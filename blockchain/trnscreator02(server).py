import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p

privKey = input("Enter your private key: ")
amount = int(input("Amount: "))
to = input("Who are you sending sepcoin to: ")
fee = int(input("Fee: "))
blocknum = int(input("Block Num: "))

privKey =eth_keys.keys.PrivateKey(binascii.unhexlify(str(privKey)))
pubKey = privKey.public_key
address = pubKey.to_checksum_address()
#msg = b'Message for signing'
msg = (address+str(hex(amount))+str(to)+str(hex(fee))+str(hex(blocknum))).encode('UTF-8')
signature = privKey.sign_msg(msg)
print(signature)
print("?sign="+str(signature)+"&address="+address+"&amount="+str(hex(amount))+"&to="+str(to)+"&fee="+str(hex(fee))+"&blocknum="+str(hex(blocknum)))
