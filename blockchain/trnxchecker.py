import ecdsa
import hashlib
from ecdsa import SigningKey, NIST384p
from ecdsa import SigningKey, VerifyingKey
import binascii

private_key = SigningKey.generate(curve=NIST384p) # uses NIST192p
print(private_key.to_string().hex())
public_key = private_key.verifying_key
print(public_key.to_string().hex())
signature = private_key.sign(b"Educative authorizes this shot")
print(signature.hex())


signature2 ="dbd2f51f33cfb96889edb06cbec937ad06787789060a720d16a83fc94fb62a961f0b3a3f9eaa54805c9f174daa99d2f288e67191994a8310903bf0c64791ad8936ab229117ca146e8d2b2dffa3015e17789ae4dba24d9b7c75dddd85c09b7a80"

signature2 = binascii.unhexlify(signature2)

public_key = VerifyingKey.from_string(binascii.unhexlify("85c47fb7d40e32aee921c9332f30c9a0414f2f1d7c7006203b6bc7d5dae5dfbc48823307dcc984e9e3dc7e99f318fa8228932b98a77378f2ed109f9b773dd63442f239b30f176a14591649e3fb52c91bb97de5e800da828cd65b1860f639c066"), curve=NIST384p)
print("Verified:", public_key.verify(signature2, b"Educative authorizes this shot"))
