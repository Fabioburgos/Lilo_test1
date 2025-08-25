# Subset Sum Solver for CSV Data

## Project Overview

This project provides a Python script to solve a variation of the classic **Subset Sum Problem**. It reads data from a CSV file where each row contains a "big number" followed by a list of "small numbers." For each row, the program finds the combination of small numbers whose sum is as close as possible to the big number without exceeding it.

This solution was developed as a technical challenge, demonstrating an elegant and efficient approach to a complex problem.

## Features

* **CSV Input**: Reads data directly from a `.csv` file located in a `data/` subfolder.
* **Optimal Solution**: Uses a dynamic programming approach to guarantee the best possible combination of numbers is found.
* **Clear Output**: Prints the selected numbers and their sum for each row in the input file.
* **Error Handling**: Includes basic error handling for file-not-found and data formatting issues.

## How to Run the Solution

1.  **Prerequisites**: Ensure you have Python 3 installed on your system.

2.  **Project Structure**: The project is structured with a main execution script and a separate module for the core logic. Place your input CSV file inside a folder named `data`.

    ```
    .
    ├── data/
    │   └── input.csv
    ├── main.py               # Main script to run the program
    └── processcsv.py         # Module containing the solver logic
    ```

3.  **Prepare your data**: Your `input.csv` file should be formatted with comma-separated numbers. The first number in each row is the target ("big number"), and the rest are the numbers to choose from ("small numbers").

    *Example `input.csv` content:*
    ```csv
    100,10,20,30,40,50
    250,23,56,12,89,4,98
    50,15,17,2,8,25
    ```

4.  **Execute the Script**: Run the `main.py` script from your terminal:
    ```bash
    python main.py
    ```

5.  **View the Output**: The script will print the results directly to the console.

    *Example Output:*
    ```
    Processing 'data/input.csv'...
    Row 1:
      Selected Numbers: [10, 20, 30, 40]
      Sum: 100

    Row 2:
      Selected Numbers: [23, 56, 12, 89, 4, 98]
      Sum: 248

    Row 3:
      Selected Numbers: [15, 17, 8, 25]
      Sum: 48
    ```

## Approach and Justification

The chosen approach to solve this problem is **dynamic programming**, a well-suited technique for optimization challenges like the Subset Sum Problem. This method is considered the best fit because it guarantees finding the optimal solution by systematically exploring all valid combinations. Its main advantage is its correctness and efficiency given the problem's constraints (up to 12 "small numbers"). However, a potential limitation is its performance scalability; the memory and time required would increase significantly if the input lists were much larger, which might necessitate the use of approximation algorithms in a different context.