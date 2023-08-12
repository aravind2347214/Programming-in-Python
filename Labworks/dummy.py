'''Multiple inheritance'''
class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Work:
    def __init__(self,workID,workLocation):
        self.workID =  workID
        self.workLocation=workLocation

class Worker(User,Work):
    def __init__(self, name, age, gender,workID,workLocation,workerID,workerRate):
        User.__init__(name, age, gender)
        Work.__init__(workID,workLocation) 
        self.workerID=workerID
        self.workerRate=workerRate

    def WorkerDisplay(self):
        print("Worker ID     : ",self.workerID)
        print("Worker Name   : ",self.name)   
        print("Worker Age    : ",self.age)   
        print("Worker Gender : ",self.gender)   
        print("Work ID       : ",self.workID)
        print("Work Location : ",self.workLocation)
        print("Worker Rate   : ",self.workerRate)

print("Enter Worker Details")
workerID=input("Enter Worker ID")
wName=input("Enter Worker Name")
wAge=input("Enter Worker Age")
wGender=input("Enter Worker Gender")
workID=input("Enter Work ID")
workLocation=input("Enter Work Location")
workerRate=input("Enter Worker Hourly Rate")

workerObj=Worker(wName,wAge,wGender,workID,workLocation,workerID,workerRate)
workerObj.WorkerDisplay()


    
        

        