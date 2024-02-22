#!/bin/bash

# create tests directory if it doesn't exist
mkdir -p tests

# loop through each grid file
for i in $(seq -w 1 50); do
    # create directory for each grid inside the tests directory
    mkdir -p "tests/$i"

    # define file names based on the current grid number
    puzzleInput="inputs/grid$i.txt"
    puzzleOutput="outputs/$i/puzzle$i.cnf"
    assignOutput="outputs/$i/assign$i.txt"
    statOutput="outputs/$i/stat$i.txt"
    solutionOutput="outputs/$i/solution$i.txt"

    # run the commands for each grid
    ./sud2sat.py < "$puzzleInput" > "$puzzleOutput"
    minisat "$puzzleOutput" "$assignOutput" > "$statOutput"
    ./sat2sud.py < "$assignOutput" > "$solutionOutput"

    # echo progress
    echo "Processed Grid $i"
done

echo "All grids processed."
