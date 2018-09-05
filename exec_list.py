exec_list = [1,2,3,4,5]
wait_list = [61261,1235,1346]

comb_list = list(zip(wait_list, exec_list)) 
comb_list.sort() 
list1, list2 = list(zip(*comb_list)) 
print(list1[0],list2[0]) 