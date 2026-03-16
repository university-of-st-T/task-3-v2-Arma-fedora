prices = [100, 200, 300]

def calculate_total(prices, *discounts , **options):
    sum_prices = 0
    for i in prices:
        sum_prices+=i
    for j in discounts:
        sum_prices=sum_prices*(100-j)/100
    sum_prices = sum_prices*(options.get('tax', 0)+100)/100
    sum_prices = float(round(sum_prices, options.get('round_to', 0)))
    return sum_prices
prices = [100, 200, 300]
print(calculate_total(prices, 10, 5, tax=20, round_to=1))