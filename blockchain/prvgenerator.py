import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p
print(os.urandom(32))
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
