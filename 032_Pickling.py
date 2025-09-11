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



############################################################
if __name__ == "__main__":
    JSONStorage("Employee.json")
    print("-" * 80)
    JSONModifyData("Employee.json")