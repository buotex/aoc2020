using Debugger
using Test

function task(input)
    last_letter = [2,2]
    movement = Dict([("U", [0,-1]), ("L", [-1,0]), ("R",  [1,0]),( "D",  [0,1])])
    positions = []
    for instruction in map(strip, split(input))
        for letter in eachmatch(r"\w", instruction)
            last_letter .+= get(movement, letter.match, nothing)
            last_letter = min.(last_letter, [3,3]) 
            last_letter = max.(last_letter, [1,1]) 
        end
        push!(positions, copy(last_letter))
    end
    array = [1 4 7; 2 5 8; 3 6 9]
    println(positions)
    return [array[CartesianIndex(Tuple(pos))] for pos in positions]
    #return input
end
function task2(input)
    last_letter = CartesianIndex(3,3)
    movement = Dict([("U", (0,-1)), ("L", (-1,0)), ("R",  (1,0)),( "D",  (0,1))])
    positions = []
    array = [0 0 5 0 0; 0 2 6 0xA 0; 1 3 7 0xD 0xD; 0 4 8 0xC 0; 0 0 9 0 0]

    for instruction in map(strip, split(input))
        for letter in eachmatch(r"\w", instruction)
            new_letter = last_letter
            new_letter += CartesianIndex(get(movement, letter.match, nothing))
            if (checkbounds(Bool, array, new_letter) && array[new_letter] != 0)
                last_letter = new_letter
            end
        end
        push!(positions, last_letter)
    end
    println(positions)
    return [array[pos] for pos in positions]
    #return input
end
testinput = """
ULL
RRDDD
LURDL
UUUUD
"""
#@test task(testinput) == 0
io = read(open("puzzles/2016/day2_input.txt", "r"), String)
println(task(io))
println(task2(io))
