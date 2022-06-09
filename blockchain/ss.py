from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from cryptography import exceptions
import binascii
import sys


#private_value = 0xb3218473105359e241338f91160824629277839e227d54b27dca651c57ea0112
#private_value2 = 0x63bd3b01c5ce749d87f5f7481232a93540acdb0f7b5c014ecd9cd32b041d6f33
private_value = 0xb3218473105359e241338f91160824629277839e227d54b27dca651c57ea0112

curve = ec.SECP256R1()
signature_algorithm = ec.ECDSA(hashes.SHA256())

# Make private and public keys from the private value + curve
priv_key = ec.derive_private_key(private_value, curve, default_backend())
#priv_key2 = ec.derive_private_key(private_value2, curve, default_backend())
pub_key = priv_key.public_key()
print('Private key: 0x%x' % priv_key.private_numbers().private_value)
print('Public point (Uncompressed): 0x%s' % pub_key.public_bytes(serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint).hex())

# Sign some data
data = "sepehrmnp".encode()
signature = priv_key.sign(data, signature_algorithm)
print('Signature: 0x%s' % signature.hex())

# Verify
try:
    pub_key.verify(signature, data, signature_algorithm)
    print('Verification OK')
except InvalidSignature:
    print('Verification failed')

private_key = ec.generate_private_key(ec.SECT233R1())
private_vals = private_key.private_numbers()

no_bits=private_vals.private_value.bit_length()
print (f"Private key value: {private_vals.private_value}. Number of bits {no_bits}")
pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
der = private_key.private_bytes(encoding=serialization.Encoding.DER,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
print ("\nPrivate key (PEM):\n",pem.decode())
print ("Private key (DER):\n",binascii.b2a_hex(der))
