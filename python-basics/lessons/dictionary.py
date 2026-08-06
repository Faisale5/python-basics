car ={
    "brand": "Hyundai",
    "model": "i30",
    "year": 2014
}
print(car["brand"])
print(car["model"])
print(car["year"])

person = {
    "name": "Faisal",
    "age": 22 
}

print(person["name"])
print(person["age"])
person["age"] = 23
print(person["age"])

person["country"] = "Australia"
person["job"] = "Student"
print(person["country"])
print(person["job"])

del person["job"]
print(person)