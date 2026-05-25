'''find min max and average salary of employee by considering above salary list'''
# salary=[67000,45000,78000,55000,28000,44000,33000] 
# minimum=min(salary)
# maximum=max(salary)  
# avg=sum(salary)/len(salary)
# print("Minimum :",minimum)
# print("Maximum :",maximum)
# print("Average :",avg)

salary=[67000,45000,78000,55000,28000,44000,33000] 
minimum=min(salary)
maximum=max(salary)
total=0
for i in salary:
    total=total+i
avg=total/len(salary)
print("Average :",avg)
print("Minimum :",minimum)
print("Maximum :",maximum)