import json

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.id}, {self.name}, {self.salary}"

#-------------------------------------------------------------

## JSON ###################################################

def JSONStorage(fileName):
    # 1. Create object
    emp = Employee(111, "Rakesh", 100000)

    # 2. Convert to dictionary
    dt = {
        "id": emp.id,
        "name": emp.name,
        "salary": emp.salary
    }

    # 3. Save to a file
    with open(fileName, 'w') as file:
        json.dump(dt, file, indent=4)

def JSONModifyData(fileName):
    # 4. Read the file
    with open(fileName, 'r') as file:
        dt = json.load(file)
    print(dt)

    # 5. Convert to Object
    obj = Employee(dt['id'], dt['name'], dt['salary'])
    print(obj)

    # 6. Modify Object
    obj.salary += 50000
    print(obj)

    # 7. Convert to dictionary
    dt = {
        "id": obj.id,
        "name": obj.name,
        "salary": obj.salary
    }
    print(dt)

    # 8. Save to the file
    with open(fileName, 'w') as file:
        json.dump(dt, file)


## Pickle ###################################################

import pickle

def PickleStorage(fileName):
    # 1. Create Employee object
    emp = Employee(111, "Rakesh", 100000)

    # 2. Save object to a file
    with open(fileName, "wb") as file:
        pickle.dump(emp, file)

def PickleModifyFile(fileName):
    # 3. Read from file to object
    with open(fileName, 'rb') as file:
        obj = pickle.load(file)
    print(obj)

    # 4. Modify the object
    obj.salary += 5000
    print(obj)

    # 5. Save object to a file
    with open(fileName, 'wb') as file:
        pickle.dump(obj, file)


############################################################
if __name__ == "__main__":
    # JSON 
    # JSONStorage("Employee.json")
    print("-" * 80)
    JSONModifyData("Employee.json")
    print("\n", "-" * 80, "\n")

    # Pickle
    # PickleStorage('Employee.pkl')
    PickleModifyFile('Employee.pkl')
