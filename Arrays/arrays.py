
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