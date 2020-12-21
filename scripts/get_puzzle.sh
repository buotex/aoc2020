#!/bin/bash

day=$1

if [[ -z "$2" ]]; then
    year=2020
else
    year = $2
fi
cp $year/puzzles/template.py puzzles/$year/day${day}_solver.py
sed -i "s/dayx_input/day${day}_input/g" puzzles/$year/day${day}_solver.py
wslview https://adventofcode.com/$year/day/${day}
python -c "from aocd.models import Puzzle; print(Puzzle(year=$year, day=${day}).input_data)" > puzzles/$year/day${day}_input.txt

