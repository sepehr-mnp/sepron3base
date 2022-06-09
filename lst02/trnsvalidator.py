import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p
import sys,adder,messageadder


lisinp = input()

lisinp = lisinp.split("!")
print(lisinp)

signature = lisinp[0]
fromadd = lisinp[1]
amount = lisinp[2]
to = lisinp[3]
fee = lisinp[4]
blocknum = lisinp[5]
'''

signature = sys.argv[1]
fromadd = sys.argv[2]
amount = sys.argv[3]
to = sys.argv[4]
fee = sys.argv[5]
blocknum = sys.argv[6]
'''

msg = (fromadd + amount + to + fee + blocknum).encode("UTF-8")
msgSigner = fromadd
signature = eth_keys.keys.Signature(binascii.unhexlify(signature[2:]))
signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
valid = signerRecoveredAddress == msgSigner
print('Signature valid?:', valid)
print('signer balance' ,adder.balance(signerRecoveredAddress))
if(valid):
    messageadder.add(fromadd,to,amount,fee)
