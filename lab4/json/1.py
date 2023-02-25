import json

y = open ("sample_data.json",'r')
json_object = json.load(y)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for x in json_object["imdata"]:
    for y in x["l1PhysIf"]:
        for f in x["l1PhysIf"][y]:
            if f == 'dn':
                DN = x["l1PhysIf"][y][f]
            if f == "speed":
                Speed = x["l1PhysIf"][y][f]
            if f == "mtu":
                MTU = x["l1PhysIf"][y][f]
            if f == "description":
                Description =  x["l1PhysIf"][y][f]
            else: 
                Description = ""
    print(f"{DN}                            {Description}  {Speed}   {MTU}")