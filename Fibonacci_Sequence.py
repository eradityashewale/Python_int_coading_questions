def fibonacci(n: int) -> list:
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Test
print(fibonacci(10))  # Should return first 10 Fibonacci numbers
