print("Empoyee Salary Caluculator")

Salary = 50000;
Bonus = "5000";

try:

    total_salary = Salary + Bonus;

    print("Emloyee total Salary is:",total_salary);

except TypeError:
    print("error: cannot perform operation on incompatible data types. Please check the data types of Salary and Bonus. ");

