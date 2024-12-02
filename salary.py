import employee
name = str(input("enter the name of the employee: "))
basic_salary = float(input("Enter the basic salary of employee :"))

da = employee.DA(basic_salary)
print("DA = ",da)

hra = employee.HRA(basic_salary)
print("HRA = ",hra)

pf = employee.PF(basic_salary)
print("PF = ",pf)

itax = employee.ITAX(basic_salary)
print("ITAX = ",itax)

gross_salary = basic_salary + da + hra
net_salary = gross_salary - pf - itax

print("Basic Salary = ",basic_salary)
print("Net salary = ",net_salary)
 