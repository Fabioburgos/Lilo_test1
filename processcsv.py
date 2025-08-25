import csv
import os # Import the os module to handle file paths and directories

def solve_subset_sum(big_number, small_numbers):
    """
    Finds the subset of small_numbers that sums closest to big_number without exceeding it.
    This function uses a dynamic programming approach, similar to the 0/1 knapsack problem.

    Args:
        big_number (int): The target number.
        small_numbers (list): A list of numbers to choose from.

    Returns:
        tuple: A tuple containing the list of selected numbers and their sum.
    """
    # dp stores the achievable sums and the combinations to get them.
    dp = {0: []}
    
    # Iterate through each small number
    for num in small_numbers:
        # Create a new dictionary to store the sums we can make with the current number
        new_sums = {}
        for current_sum, combination in dp.items():
            new_sum = current_sum + num
            # If the new sum is within our target and we haven't found a combination for it yet
            if new_sum <= big_number:
                if new_sum not in dp:
                    new_sums[new_sum] = combination + [num]
        # Update our main dp table with the new sums found
        dp.update(new_sums)

    # Find the sum in our dp table that is closest to the big_number
    best_sum = 0
    # Iterate through all possible sums we've calculated
    for s in dp.keys():
        if s > best_sum:
            best_sum = s
            
    return dp.get(best_sum, []), best_sum

def process_csv(file_path):
    """
    Reads a CSV file, processes each row to solve the subset sum problem,
    and prints the result.

    Args:
        file_path (str): The path to the input CSV file.
    """
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if not row:
                    continue # Skip empty rows
                try:
                    # Convert string numbers to integers
                    numbers = [int(n) for n in row]
                    big_number = numbers[0]
                    small_numbers = numbers[1:]
                    
                    # Solve the problem for the current row
                    selected_numbers, total_sum = solve_subset_sum(big_number, small_numbers)
                    
                    # Print the results
                    print(f"Row {i+1}:")
                    print(f"  Selected Numbers: {selected_numbers}")
                    print(f"  Sum: {total_sum}\n")

                except (ValueError, IndexError) as e:
                    print(f"Error processing row {i+1}: {e}. Please check the data format.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")