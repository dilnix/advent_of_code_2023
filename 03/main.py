"""
There is a file named "input" with a 2D array of objects:
- empty space, which is a dot (.)
- connecting nodes, to which the part numbers are connected, use special characters (@, #, $, %, &, *, +, -, =, /)
- part numbers, which are numbers with dynamic size from 1 to 3 digits
The connection rule is that each part number can be connected to nodes only by adjacent sides (up, down, left,
right) and diagonally. The connection between part numbers is not needed to be checked.
The task is to find all part numbers in the map which are connected to nodes and sum their numbers.
The part numbers which are not connected to nodes should be ignored.
"""
