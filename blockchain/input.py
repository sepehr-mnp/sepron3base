import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p
#privKey =SigningKey.from_string(binascii.unhexlify("3ea09de34eb951239b7a6842ef6136af73bea6f0a5013826e8330af17624e80f"))
privKey = eth_keys.keys.PrivateKey(os.urandom(32))
#privKey = eth_keys.keys.PrivateKey(binascii.unhexlify('3ea09de34eb951239b7a6842ef6136af73bea6f0a5013826e8330af17624e80f'))
pubKey = privKey.public_key
pubKeyCompressed = '0' + str(2 + int(pubKey) % 2) + str(pubKey)[2:66]
address = pubKey.to_checksum_address()
print('Private key (64 hex digits):', privKey)
print('Public key (plain, 128 hex digits):', pubKey)
print('Public key (compressed, 66 hex digits):', pubKeyCompressed)
print('Signer address:', address)

print()

msg = b'Message for signing'
signature = privKey.sign_msg(msg)
print('Msg:', msg)
print('Msg hash:', binascii.hexlify(eth_utils.keccak(msg)))
print('Signature: [v = {0}, r = {1}, s = {2}]'.format(
    hex(signature.v), hex(signature.r), hex(signature.s)))
print('Signature (130 hex digits):', signature)

print()
'''
msg = b'Message for signing'
msgSigner = '0xa44f70834a711F0DF388ab016465f2eEb255dEd0'
signature = eth_keys.keys.Signature(binascii.unhexlify(
    '6f0156091cbe912f2d5d1215cc3cd81c0963c8839b93af60e0921b61a19c54300c71006dd93f3508c432daca21db0095f4b16542782b7986f48a5d0ae3c583d401'))
signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
print('Signer public key (128 hex digits):', signerRecoveredPubKey)
print('Signer address:', signerRecoveredAddress)
print('Signature valid?:', signerRecoveredAddress == msgSigner)
'''
msg = b'Message for signing'
msgSigner = '0xc302CEC938Ef81922aa06B8c0958030a99a357c5'
signature = eth_keys.keys.Signature(binascii.unhexlify('15a6842ad475fdad4e3aa8e559665704d5f28e72fec69afae6ce27876ae8250a62a0223d461d3d0c796b02f53b5c6b29b5ca4d04b6c3735649eeaefb1e6d8c1100'))
signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
print('Signer public key (128 hex digits):', signerRecoveredPubKey)
print('Signer address:', signerRecoveredAddress)
print('Signature valid?:', signerRecoveredAddress == msgSigner)
