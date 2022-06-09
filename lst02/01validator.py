import json,adder01,hsh
import eth_keys, eth_utils, binascii, os,  ecdsa
privKey =eth_keys.keys.PrivateKey(binascii.unhexlify(str("26e4500ee80f51cc07f83670e6295d1cf3a4be3adfbafc02cb27d4b3bd281d08")))
pubKey = privKey.public_key
address = pubKey.to_checksum_address()

def validate():
    with open("blocks/00chaininf.json",'r') as file:
                            jsondata = json.load(file)
                            blocknum =jsondata['blocknum']
                            file.seek(0)

    with open("blocks/"+str(blocknum-2)+".json",'r') as file:
                        prvhsh = json.load(file)['hash']
                        print(prvhsh)
                        file.seek(0)

    with open("blocks/"+str(blocknum-1)+".json",'r') as file:
                            file_data = json.load(file)
                            file.seek(0)

    with open("validators.json",'r') as file:
                        validator = json.load(file)['validators'][0]
    if(validator!=file_data['validator']):
        return 0
    
    
    for i in range(len(file_data['trans']['index'])):
                    amountspent=0
                    for j in range(len(file_data['trans'][file_data['trans']['index'][i]]['recvd'])):
                               amountspent+=int(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]['amount'],16)
                    amountspent+=int(file_data['trans'][file_data['trans']['index'][i]]['fee'],16)
                    if(amountspent<adder01.balance(file_data['trans'][file_data['trans']['index'][i]]['data'])):
                        continue
                    else:
                        return 0
    blockdata=str(blocknum-1)+str(file_data['trans'])+prvhsh+validator
    msg = (hsh.hsh(blockdata)).encode('UTF-8')
    msgSigner = validator
    signature = eth_keys.keys.Signature(binascii.unhexlify(file_data['sign'][2:]))
    signerRecoveredPubKey = signature.recover_public_key_from_msg(msg)
    signerRecoveredAddress = signerRecoveredPubKey.to_checksum_address()
    valid = signerRecoveredAddress == msgSigner
    if(valid):
        return file_data

def validated():    
    print(validate())
    file_data=validate()
    if(file_data):
        for i in range(len(file_data['trans']['index'])):
         
            amountspent=0
            for j in range(len(file_data['trans'][file_data['trans']['index'][i]]['recvd'])):
                amountspent+=int(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]['amount'],16)
            amountspent+=int(file_data['trans'][file_data['trans']['index'][i]]['fee'],16)
            if(amountspent<adder01.balance(file_data['trans'][file_data['trans']['index'][i]]['data'])):
                                #print(file_data['trans'][file_data['trans']['index'][i]]['data'])
                adder01.add(file_data['trans'][file_data['trans']['index'][i]]['data'],adder01.balance(file_data['trans'][file_data['trans']['index'][i]]['data'])-amountspent)
                for j in range(len(file_data['trans'][file_data['trans']['index'][i]]['recvd'])):
                    adder01.add(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]['reciever'],adder01.balance(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]["reciever"])+int(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]["amount"],16))
                                    #print(str(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]['reciever'] )+":"+str(adder01.balance(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]["reciever"])+int(file_data['trans'][file_data['trans']['index'][i]]['recvd'][j]["amount"],16
        msg = file_data['hash'].encode('UTF-8')
        signature = privKey.sign_msg(msg)
        print(address)
        print(signature)
            
validated()
