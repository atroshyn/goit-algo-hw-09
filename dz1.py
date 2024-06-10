def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
            
    return result

# Приклад використання
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))  # {50: 2, 10: 1, 2: 1, 1: 1}
