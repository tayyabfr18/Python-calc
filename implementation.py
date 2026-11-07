"""
Project: Simple Calculator with Execution Time & Complexity Analysis
Student Name: Muhammad Tayyab
Student ID: 24SP-014-CS

Description:
This script performs various calculator operations, measures their execution
time precisely using time.perf_counter(), and documents their theoretical
time and space complexities.
"""

import time
import math

class ComplexityCalculator:
    """A calculator that records execution metrics and complexity profiles."""

    def __init__(self):
        print("=" * 65)
        print(" Initializing Calculator Module...")
        print(f" Student: Muhammad Tayyab | ID: 24SP-014-CS")
        print("=" * 65)

    def measure_execution(self, func, *args):
        """Helper method to measure execution time of any calculator function."""
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        
        # Calculate elapsed time in microseconds (µs)
        elapsed_time_us = (end_time - start_time) * 1_000_000
        return result, elapsed_time_us

    # --- Arithmetic Operations ---
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(x)

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(n)


if __name__ == "__main__":
    calc = ComplexityCalculator()

    # Test cases with complexity profiles
    operations = [
        ("Addition", calc.add, (158942, 98451), "Time: O(1) | Space: O(1)"),
        ("Multiplication", calc.multiply, (1234, 5678), "Time: O(1) | Space: O(1)"),
        ("Exponentiation", calc.power, (5, 100), "Time: O(log b) | Space: O(1)"),
        ("Square Root", calc.square_root, (144.0,), "Time: O(1) | Space: O(1)"),
        ("Factorial", calc.factorial, (20,), "Time: O(n) | Space: O(n) [Due to call stack]"),
    ]

    print("\n" + "-" * 75)
    print(f"{'Operation':<18} | {'Result':<15} | {'Execution Time':<15} | {'Complexity'}")
    print("-" * 75)

    for name, func, args, complexity in operations:
        try:
            res, duration = calc.measure_execution(func, *args)
            print(f"{name:<18} | {str(res):<15} | {duration:.4f} µs     | {complexity}")
        except Exception as e:
            print(f"{name:<18} | Error: {e}")

    print("-" * 75)
    print("Execution and complexity benchmark complete successfully!")
