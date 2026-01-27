Python Sorting Algorithm Benchmark
A simple command-line interface (CLI) application designed to demonstrate and compare the performance of classic sorting algorithms. The tool reads numeric data from a text file, sorts it using a chosen algorithm, and outputs both the sorted results and the execution time.

Features
Multiple Algorithms: Includes implementations for:

Bubble Sort: A simple comparison-based algorithm.

Insertion Sort: Efficient for small data sets or nearly sorted data.

Merge Sort: A divide-and-conquer algorithm optimized for larger datasets (includes recursion depth handling for up to 10,000+ items).

Data Parsing: Automatically cleans and extracts integers from a dataset.txt file, handling potential tags or brackets.

Performance Tracking: Measures and displays the exact time taken to sort the data in seconds.

Prerequisites
To run this application, you only need:

Python 3.x installed on your system.

No external libraries are required (uses standard time and sys modules).

How to Run
'' python "Prelim LabWork 2/bim.py" ''

Usage
Upon launching, you will see the Sorting Menu.

Select an algorithm by typing the corresponding number (1-3) and pressing Enter.

The program will:

Load the data from dataset.txt.

Perform the sort.

Print the sorted list in a single column.

Display the total Time Spent for the operation.

To close the application, select option 4.