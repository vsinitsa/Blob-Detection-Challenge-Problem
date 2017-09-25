# Blob-Detection-Challenge-Problem

If we have a data set like this:  
O O O O X O O O O  
O O X X O O O O O  
X X X X O O O O X  
O O O X O O O X X  
O O X X X O O X O  
O X X O O O X O O  
O X X X X X O O O  

The premise of the problem is to find the biggest chunk of X's and the biggest chunk of O's.
Chunks are defined as X's or O's that are touching in the 4 cardinal directions (ie up, down, left, and right).

Input:
Input will be a text file of X's and O's with spaces in between and newlines at the end of each row.
The input file will not exceed 250 by 250

Output:
Output will be a dictionary of the size of the largest X chunk and O chunk.

Example:
For the data set  
X X O  
X O O  
O X X  

The output will be
{'X': 3, 'O': 3}

