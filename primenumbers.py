i = int(input('enter a starting number :'))
num = int(input('enter an ending number :'))
count = int(0)
for i in range(i, num):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"the no.of prime number between 0 to {num} are {count}.")
