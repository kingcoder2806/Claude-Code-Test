def count_numbers(start, end):
    """Count numbers from start to end (inclusive)."""
    numbers = []
    for num in range(start, end + 1):
        numbers.append(num)
    return numbers


if __name__ == "__main__":
    start = 1
    end = 20

    numbers = count_numbers(start, end)

    print(f"Numbers from {start} to {end}:")
    print(numbers)
    print(f"\nTotal count: {len(numbers)} numbers")
