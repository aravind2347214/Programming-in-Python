import pandas as pd
dict1={
    'name':["Samantha","Tom","John","Serah"],
    'age':[23,24,21,25],
    'gender':["Female","Male","Male","Female"]
}
df = pd.DataFrame(dict1)
#df = pd.DataFrame.from_dict(dict1)
print(df)