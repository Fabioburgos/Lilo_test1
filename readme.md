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
    100,10,2