def read_numbers_in_file(filename):
    # Reads numbers from a file
    numbers = []
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
                line = line.strip()
                if line:  # avoids empty lines
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"non-numeric value Skipped : {line}")

            # handle Empty file
            if line_count == 0:
                print(f" File'{filename}' is empty or contains no valid numbers, please enter numbers into the file.")
            elif len(numbers) == 0:
                print(f"File '{filename}' contains no valid numbers.")

        return numbers
    except FileNotFoundError:
        print(f"Error File '{filename}' was not found.")
        return None


def find_min_max(numbers):
    """Finds minimum and maximum values in a list."""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


def show_results(numbers, min_val, max_val):

    print("-" * 20)
    print("MIN AND MAX RESULTS")
    print("-" * 20)
    print(f"Amount of numbers Used: {len(numbers)}")
    print(f"Numbers: {numbers}")
    if min_val is not None:
        print(f"Minimum: {min_val}")
        print(f"Maximum: {max_val}")
    else:
        print("No valid numbers was found.")


def main():
    print("MINIMUM AND MAXIMUM FINDER")
    print("-" * 25)

    filename = "user_numbers.txt"  #  uses user_numbers file

    # Read numbers from the file
    numbers = read_numbers_in_file(filename)

    if numbers is None:
        return

    # Finds min and max
    min_val, max_val = find_min_max(numbers)

    # Display results
    show_results(numbers, min_val, max_val)


if __name__ == "__main__":
    main()
