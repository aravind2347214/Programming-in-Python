# %%
def swap(numlist):
    print("Before Swapping : ",numlist)
    temp = numlist[-1]
    numlist[-1]=numlist[0]
    numlist[0]=temp
    print("After Swapping : ",numlist)

def listSum(numlist):
    sum=0
    for singleElement in numlist:
        sum+=singleElement
    print("The Sum is : ",sum)

def smallest(numlist):
    small=numlist[0]
    for i in numlist:
        if i<small:
            small=i
    print("Smallest in List is : ",small)

numericList=[23.5,43,65,21,55.6,33.2,55]
swap(numericList)
listSum(numericList)
smallest(numericList)


# %%
# Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).

domainAttributes=["clientName","workerId","location","rating"]
# "maxAmountPerHour",'clientId', 'workerName', 'workerAvailablity', 'clientAge', 'expectedDuration'
print("Initial List : ",domainAttributes)
domainAttributes.append("maxAmountPerHour")
domainAttributes.insert(1,"clientAge")
domainAttributes.extend(["clientId", "workerName", "workerAvailablity", "clientAge", "expectedDuration"])
person={
    "name":"same",
    "age":45,
    "gender":"male"
}

pincodes={2034,2043,2021,1223}
marks=(90,43,54,65)
domainAttributes.extend(marks)
domainAttributes.extend(pincodes)
domainAttributes.insert(0,person)

print("After Adding elements : ",domainAttributes)


# %%
# Sorting dictionary based on the key
mydict={'a': 1, 'b': 2, 'c': 3,
'k': 11, 'm': 13, 'z': 26,
'a': 1, 'x': 24, 'y': 25,
'p': 16, 'q': 17, 'r': 18}

# new_dict = dict(sorted(mydict.items())) 
# rev_new_dict = dict(sorted(mydict.items(),reverse=True))
keys= list(mydict.keys())
keys.sort()
# new_dict= {key:mydict[key] for key in keys}
new_dict = dict(sorted(mydict.items(),key=lambda item : item[0]))
print(new_dict)


# %%
#Sum of Values for a dictionary
mydict={'a': 1, 'b': 2, 'c': 3,
'k': 11, 'm': 13, 'z': 26,
'a': 1, 'x': 24, 'y': 25,
'p': 16, 'q': 17, 'r': 18}

sum=0
print(mydict.items())
for key,val in mydict.items():
    sum+=val
    print(val)
print("Sum : ",sum)
    



# %%
# sorting dictionary based on decending order of value in lambda function
mydict={'a': 1, 'b': 2, 'c': 3,
'k': 11, 'm': 13, 'z': 26,
'a': 1, 'x': 24, 'y': 25,
'p': 16, 'q': 17, 'r': 18}

new_dict=sorted(mydict,key= lambda item:item[1],reverse=True)
print()



