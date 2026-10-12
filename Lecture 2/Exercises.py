import numpy as np

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

a = np.arange(1, x * y + 1).reshape(x, y)

print("Matrix:")
print(a)
print("Sum:", np.sum(a))