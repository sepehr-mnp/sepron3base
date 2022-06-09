import json
def add(hsh,sign):
    with open("validatorssigns.json",'r+') as file:
                            file_data = json.load(file)
                            file.seek(0)
                            json.dump(file_data, file)
    file_data[hsh].append(sign)
    
    with open("validatorssigns.json", "w+") as outfile:
                    json.dump(file_data, outfile)
#add("39f9ce7d6dd10302131e8ceb5d4012705183897742e9c1ea6dbca1e449594294","0x6d4d71abfbf1c21e13ca7bdcc597d02063dd5ff9c3db8a99ad1d2c9a73ac920f6e4e9857f50d63173dd359880f95a9f7384e229aac450730d2f5922a4b9642b801")
