import json,hashlib

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
                file_data = json.load(file)
                file_data[hs]["recvd"].append({"reciever":new_data_2,"amount":amount})
                file_data[hs]['fee']+=fee
                #file_data[hs]["recvd"][new_data_2]['amount'] = amount
                file.seek(0)
                json.dump(file_data, file)
                a="sss1"
        else:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                y = {hs: {"data":new_data,"recvd":[{"reciever":new_data_2,"amount":amount}],"fee":fee}}
                #file_data[hs]["recvd"][new_data_2]['amount'] = amount
                file_data.update(y)
                file_data["index"].append(hs)
                file.seek(0)
                json.dump(file_data, file)
                a="sss2"
        return a


