result = 0
for num in range(1, 51):
    result = result + num
    
print(result)

for i in range(2, 10, 4):
    print(i)

numbers = [6, 1, 2, 3, 4, 5, 7, 8, 9, 10]
max_n = numbers[0]
for n in numbers:
    if n > max_n:
        max_n = n
print(max_n)

result = 0
for num in range(100):
    if num % 2 == 0:
        result += num
print("total result:", result)

result = 0
for num in range(5, 101,5):
    print(num)
    result += num
print("Total result:", result)