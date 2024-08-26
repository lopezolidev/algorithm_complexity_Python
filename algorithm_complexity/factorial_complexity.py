import time
import sys

sys.setrecursionlimit(150000)
# we must alter this recursion limit only of the sake of the exercise

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n-1)

def iterative_factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i


print("Start recursive factorial: ")
start = time.time()
recursive_factorial(19375)
print("End recursive factorial: ")
end = time.time()
print("Total time: ", end - start) # → 0.10207676887512207
# measuring time complexity of recursive factorial

print("\n")
print("Start iterative factorial: ")
start = time.time()
iterative_factorial(19375)
print("End iterative factorial: ")
end = time.time()
print("Total time: ", end - start) # → 0.09558415412902832
# Same for iterative factorial

# the iterative factorial is slightly more efficient regarding time than the recursive one