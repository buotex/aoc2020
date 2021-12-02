using Test
using StatsBase
using OffsetArrays

io = read(open("puzzles/2016/day10_input.txt", "r"), String);
vals = Dict()
passoff = Dict()
re_pass = r"bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)"
re_init = r"value ([0-9]+) goes to bot ([0-9]+)"

for line in map(strip, split(io, "\n"))
    if length(line) > 0
        if occursin(re_pass, line)
            my_match = match(re_pass, line)
            passoff[my_match.captures[1]] = NamedTuple{(:low_target, :low_num, :high_target, :high_num)}((my_match.captures[2], my_match.captures[3], my_match.captures[4], my_match.captures[5]))

        else
            my_match = match(re_init, line)
            val = get(vals, my_match.captures[2], [])
            vals[my_match.captures[2]] = vcat(val, my_match.captures[1])
        end

    end
end
println(vals)
println(passoff)
while ! isempty(filter(x -> length(x) == 2, collect(values(vals))))
    my_keys = filter(x -> length(vals[x]) == 2, keys(vals))
    for key in my_keys
        _vals = sort(vals[key])
        println(_vals[1])
        println(_vals[2])
        println("wtf")
        target = passoff[key]
        if _vals[1] == "17" && _vals[2] == "61"
            println(key)
        end
        if target.low_target == "bot"
            if length(get(vals, target.low_num, [])) == 2
                continue
            end
            vals[target.low_num] = vcat(get(vals, target.low_num, []), _vals[1])
        end
        if target.high_target == "bot"
            if length(get(vals, target.high_num, [])) == 2
                continue
            end
            vals[target.high_num] = vcat(get(vals, target.high_num, []), _vals[1])
        end
        delete!(vals, key)
    end
end
#println(vals)
