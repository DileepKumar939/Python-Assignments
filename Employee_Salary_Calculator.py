print("Employee Salary Calculator");
print("-------------------------------");
name=input("Enter Employee Name: ")
salary=float(input("Enter Employee Basic Salary: "));
Bonus=float(input("Enter Employee Bonus; "));

totalsalary = salary + Bonus;
hra = salary*0.20;
gross= salary + hra + Bonus;

print("Employee Summary");
print("Employee Name: {name}");
print("Employee Total Salary: {totalsalary}");
print("Employee hra: {hra}");
print("Employee Gross Salary: ",gross);

if totalsalary>=50000:
    highEarner=True
else:
    highEarner=False;
    print("High Earner",highEarner);    