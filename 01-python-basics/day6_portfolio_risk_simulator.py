import numpy as np

portfolio_start_value = 10000
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
means = np.array([0.0005, 0.0004, 0.0008, 0.0005, 0.0002])
volatilities = np.array([0.02, 0.018, 0.035, 0.022, 0.04])

# single day return

random_daily_return = np.random.normal(means, volatilities)

print(f'AAPL {random_daily_return[0]}')
print(f'MSFT {random_daily_return[1]}')
print(f'NVDA {random_daily_return[2]}')
print(f'GOOGL {random_daily_return[3]}')
print(f'TSLA {random_daily_return[4]}')

single_day_portfolio_return = np.sum(random_daily_return * weights)
single_day_growth_factor = 1 + single_day_portfolio_return

print(single_day_portfolio_return)
print(single_day_growth_factor)

# simulate 252 trading days (1 year)

portfolio = np.zeros((252, 1))
portfolio_return = np.zeros((252, 1))
portfolio_value = portfolio_start_value

for i in range(252):
    random_return_i = np.random.normal(means, volatilities)

    daily_portfolio_return = np.sum(random_return_i * weights)
    daily_growth_factor = 1 + daily_portfolio_return

    portfolio_return[i] = daily_portfolio_return
    portfolio_value = portfolio_value * daily_growth_factor
    portfolio[i] = portfolio_value

final_value = portfolio[-1]
total_return = (final_value - portfolio_start_value)
mean_daily_return = np.mean(portfolio_return)
daily_volatility = np.std(portfolio_return)
best_day = np.max(portfolio_return)
worst_day = np.min(portfolio_return)

print(f'Mean daily return {mean_daily_return}')
print(f'Daily volatility {daily_volatility}')
print(f'Best day {best_day}')
print(f'Worst day {worst_day}')


print(f'Final portfolio value {final_value.item()}. ')
print(f'Total return {total_return.item()}.')

# simulate the year 1000 times 

simulations = np.zeros(1000)

for j in range(1000):
    portfolio_value = portfolio_start_value

    for k in range(252):
        random_return_k = np.random.normal(means, volatilities)
        
        daily_portfolio_return = np.sum(random_return_k * weights)
        daily_growth_factor = 1 + daily_portfolio_return

        portfolio_value = portfolio_value * daily_growth_factor

    simulations[j] = portfolio_value

mean_final_value = np.mean(simulations)
median_final_value = np.median(simulations)
standard_dev = np.std(simulations)
best = np.max(simulations)
worst = np.min(simulations)

print(f'After 1000 simulated trading years, the best outcome was {best}'
      f' and the worst outcome was {worst}. The mean portfolio value was'
      f' {mean_final_value} and the median was {median_final_value}.'
      f' The standard deviation was {standard_dev}')

prob_1 = np.mean(simulations>11000)
prob_2 = np.mean(simulations>15000)
prob_3 = np.mean(simulations<portfolio_start_value)

print(f'The probability the portfolio finishes above £11,000 is {prob_1}.')
print(f'The probability the portfolio finishes above £15,000 is {prob_2}.')
print(f'The probability the portfolio loses money is {prob_3}.')
