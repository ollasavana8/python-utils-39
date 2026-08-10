import time
import functools

# A decorator to measure the performance of functions

def performance_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f'Performance: {func.__name__} executed in {execution_time:.6f} seconds')
        return result
    return wrapper

# Example function to demonstrate performance measurement
@performance_measure
def compute_factorial(n):
    if n == 0:
        return 1
    return n * compute_factorial(n - 1)  # Recursive call

if __name__ == '__main__':
    result = compute_factorial(10)  # Call function to see performance
    print(f'Factorial Result: {result}')