using Debugger
using Test
using StatsBase
using OffsetArrays


screen_arr = fill('.', 50, 6);
screen = OffsetArray(screen_arr, 0:49, 0:5);
io = read(open("puzzles/2016/day8_input.txt", "r"), String);
testinput = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""
for line in map(strip, split(io, "\n"))
    if length(line) > 0
        command = match(r"^\w+", line).match
        numbers = map(x -> parse(Int, x.match), collect(eachmatch(r"[0-9]+", line)))
        if command == "rect"
            global screen[0:numbers[1]-1, 0:numbers[2]-1] .= '#'
        else
            if occursin(r"x", line)
                dim = 1
                data = vcat(screen[numbers[1], end + 1-numbers[2]:end], screen[numbers[1], begin:end - numbers[2]])
                global screen[numbers[1], :] = data
            else
                dim = 2
                data = vcat(screen[ end + 1-numbers[2]:end,numbers[1] ], screen[begin:end - numbers[2], numbers[1]])
                global screen[:, numbers[1]] = data
            end
        end
    end
end
counts = countmap(screen)
println(counts['#'])

for i in axes(screen)[2]
    println(join(screen[:, i]))
end
