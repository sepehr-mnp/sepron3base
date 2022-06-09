import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p
import sys,adder,messageadder,json
'''
with open("blocks/00chaininf.json",'r') as file:
                        jsondata = json.load(file)
                        blocknumjsn =jsondata['blocknum']
                        file.seek(0)

lisinp = input()

lisinp = lisinp.split("!")
print(lisinp)

signature = lisinp[0]
fromadd = lisinp[1]
amount = lisinp[2]
to = lisinp[3]
fee = lisinp[4]
blocknum = lisinp[5]

msg = (fromadd + amount + to + fee + blocknum).encode("UTF-8")
msgSigner = fromadd
signature = eth_keys.keys.Signature(binascii.unhexlify(signature[2:]))
signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
valid = signerRecoveredAddress == msgSigner
print('Signature valid?:', valid)
print('signer balance' ,adder.balance(signerRecoveredAddress))
if(valid && (blocknum==blocknumjsn)):
    messageadder.add(fromadd,to,amount,fee)
'''
signature = eth_keys.keys.Signature(binascii.unhexlify("0x6d4d71abfbf1c21e13ca7bdcc597d02063dd5ff9c3db8a99ad1d2c9a73ac920f6e4e9857f50d63173dd359880f95a9f7384e229aac450730d2f5922a4b9642b801"[2:]))
signerRecoveredPubKey = signature.recover_public_key_from_msg("39f9ce7d6dd10302131e8ceb5d4012705183897742e9c1ea6dbca1e449594294".encode('UTF-8'))
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
print(signerRecoveredAddress)
