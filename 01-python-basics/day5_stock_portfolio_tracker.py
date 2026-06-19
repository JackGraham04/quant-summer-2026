import csv

# all required function
def investment_value(a, b):
    return a*b

def profit(a, b):
    return b-a

def returns(a, b):
    return round(((profit(a, b))/a)*100, 2)

def total(*args):
    return sum(args)

def best_return(*args):

    best = args[0]

    for i in args:
        if (i['Return']) > (best['Return']):
            best = i
    
    return best

def worst_return(*args):

    worst = args[0]

    for i in args:
        if (i['Return']) < (worst['Return']):
            worst = i
    
    return worst


new_stock = 'y'
i = 1
portfolio = []
portfolio_outcome = []

# input all stock names, number of shares and share prices
while new_stock == 'y':
    stock_name_i = input('Stock name: ')
    shares_i = float(input('Number of shares purchased: '))
    price_i = float(input('Current share price: '))

    portfolio.append({'name': stock_name_i, 'shares': shares_i, 'price': price_i})

    i += 1

    new_stock = input('Would you like to add another stock to your portfolio? y/n ')

# calculate performance of each stock and store in portfolio
for stock in portfolio:
    new = float(input(f'New {stock['name']} share price? '))
    stock['new_price']=new

    investment = investment_value(stock['shares'], stock['price'])
    current = investment_value(stock['shares'], stock['new_price'])
    profit_loss = profit(investment, current)
    return_percentage = returns(investment, current)

    portfolio_outcome.append({'Name': stock['name'], 'Number_of_shares': stock['shares'],
                              'Initial_share_price': stock['price'], 
                              'Current_share_price': stock['new_price'], 
                              'Initial_investment': investment,
                              'Current_investment': current, 'Profit_Loss': profit_loss, 
                              'Return': return_percentage})

invested = []
current = []
profits = []

# output all stock metrics
for stock in portfolio_outcome:
    invested.append(stock['Initial_investment'])
    current.append(stock['Current_investment'])
    profits.append(stock['Profit_Loss'])
    print(stock['Name'])
    print('')
    print(f'Invested: £{stock['Initial_investment']}')
    print(f'Current Value: £{stock['Current_investment']}')
    print(f'Profit: £{stock['Profit_Loss']}')
    print(f'Return: {stock['Return']}%')
    print('')
    print('')

# calculate portfolio performance
total_invested = total(*invested)
total_current = total(*current)
total_profit = total(*profits)
total_return = returns(total_invested, total_current)
best_stock = best_return(*portfolio_outcome)
worst_stock = worst_return(*portfolio_outcome)

print(f'Total Invested: {total_invested}')
print(f'Total Current Value: {total_current}')
print(f'Total Profit: {total_profit}')
print(f'Total Return: {total_return}%')
print(f'Best performing stock: {best_stock['Name']}')
print(f'Worst performing stock: {worst_stock['Name']}')

# create csv file for portfolio
with open('01-python-basics/portfolio_results.csv', 'w', newline = '') as results_file:
    
    fieldnames = ['Name', 'Number_of_shares', 'Initial_share_price', 
                  'Current_share_price', 'Initial_investment', 'Current_investment',
                  'Profit_Loss', 'Return']
    
    writer = csv.DictWriter(results_file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(portfolio_outcome)