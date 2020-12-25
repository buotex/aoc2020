function do_step!(cups_dict, current_cup, max_cup=1000001)
    cup1 = cups_dict[current_cup]
    cup2 = cups_dict[cup1]
    cup3 = cups_dict[cup2]
    follow_cup = cups_dict[cup3]
    destination_cup = (current_cup - 1) % max_cup
    while (!(haskey(cups_dict, destination_cup))) || destination_cup in [cup1, cup2, cup3]
        destination_cup = mod(destination_cup - 1,  max_cup)
    end
    follow_destination = cups_dict[destination_cup]
    cups_dict[destination_cup] = cup1
    cups_dict[current_cup] = follow_cup
    cups_dict[cup3] = follow_destination
    return cups_dict, follow_cup
end

input = [2,5,3,1,4,9,8,6,7]
for i in 10:1000000
    append!(input, i)
end
cups_dict = Dict{Int, Int}()
sizehint!(cups_dict, 1000000)
for (inp1, inp2) in zip(input, append!(input[2:end], input[1]))
    cups_dict[inp1] = inp2
end
current_cup = input[1]
function do_iterations(cups_dict, current_cup, max_cup)
    for _ in 1:10000000
        cups_dict, current_cup = do_step!(cups_dict, current_cup)
    end
    result1 = cups_dict[1]
    result2 = cups_dict[result1]
    return result1, result2
end
do_iterations(cups_dict, current_cup, 1000001)
