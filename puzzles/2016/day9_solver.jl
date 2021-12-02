using Test
using StatsBase
using OffsetArrays

io = read(open("puzzles/2016/day9_input.txt", "r"), String);
count = 0
input = strip(join(collect(io)));
function expand(data)
    current_pointer = 1
    while occursin(r"\(", data[current_pointer:end])
        i1= findfirst(isequal('('), data[current_pointer:end]) + current_pointer - 1
        i2= findfirst(isequal(')'), data[current_pointer:end]) + current_pointer - 1
        token = data[i1:i2]
        numbers=map(x -> parse(Int, x.match), collect(eachmatch(r"[0-9]+", token)))
        next_token = data[i2+1:i2+numbers[1]]
        data = join(vcat(data[begin:i1-1], repeat(next_token, numbers[2]), data[i2+numbers[1]+1:end]))
        current_pointer = i1 + numbers[2] * length(next_token)
    end
    println(length(data))
    return data
end
testinput = """A(2x2)BCD(2x2)EFG"""
testinput2 = "X(8x2)(3x3)ABCY"
print(expand(input))
# @test task(testinput) == 0
