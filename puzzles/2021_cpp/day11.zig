const std = @import("std");
const stdout = std.io.getStdOut().writer();
const test_input = [12][12]i8{
    [_]i8{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    [_]i8{ 0, 5, 4, 8, 3, 1, 4, 3, 2, 2, 3, 0 },
    [_]i8{ 0, 2, 7, 4, 5, 8, 5, 4, 7, 1, 1, 0 },
    [_]i8{ 0, 5, 2, 6, 4, 5, 5, 6, 1, 7, 3, 0 },
    [_]i8{ 0, 6, 1, 4, 1, 3, 3, 6, 1, 4, 6, 0 },
    [_]i8{ 0, 6, 3, 5, 7, 3, 8, 5, 4, 7, 8, 0 },
    [_]i8{ 0, 4, 1, 6, 7, 5, 2, 4, 6, 4, 5, 0 },
    [_]i8{ 0, 2, 1, 7, 6, 8, 4, 1, 7, 2, 1, 0 },
    [_]i8{ 0, 6, 8, 8, 2, 8, 8, 1, 1, 3, 4, 0 },
    [_]i8{ 0, 4, 8, 4, 6, 8, 4, 8, 5, 5, 4, 0 },
    [_]i8{ 0, 5, 2, 8, 3, 7, 5, 1, 5, 2, 6, 0 },
    [_]i8{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
};
pub fn printer(comptime N: i16, mat: [N][N]i8) !void {
    try stdout.print("Matrix: {} {}\n", .{ N, N });
    for (mat) |row| {
        for (row) |item| {
            try stdout.print("{}", .{item});
        }
        try stdout.print("\n", .{});
    }
}
pub fn step(comptime N: i16, mat: [N][N]i8) [N][N]i8 {
    var new_mat = mat;
    for (mat) |row, i| {
        for (row) |item, j| {
            new_mat[i][j] = item + 1;
        }
    }
    return new_mat;
}
pub fn flashing(comptime N: i16, mat: [N][N]i8) [N][N]i8 {
    var has_changed = true;
    var is_flashing: [N][N]bool = std.mem.zeroes([N][N]bool);
    var octopi = mat;
    while (has_changed) {
        has_changed = false;
        for (octopi) |row, i| {
            if ((i == 0) or (i == N - 1)) continue;
            for (row) |item, j| {
                if ((j == 0) or (j == N - 1)) continue;
                // flashing
                if (item > 9) {
                    if (!is_flashing[i][j]){
                        has_changed = true;
                        is_flashing[i][j] = true;
                        }
                }
            }
        }
    }
    for (is_flashing) |row, i| {
        for (row) |item, j| {
                if (item) octopi[i][j] = 0;
            }
        }
    return octopi;
}

pub fn main() !void {
    try stdout.print("Hello world \n", .{});

    var data = test_input;
    try printer(12, data);
    data = step(12, data);
    try printer(12, data);
    data = flashing(12, data);
    try printer(12, data);
    data = step(12, data);
    data = flashing(12, data);
    try printer(12, data);
}
