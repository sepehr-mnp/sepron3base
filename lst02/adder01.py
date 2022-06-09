import json
#heighest 4*10**73
def add(acc,val):    
    with open("01validator/accs.json",'r+') as file:
        file_data = json.load(file)
        y = {acc : hex(val)}
        file_data.update(y)
        file.seek(0)
        json.dump(file_data, file)
def balance(acc):
    acc=str(acc)
    with open("01validator/accs.json",'r+') as file:
        file_data = json.load(file)
        try:
            return int(file_data[acc],16)
        except:
            return 0
#print(balance("0x97031154547BA86D4bb22036e0764a96DbE19d73"))
