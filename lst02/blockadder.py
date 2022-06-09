import eth_keys, eth_utils, binascii, os,  ecdsa
import json,hsh,adder
import sched
import time,validatorlister

scheduler = sched.scheduler(time.time, time.sleep)
privKey =eth_keys.keys.PrivateKey(binascii.unhexlify(str("4889127bb642b09f893570b4aa315e1a672366d11c15877d64eedb640bd7cd92")))
pubKey = privKey.public_key
address = pubKey.to_checksum_address()
                        
def blockadder():
        now = time.time()
        print('EVENT:', now)
        scheduler.enterabs((int(now)+(5-int(now)%5)), 2, blockadder)

        with open("messages.json",'r+') as file:
                        file_data = json.load(file)
                        file.seek(0)
                        json.dump(file_data, file)

        print(len(file_data))
        for i in range(len(file_data['index'])):
                amountspent=0
                for j in range(len(file_data[file_data['index'][i]]['recvd'])):
                           amountspent+=int(file_data[file_data['index'][i]]['recvd'][j]['amount'],16)
                amountspent+=int(file_data[file_data['index'][i]]['fee'],16)
                if(amountspent<adder.balance(file_data[file_data['index'][i]]['data'])):
                    print(file_data[file_data['index'][i]]['data'])
                    adder.add(file_data[file_data['index'][i]]['data'],adder.balance(file_data[file_data['index'][i]]['data'])-amountspent)
                    for j in range(len(file_data[file_data['index'][i]]['recvd'])):
                        adder.add(file_data[file_data['index'][i]]['recvd'][j]['reciever'],adder.balance(file_data[file_data['index'][i]]['recvd'][j]["reciever"])+int(file_data[file_data['index'][i]]['recvd'][j]["amount"],16))
                        print(str(file_data[file_data['index'][i]]['recvd'][j]['reciever'] )+":"+str(adder.balance(file_data[file_data['index'][i]]['recvd'][j]["reciever"])+int(file_data[file_data['index'][i]]['recvd'][j]["amount"],16)))
                else:
                    #bara delet element az dict
                    file_data.pop(file_data['index'][i],None)

        print(len(file_data))
        print(file_data)
###check if im block creartor
        with open("validators.json",'r') as file:
                        validator = json.load(file)['validators'][0]
                        #file.seek(0)
                        #json.dump(file_data, file)
        print(validator==address)
        #validatorlister.listUpdate()
        if(len(file_data)>1):
            print(file_data)
            
            with open("blocks/00chaininf.json",'r') as file:
                        jsondata = json.load(file)
                        blocknum =jsondata['blocknum']
                        file.seek(0)
                        #json.dump(jsondata, file)

            print(blocknum)

            with open("blocks/"+str(blocknum-1)+".json",'r') as file:
                        prvhsh = json.load(file)['hash']
                        print(prvhsh)
                        file.seek(0)
                        #json.dump(prvhsh, file)

            #msg = b'Message for signing'
            blockdata=str(blocknum)+str(file_data)+prvhsh+address
            msg = (hsh.hsh(blockdata)).encode('UTF-8')
            signature = privKey.sign_msg(msg)
            hashb =hsh.hsh(blockdata+str(signature))
            dictionary ={
                "blocknum" : blocknum ,
                "trans" : file_data,
                "prvhash" : prvhsh,
                "validator" :address ,
                "sign":str(signature),
                "hash": hashb
            }
              
            with open("blocks/"+str(blocknum)+".json", "w+") as outfile:
                json.dump(dictionary, outfile)

            with open("blocks/00chaininf.json",'r+') as file:
                        jsondata = json.load(file)
                        jsondata['blocknum']=blocknum+1
                        file.seek(0)
                        json.dump(jsondata, file)

            

            with open("messages.json", "w+") as outfile:
                dictionary ={"index":[]}
                json.dump(dictionary, outfile)
        ###inja bayad ezaf konim tabe validator
            with open("validatorssigns.json", "w") as outfile:
                json.dump('{"'+hashb+'":[]}', outfile)
        else:
                print("nothing")


now = time.time()
scheduler.enterabs((int(now)+(5-int(now)%5)), 2, blockadder)
scheduler.run()


