# input budget, purchases and costs

budget = float(input('Budget:'))

number_purchases = int(input('How many purchases have you made?'))

expenses = []

for i in range(number_purchases):
    expense = {'name':input('Expense name:'), 'cost':float(input('Cost:'))}
    expenses.append(expense)

# turn costs from dictionary into a single list
costs = []

for expense in expenses:
    cost = expense['cost']
    costs.append(cost)

# calculate the largest expense
largest = expenses[0]
for expense in expenses:
    if expense['cost'] > largest['cost']:
        largest = expense

# calculate the total expendature 
def total(costs):
    return sum(costs)

#Output

print(f'Budget  =  £{budget}')

i = 1

for expense in expenses:
    print(f'Expense  {i}    ' 
          f'Name:  {expense['name']}    '
          f'Cost:  £{expense['cost']}')
    i += 1


print(f'Largest expense: {largest['name']} for £{largest['cost']}')

print(f'Total spent:  £{total(costs)}')

if total(costs) <= 0.5*budget:
    print('Comfortably within budget')
elif total(costs) <= budget:
    print('Within budget')
else:
    print('Over budget')