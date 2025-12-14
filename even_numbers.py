def get_even_numbers(start, end):
    """Get all even numbers in the given range (inclusive)."""
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


if __name__ == "__main__":
    start = 1
    end = 50

    even_nums = get_even_numbers(start, end)

    print(f"Even numbers between {start} and {end}:")
    print(even_nums)
    print(f"\nTotal count: {len(even_nums)} even numbers")
