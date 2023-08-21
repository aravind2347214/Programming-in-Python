# 



BLACKWHITE=[['black'],['white','black'],['white'],['white','black'],['white'],['black']]

def uniqueCount(colorList):
    color_dict={}
    for node in colorList:
        color_dict[tuple(node)]= colorList.count(node)
    print(color_dict)  

uniqueCount(BLACKWHITE) 


