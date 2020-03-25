



#Dictionary
mylist = {1,2,3,4}
myDictionary = {"key":"value","key2":"vlue"}

myPhones= {"IPHONEX":100,"Samsung":500}

print(myPhones) 

Iphone_Price=myPhones["IPHONEX"]
#access dic keys
print("Iphone price: " + str(Iphone_Price))

#change key value

myPhones["IPHONEX"]=1000
print(myPhones)

myPhones.clear()
print(myPhones)