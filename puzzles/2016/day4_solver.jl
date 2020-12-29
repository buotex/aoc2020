using Debugger
using Test
using StatsBase

function task(input)
    valid_count = 0
    for line in map(strip, split(input,"\n"))
        if length(line) > 0
            tokens = match(r"([^[]+)\[(\w+)\]", line)
            letters = countmap(tokens.captures[1])
            checksum = tokens.captures[2]
            room_number = parse(Int, match(r"[0-9]+", line).match)
            sorted_letters = filter(x->! isnothing(match(r"[a-z]", string(x[1]))), sort(collect(letters), by=x -> x[1]))
            sorted_letters = sort(sorted_letters, alg=InsertionSort, by=x -> x[2], rev=true)
            valid = true
            for (l_name, l_checksum) in zip(map(x -> x[1], sorted_letters), checksum)
                if l_name != l_checksum
                    valid = false
                    break
                end
            end
            if valid == true
                valid_count += room_number
                # rotate letters
                words = map(x->Int(x) - Int('a'), collect(tokens.captures[1]))
                words_shifted = join(map(x -> Char(x + Int('a')), map(x -> mod(x + room_number, 26), words)))
                if ! isnothing(match(r"north", words_shifted))
                    println(room_number, words_shifted)
                end
            end

        end
    end
    return valid_count
end
testinput = """
"""
# @test task(testinput) == 0
io = read(open("puzzles/2016/day4_input.txt", "r"), String);
task(io)
