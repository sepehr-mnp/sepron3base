import json
def listUpdate():
    with open("validatorscandidates.json",'r+') as file:
                            file_data = json.load(file)
                            file.seek(0)
                            json.dump(file_data, file)

    ##prossecc on validators
    validatorslist = {"validators":file_data['validators']}

    with open("validators.json", "w+") as outfile:
                    json.dump(validatorslist, outfile)
    #chck
    print("list Updated")
