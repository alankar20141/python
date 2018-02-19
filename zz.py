list1 = [1,2,3,4,5,4,6,4]
#new_list = [elem for elem in list1 if elem != 4] list comprension
#print (new_list)
        
for i in list1:
    #print (index)
    if i == 4:
        list1.remove(4)

print (list1)
