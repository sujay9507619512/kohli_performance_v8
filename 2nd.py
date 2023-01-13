# ratedAvengerList2D = [
#     ["spiderman",8],
#     ["groot",7],
#     ["black widow",8]
# ]
# for i in range (0, len(ratedAvengerList2D)):
#     for j in range (0, len(ratedAvengerList2D[i])):  
#         print(ratedAvengerList2D[i][j])



# for elem in ratedAvengerList2D:
#     for inne






# employee = {
#     "name": "tony stark",
#     "emp_id": 3,
#     "address": [
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"
#         },
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"   
#         }
#     ]
# }
# for i in range (len(employee["address"])) : 
#     print(employee["address"][i]["pincode"])




# employee_list = [
#     {
#     "name": "tony stark",
#     "emp_id": 3,
#     "address": [
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"
#         },
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"   
#         }
#     ]  
#     },
#     {
#     "name": "steve roggers",
#     "emp_id": 6,
#     "address": [
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"
#         },
#         {
#             "line1": "fff",
#             "line2": "hhh",
#             "state": "wb",
#             "pincode": "700107"   
#         }
#     ]
#     }
# ]
# emp_pin_list = []
# for emp in employee_list:
#     emp_pin_list.append({"name":emp["name"]})
#     emp_pin_list[employee_list.index(emp)]["pincode"]=[]
#     for address in emp["address"]:
#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
# print(emp_pin_list)




# def get_employee_pin_list(employee_list):
#     emp_pin_list = []
# for emp in employee_list:
#     emp_pin_list.append({"name":emp["name"]})
#     emp_pin_list[employee_list.index(emp)]["pincode"]=[]
#     for address in emp["address"]:
#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
#     return get_employee_pin_list(employee_list)
#     print(func_list)




# #questions--1__function call
# a=7
# b=6
# result=a*b
# print(result)
# def multiply (a,b):
#     result=a*b
#     return result
# #calling functions
# result=multiply(4,8)
# print(result)



## from file name import * ---->call the file that u want to impoert in the current file



