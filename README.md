Ritika Jain

- **Plain Python (`math.factorial` or standard integers):** Python automatically handles arbitrarily large integers by assigning more memory as numbers grow, which allows it to calculate `33!` precisely without overflow.
- **NumPy (`np.int64`):** Uses fixed 64-bit integer representation in memory. The value of `33!` exceeds the maximum limit for a signed 64-bit integer , causing integer overflow and returning an incorrect negative or wrapped value.

# Signal Statistics Project

This Python script generates, reads, and analyzes a noisy sine wave using only standard Python without relying on external libraries like NumPy or Pandas. 

## How to Run the Script
 The program will prompt you to type in custom values for the number of samples, frequency, and noise level. It will then automatically create a text file named `signal.txt`, calculate all the required statistics, run built-in self-checks, and print the results to your screen.

## Project Summary & Functionality
The script is broken down into steps. First, it generates a noisy wave using mathematical sine functions and a fixed random seed so that the output stays consistent every time it runs, saving the numbers line by line. Next, it includes a loading function that reads the saved file, ignores any empty or blank lines, and converts the text into a clean list of numbers. 

For data analysis, the script computes the mean, maximum, and minimum values using custom loops instead of relying on banned built-in shortcuts like `sum()`, `max()`, or `min()`. It also features a moving average function built with list slicing (defaulting to a window size of 5), a peak-counting function that tracks upward threshold crossings, and a binning tool that organizes the data into ordered `0.5`-wide frequency intervals. Finally, everything is tied together inside a main control function equipped with robust error handling for empty files and `assert` statements to verify that our custom math matches standard Python modules.
