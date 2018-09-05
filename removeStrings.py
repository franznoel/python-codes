stringlengths = {"somethingisgoing":"onherewiththeworld","this":"isnottheanswerim","looking":"for"}

for i in list(stringlengths.keys()): 
    if stringlengths[i] > 10 or stringlengths[i] < 3 :
       del stringlengths[i]

print(stringlengths)