employee={
    "name": "tony stark",
    "emp_id": 3,
    "address": [
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"
        },
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"   
        }
    ]
}
for i in range (len(employee["address"])) : 
    print(employee["address"][i]["pincode"])
employee_list = [
    {
    "name": "tony stark",
    "emp_id": 3,
    "address": [
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"
        },
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"   
        }
    ]  
    },
    {
    "name": "steve roggers",
    "emp_id": 6,
    "address": [
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"
        },
        {
            "line1": "fff",
            "line2": "hhh",
            "state": "wb",
            "pincode": "700107"   
        }
    ]
    }
]
# emp_pin_list = []
# for emp in employee_list:
#     emp_pin_list.append({"name":emp["name"]})
#     emp_pin_list[employee_list.index(emp)][address]=[]
#     for address in emp["address"]:
#         emp_pin_list[employee_list.index(emp)][address].append(address[address])
# print(emp_pin_list)
def get_emp_pin_list(employee_list,Key):
    emp_pin_list = []
    for emp in employee_list:
      emp_pin_list.append({"name": emp["name"]})
      emp_pin_list[employee_list.index(emp)][Key] = []
      #print(emp["address"])
      for address in emp["address"]:
        #print(employee_list.index(emp))
        emp_pin_list[employee_list.index(emp)][Key].append(address[Key])
        print("Address:", address[Key])
    return get_emp_pin_list

func_list = get_emp_pin_list(employee_list,Key="state")
print(func_list)