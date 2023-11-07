#constructor
#default constructor

class Employee:
    def fullName(self, fName, lName):
        print(fName+lName)
emp = Employee()
emp.fullName("Thulasi","Latha")

#parameters constructor

class Employee:
    def _init_(self):
        pass
    def fullName(self, fName, lName):
        print(fName+lName)
emp = Employee()
emp.fullName("Thulasi","Hari")

#parameterized constructor

class Employee:
     _fName: str = " "
     _lName: str = " "
     def _init_(self, fName, lName):
        self._fName = fName
        self._lName = lName
     def fullName(self):
        print(self._fName + self._lName)
emp = Employee("thulasi","latha")
emp.fullName()