# Жадібні алгоритми і динамічне програмування
Цей файл README.md надає короткий опис функцій, приклади їх використання та порівняння ефективності алгоритмів.

## Касова система для видачі решти

## Опис

Цей проект включає дві функції для видачі решти покупцеві за допомогою монет заданих номіналів. Перша функція використовує жадібний алгоритм, а друга - метод динамічного програмування.

## Вхідні дані

- Набір монет: [50, 25, 10, 5, 2, 1]
- Сума, яку потрібно видати як решту

## Функції

### 1. Жадібний алгоритм

Функція `find_coins_greedy` приймає суму, яку потрібно видати покупцеві, і повертає словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми.

```python
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

### 2. Динамічне програмування

```python
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
