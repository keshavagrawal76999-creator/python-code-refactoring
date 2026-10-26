def sum_positive_numbers(numbers):
    """Return the sum of values greater than zero."""
    return sum(number for number in numbers if number > 0)


def main():
    sample_numbers = [2, -3, 4, 0]
    total = sum_positive_numbers(sample_numbers)
    print(f"Sum of positive numbers: {total}")


if __name__ == "__main__":
    main()
