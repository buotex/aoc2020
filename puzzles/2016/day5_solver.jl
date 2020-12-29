using Debugger
using Test

function task(input)
    for line in map(strip, split(input, "\n"))
        if length(line) > 0
            println(line)
        end
    end
    return input
end
testinput = """
"""
# @test task(testinput) == 0
io = read(open("puzzles/2016/day5_input.txt", "r"), String)
task(io)
