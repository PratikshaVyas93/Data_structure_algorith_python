
"""
    List of expenses are defined below
"""
exp = [2200,2350,2600,2130,2190]
# Questions 1 # February month how many dollars spent extra compare to January
print(f"{exp[1]-exp[0]} spent extra in the month of February")
# Total first quaters expenses
print(f"{exp[0]+exp[1]+exp[2]} Total of first three month")
# Find out if ever spent 2000 dollar in any month
print(f"did i spend 2000 in any month: ", 2000 in exp)
# add expense in the month of june
exp.append(1980)
print(f"adding an item to exp for june {exp}")
""" You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this
"""
exp[3] = exp[3]-200
print(f"sfter adding bonus 200 in the month of appril {exp}")


# Operation 2 

heros=['spider man','thor','hulk','iron man','captain america']
print("len of the heros", len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)
heros.insert(3,'black panthe')
print(heros)
heros.remove('thor')
heros.remove('hulk')
heros.insert(1,'doctor strange')
print(heros)
print(heros.sort,"sorted list")
print(dir(heros),"heros in dir")

# operation 3
numbers = int(input("please enter number:"))
print("number",numbers)
list_odd = []
list_even = []
for i in range(1,numbers):
    if i%2!=0:
        list_odd.append(i)
        print(list_odd,"This is list of odd number")
    else:
        list_even.append(i)
        print(f" {list_even} List of even number")
