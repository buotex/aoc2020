using Debugger
using Test
using StatsBase

function task(input)
    all_letters = map(x -> x.match, collect(eachmatch(r"\w", input)));
    all_letters = reshape(all_letters, 8, :);
    for i in range(1, stop=8)
        counts = countmap(all_letters[i,:]);
        letter = sort(collect(counts), by=x->x[2])[1]
        print(letter)

        #print(letter)
    end
    return 
end
testinput = """
"""
# @test task(testinput) == 0
io = read(open("puzzles/2016/day6_input.txt", "r"), String)
task(io)
