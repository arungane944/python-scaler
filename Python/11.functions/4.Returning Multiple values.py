def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count != 0 else 0
    return total, count, average

# Example usage
numbers = [10, 20, 30, 40, 50]
total, count, average = calculate_statistics(numbers)
print(f"Total: {total}, Count: {count}, Average: {average}")
