#!/bin/bash

day=$1
cp puzzles/template.py puzzles/day${day}_solver.py
sed -i "s/dayx_input/day${day}_input/g" puzzles/day${day}_solver.py
wslview https://adventofcode.com/2020/day/${day}
python -c "from aocd.models import Puzzle; print(Puzzle(year=2020, day=${day}).input_data)" > puzzles/day${day}_input.txt

