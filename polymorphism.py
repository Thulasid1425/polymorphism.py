#method overloading

class Calculation:
    def _add_(self, a:int, b:int):
        print(a+b)
    def _add_(self, a:int, b:int, c:int):
        print(a+b+c)
    def _add_(self, a:int, b:int, c:int=0):
        print(a+b+c)
    def _name_(self, a:str, b:str):
        print(a+ "" +b)
cal = Calculation()
cal._add_(2,5,6)
cal._add_(6,7,5)
cal._name_("Thulasi", "Latha")

#method overriding

class Employee:
    _amt = 30000
    def sal(self):
        return self._amt*12
class contractEmployee(Employee):
    _hrpay = 2000
    _hrs = 10
    def sal(self):
        return self._hrpay * self._hrs
emp = contractEmployee()
print(emp.sal())