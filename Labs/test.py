Write a function get_name(name_dict, id_num) that takes as its first parameter a dictionary mapping an ID number to a name and as its second parameter a particular ID number (which might be invalid) and returns the name associated with the given ID number if that ID number exists in the dictionary or None otherwise.
















#def list_sorting(lst1, lst2):
#     for i in range(len(lst2)):
#         for j in range(i+1, len(lst2)):
#             if lst2[i] < lst2[j]:
#                 lst2[i], lst2[j] = lst2[j], lst2[i]
#                 lst1[i], lst1[j] = lst1[j], lst1[i]
#             elif lst2[i] == lst2[j]:
#                 print(lst1[i],lst1[j])
#                 for k in range(len(lst1[j])-1):
#                     print(lst1[i][k])
                


# #lst2,lst1 = (list(t) for t in zip(*sorted(zip(lst2, lst1))))
# #print(lst1,lst2)
                
#                 # firstName=lst1[i]
#                 # secondName=lst1[j]
#                 # print(secondName)
#                 # for k in range(len(firstName)):
#                 #     for e in range(len(secondName)):
#                 #         if secondName[e] > firstName[k]:
#                 #             lst2[i], lst2[j] = lst2[j], lst2[i]
#                 #             lst1[i], lst1[j] = lst1[j], lst1[i]
#                 #         else:
#                 #             break
    
#     print(lst1)
#     print(lst2)

# lst1=['Adam',"bella","sophia","eve","james"]
# lst2=[28,36,27, 36, 36]
	
# list_sorting(['Ali','Aali','Asad','Amad','Arran','Allen','Abraham'],[41,41,41,65,41,23,41])