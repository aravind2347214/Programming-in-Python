COLORS=[['black'],['black','white'],['white'],['black','white'],['white'],['black','white']]

def unique_count(colorList):
    color_dict={}
    for node in colorList:
        color_dict[tuple(node)]=colorList.count(node)
    print(color_dict)

unique_count(COLORS) 

       

