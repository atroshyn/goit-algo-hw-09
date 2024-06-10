def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin
                
    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
        
    return result

# Приклад використання
amount = 113
print("Динамічне програмування:", find_min_coins(amount))  # {50: 2, 10: 1, 2: 1, 1: 1}
