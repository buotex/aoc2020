using Debugger
using Test

function task(input)
    count = 0
    for line in map(strip, split(input, "\n"))
        arr = [parse(Int, x.match) for x in collect(eachmatch(r"\w+", line))]
        println(arr)
        if length(arr) > 0
            arr = sort!(arr)
            if arr[1] + arr[2] > arr[3]
                count += 1
            end
        end
    end
    return count
end
function task2(input)
    count = 0
    big_arr = []
    for line in map(strip, split(input, "\n"))
        arr = [parse(Int, x.match) for x in collect(eachmatch(r"\w+", line))]
        if length(arr) > 0
            big_arr = cat(big_arr, arr', dims=1)
        end
    end
    big_arr = reshape(big_arr, 3, :)
    for i in range(1, length=size(big_arr)[2])
        query = sort(big_arr[:, i])
        if query[1] + query[2] > query[3]
            count += 1
        end
    end

    return count
end
testinput = """
"""
# @test task(testinput) == 0
io = read(open("puzzles/2016/day3_input.txt", "r"), String)
task2(io)
