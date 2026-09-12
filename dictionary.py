#student=[1,"mouni","python",95.32,"hyderabad"]


student={
    "name":"mouni",
    "ID":"1",
    "course":"python",
    "cgpa":95.32,
    "address":"hyderabad"
}
# print(student["ID"])
# print(student["name"])
# print(student["course"])
# print(student["cgpa"])
# print(student["address"])
# print(student.get("salary"))
# adding a new key
#dict_name["new_key"]="value"


#items()
# for key, value in student .items():
#     print(key,value)

student. update ({   
    "name":"Amar",
    "number":"34567890"
})        
student.pop("number")
student.clear()
print(student)

 