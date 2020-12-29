using Debugger
using Test

count = 0
io = read(open("puzzles/2016/day7_input.txt", "r"), String);
abba = r"(\w)(?!\1)(\w)\2\1"
#big_regex=r"^(?:\w*|\[\w*\])*\w*(\w)(?!\1)(\w)\2\1\w*(?:\w*|\[\w*\])*$"
big_regex_pos=r"^(?:\w|\[\w*\])* (\w)(?!\1)(\w)\2\1 (?:\w|\[\w*\])*$"x
big_regex_neg=r"\[ \w* (\w)(?!\1)(\w)\2\1  \w* \]"x
ssl1 = r"(\w)(?!\1)(\w)\1(?:\w|\[\w*\])*\[\w*\2\1\2\w*\]"
ssl2 = r"\[\w*(\w)(?!\1)(\w)\1\w*\](?:\w|\[\w*\])*\2\1\2"
function is_valid(line)
    if occursin(big_regex_pos, line) && ! occursin(big_regex_neg, line)
        return true
    else
        println(line)
    end
    return false
end
function is_ssl(line)
    if occursin(ssl1, line) || occursin(ssl2, line)
        return true
    end
    return false
end
for line in map(strip, split(io, "\n"))
    if length(line) > 0
        if is_ssl(line)
            #println(line)
            global count += 1
        end
    end
end
testinput = """
"""
@test(is_valid("abba[mnop]qrst") == true)
@test(is_valid("abcd[bddb]xyyx") == false)
@test(is_valid("aaaa[qwer]tyui") == false)
@test(is_valid("ioxxoj[asdfgh]zxcvbn") == true)
@test(is_ssl("aba[bab]xyz") == true)
@test(is_ssl("xyx[xyx]xyx") == false)
@test(is_ssl("aaa[kek]eke") == true)
@test(is_ssl("zazbz[bzb]cdb") == true)
count
# @test task(testinput) == 0
