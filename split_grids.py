#!/usr/bin/env python3
import sys
import os

def split_grids(input_file, output_dir='grids'):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the input file containing all grids
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    current_grid = []
    grid_number = 1

    # Process each line in the input file
    for line in lines:
        # Check if the line contains a grid number
        if line.startswith('Grid'):
            # If the current grid is not empty, save it to a file
            if current_grid:
                save_grid(current_grid, grid_number, output_dir)
                grid_number += 1
                current_grid = []
        else:
            # Add the current line to the current grid, stripping any trailing whitespace
            current_grid.append(line.strip())

    # Save the last grid after the loop ends
    if current_grid:
        save_grid(current_grid, grid_number, output_dir)

def save_grid(grid, grid_number, output_dir):
    # Format the grid number with leading zeros
    formatted_number = str(grid_number).zfill(2)
    filename = os.path.join(output_dir, f'grid{formatted_number}.txt')
    # Join the grid lines with newline characters and save to a file
    with open(filename, 'w') as file:
        file.write('\n'.join(grid))

# Replace 'all_grids.txt' with the path to your input file
split_grids('all_grids.txt')
