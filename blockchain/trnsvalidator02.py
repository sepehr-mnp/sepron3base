import eth_keys, eth_utils, binascii, os,  ecdsa
from ecdsa import SigningKey, NIST384p
import sys,adder,messageadder
import json,hashlib
###
def hsh(string):
    encoded=string.encode()
    m = hashlib.sha256(encoded)
    return m.hexdigest()[:8]

def exchecker(newport,newport2):
        a=0
        with open("messages.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        if(hsh(newport) in data):
            a = 1
            for i in data[hsh(newport)]["recvd"]:
                    if(newport2  == i["reciever"]):
                       a = 2
                       break
        return a
def add(new_data,new_data_2,amount,fee, filename='messages.json'):
        a = exchecker(new_data,new_data_2)
        hs = hsh(new_data)
        if(a ==2):
                return "fucked up!"
        elif (a==1):
            with open(filename,'r+') as file:
                print("Sep")
                file_data = json.load(file)
                file_data[hs]["recvd"].append({"reciever":new_data_2,"amount":amount})
                file_data[hs]['fee']+=fee
                #file_data[hs]["recvd"][new_data_2]['amount'] = amount
                file.seek(0)
                json.dump(file_data, file)
        else:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                y = {hs: {"data":new_data,"recvd":[{"reciever":new_data_2,"amount":amount}],"fee":fee}}
                #file_data[hs]["recvd"][new_data_2]['amount'] = amount
                file_data.update(y)
                file_data["index"].append(hs)
                file.seek(0)
                json.dump(file_data, file)
                

####
def balance(acc):
    acc=str(acc)
    print(0)
    with open("accs.json",'r') as file:
        print(1)
        file_data = json.load(file)
        try:
            return int(file_data[acc],16)
        except:
            return 0
#lisinp = input()
#lisinp = sys.argv[1]

signature = sys.argv[1]
fromadd = sys.argv[2]
amount = sys.argv[3]
to = sys.argv[4]
fee = sys.argv[5]
blocknum = sys.argv[6]

msg = (fromadd + amount + to + fee + blocknum).encode("UTF-8")
msgSigner = fromadd
signature = eth_keys.keys.Signature(binascii.unhexlify(signature[2:]))
signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
#print('Signature valid?:', signerRecoveredAddress == msgSigner)
#print('signer balance' ,adder.balance(signerRecoveredAddress))
#add(fromadd,to,amount,fee)
if((signerRecoveredAddress == msgSigner) and adder.balance(msgSigner)):
    print("hiiii")
    #print(add(fromadd,to,amount,fee))
    #adder.add(fromadd,adder.balance(signerRecoveredAddress)-int(amount,16))
    #adder.add(to,adder.balance(to)+int(amount,16))
 
