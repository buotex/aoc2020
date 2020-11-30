#!/bin/bash

day=$1
wget https://adventofcode.com/2020/day/${day}/input -o puzzles/day${day}_input.txt
cp puzzles/template.py puzzles/day${day}_solver.py
