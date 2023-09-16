 # %%
# Write a python program to count the frequency of any specific word (in your domain) in the paragraph.
paragraph="This computer science project involves developing a user-centric application to connect urban residents with skilled labor workers like electricians, plumbers, and gardeners. The application's robust database incorporates ten distinct entities, each possessing a minimum of ten attributes. These entities include Users/Clients, Skilled Labor Workers, Services/Job Listings, Reviews and Ratings, Payment Transactions, Worker Availability Schedule, Client Preferences, Service Categories, Location/City Information, and Notifications and Alerts. To ensure efficient data management, the project utilizes various data types,IDs-integer, names-string , descriptions-string, timestamps-dates, hourlyRates-float, statusIndicator-boolean. The diverse data types enhance the application's functionality and enrich users' experience while seeking skilled labor services in major cities."
specificWord= input("Enter Word to find its frequency")
paragraph= paragraph.lower()
specificWord=specificWord.lower()
words = paragraph.split()
frequency = words.count(specificWord)
print("The word  '",specificWord,"'  Occurs ",frequency,"times")


# %%
# Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.
paragraph="This computer science project involves developing a user-centric application to connect urban residents with skilled labor workers like electricians, plumbers, and gardeners. The application's robust database incorporates ten distinct entities, each possessing a minimum of ten attributes. These entities include Users/Clients, Skilled Labor Workers, Services/Job Listings, Reviews and Ratings, Payment Transactions, Worker Availability Schedule, Client Preferences, Service Categories, Location/City Information, and Notifications and Alerts. To ensure efficient data management, the project utilizes various data types,IDs-integer, names-string , descriptions-string, timestamps-date, hourlyRates-float, statusIndicator-boolean. The diverse data types enhance the application's functionality and enrich users' experience while seeking skilled labor services in major cities."
alphabetCount=0
digitCount=0
specialCharCount=0
spaceCount=0
for charecter in paragraph:
    if(charecter.isdigit()):
        digitCount+=1
    elif(charecter.isalpha()):
        alphabetCount+=1
    elif(charecter.isspace()):
        spaceCount+=1
    else:
        specialCharCount+=1

print("Alphabets          : ",alphabetCount)
print("Digits             : ",digitCount)
print("Special Charecters : ",specialCharCount)
print("Spaces             : ",spaceCount)

        


# %%
# Write a python program to display all the datatypes of selected specific elements in the paragraph. (For example:– name - string, reg.no - int, marks - float, etc.)
paragraph="This computer science project involves developing a user-centric application to connect urban residents with skilled labor workers like electricians, plumbers, and gardeners. The application's robust database incorporates ten distinct entities, each possessing a minimum of ten attributes. These entities include Users/Clients, Skilled Labor Workers, Services/Job Listings, Reviews and Ratings, Payment Transactions, Worker Availability Schedule, Client Preferences, Service Categories, Location/City Information, and Notifications and Alerts. To ensure efficient data management, the project utilizes various data types,IDs-integer, names-string , descriptions-string, timestamps-date, hourlyRates-float, statusIndicator-boolean. The diverse data types enhance the application's functionality and enrich users' experience while seeking skilled labor services in major cities."
import re
def datatypeExtractor(paragraph):
    dataSet={}
    regexPattern = r"([A-Za-z0-9_]+)\s*-\s*(integer|float|boolean|string|date)"
    matches = re.findall(regexPattern, paragraph)

    for elementName, dataType in matches:
        dataSet[elementName] = dataType
    return dataSet

dataTypesSet = datatypeExtractor(paragraph)
for node,dtype in dataTypesSet.items():
    print(f"{node}-->{dtype}")

# %%
# Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain) and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.
def setOperation():
    initialSet={ 45 , True , 59.6 , "Sigma" , (9,5,6,7)}
    print("Initial Set is : ",initialSet)

    poppedElement= initialSet.pop()
    print("Popped Element : ",poppedElement)
    print("Set after Element Pop : ",initialSet)

    discardElement=45
    initialSet.discard(discardElement)
    print("Set after Discarding Element : ",initialSet)

    initialSet.clear()
    print("Set after Clearing : ",initialSet)

    initialSet={ 45 , True , 59.6 , "Sigma" , (9,5,6,7)}

    del initialSet
    
    try:
        print("Set After deletion",initialSet)
    except:
        print("Element Cant Be Displayed As it was deleted")  

setOperation()

"""" 
>>Sets are collection of unordered Elements.
>>The elements popped or discarded can change on each execution as set is unordered
>>Sets can contain diffrent kinds of data within it 
>>The pop() function  removes an arbitrary value from the set and the
  popped element is returned hence it cannot be predicted
>>The discard() function removes a particular element from the Set which can be decided.If the 
  told element does not exist in the list it does not raise an error
>>The clear() function makes the set empty or clears all the elements in the set.
>>The del keyword removes the set variable from memory making it inaccessable.if tried to access 
  it would raise a KeyError
"""


# %%


# %%
# Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.

"""" 
The Attributes used here are :
ClientName
WorkerId
Location
Rating
MaxAmountPerHour
"""

domainAttributes={"clientName","workerId","location","rating","maxAmountPerHour"}
print("Initial Set : ",domainAttributes)
sortedSet= sorted(domainAttributes,reverse=True)
print("Sorted Set : ",sortedSet)

# %%
# Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.
pattr1="clientId"
pattr2="workerName"
pattr3="workerAvailablity"
pattr4="clientAge"
pattr5="expectedDuration"
attributeTuple=tuple([pattr1,pattr2,pattr3,pattr4,pattr5])
attr1,attr2,*attr3,attr4=attributeTuple
print("The initial tuple : ",attributeTuple)
print("Attribute 1 : ",attr1)
print("Attribute 2 : ",attr2)
print("Attributes 3 : ",attr3)
print("Attribute 4 : ",attr4)

# %%
# Enter your domain name as characters and count any number of characters and print 
# the count (for example – (‘p’,’r’,’o’,’g’,’r’,’a’,’m’) count of ‘r’ = 2

def alphabetCounter(domainName):
    letterSet={}
    for letter in domainName:
        if letter.isalpha():
            lowerLetter=letter.lower()
            letterSet[lowerLetter]=letterSet.get(lowerLetter,0)+1
    return letterSet
# domainName=('L','a','b','o','r','M','a','n','a','g','e','m','e','n','t')
domainName=input("Enter the domain Name")

letterSet= alphabetCounter(domainName)

print(domainName)
print("Letter counts")
for letter,lCount in letterSet.items():
    print(letter," : ",lCount)

# %%
# Enter your domain name, execute all the slicing possibilities and also negative indexing.
domainName= input("Enter your Domain Name")
stringLength=len(domainName)
# print(stringLength)

for i in range(0,stringLength + 1):
    for j in range(i+1,stringLength + 1):
        subString = domainName[i:j]
        print(f"{domainName}[{i}:{j}] = {subString}")

for i in range(-stringLength-1,0):
    for j in range(i+1,0):
        subString = domainName[i:j]
        print(f"{domainName}[{i}:{j}] = {subString}")


# %% [markdown]
# 


