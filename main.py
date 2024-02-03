salary = 1250.0
numDependents = 2

stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = numDependents * (salary * 0.025)
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

print("stateTax: $" + str(stateTax))
print("federalTax: $" + str(federalTax))
print("dependents: $" + str(dependentDeduction))
print("salary: $" + str(salary))
print("take-Home Pay: $" + str(takeHomePay))