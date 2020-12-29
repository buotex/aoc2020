io = read(open("puzzles/2016/day1_input.txt"), String)

let
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    position = [0, 0]
    visited = Set()
    dir = 0
    for entry in eachmatch(r"(L|R)(\w+)", io)
        direction = entry.captures[1]
        if direction == "L"
            dir = mod(dir - 1, 4)
        elseif direction == "R"
            dir = mod(dir + 1, 4)
        end
        distance = parse(Int, entry.captures[2])
        println(position)
        for d in range(1, stop=distance)
            position[1] += directions[dir + 1][1]
            position[2] += directions[dir + 1][2]
            if position in visited
                println(position)
                break
            end
            push!(visited, copy(position))
        end
        println(distance)
        println(position)
    end
    println(visited)

end
