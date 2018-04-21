mykeys  = {"Key1":[1,3,4],"Key2" :"Jessy","Key3":"asdfas"}
print(mykeys)
print(mykeys["Key1"])

# Duplicate Keys provide waring however the latest one being picked.
mykeys  = {"Key1":1,"Key2" :"Jessy","Key1":1}
print(mykeys)
print(mykeys["Key1"])

# Iterate through dictionary and get Keys
for i in mykeys.keys():
    print(i)
    
# Iterate through dictionary and get Keys
for i in mykeys.keys():
    print(mykeys[i])
    
for i in mykeys.keys():
    print(mykeys.get(i))
    
for i in mykeys.items():
    print(i)


