use ndarray;
use std::fs;
const TEST_INPUT: &str = "2199943210
3987894921
9856789892
8767896789
9899965678";

fn split_input(inp: &str) -> ndarray::Array2<u32> {
    let parsed: Vec<Vec<u32>> = inp
        .lines()
        .map(|x| x.chars().map(|y| y.to_digit(10).unwrap()).collect())
        .collect();
    let ncols = parsed.first().unwrap().len();
    let nrows = parsed.len();
    let mut flattened_vec = Vec::new();
    for row in parsed.iter() {
        flattened_vec.extend_from_slice(row);
    }
    println!("{}, {}", nrows, ncols);
    ndarray::Array2::from_shape_vec((nrows, ncols), flattened_vec).unwrap()
}
fn add_border(inp: &ndarray::Array2<u32>) -> ndarray::Array2<u32> {
    let mut new_array = ndarray::Array2::zeros((inp.shape()[0] + 2, inp.shape()[1] + 2));
    new_array.fill(10);
    new_array.slice_mut(s![1..-1, 1..-1]).assign(inp);
    new_array
}
fn find_minima(inp: &ndarray::Array2<u32>) -> ndarray::Array2<u32> {
    let nrows = inp.shape()[0];
    let ncols = inp.shape()[1];
    let mut minima_array = ndarray::Array2::zeros((inp.shape()[0] - 2, inp.shape()[1] - 2));
    for i in 1..nrows - 1 {
        for j in 1..ncols - 1 {
            //print!("{}", window);
            let neighbors = ndarray::array![
                inp[(i, j - 1)],
                inp[(i, j + 1)],
                inp[(i - 1, j)],
                inp[(i + 1, j)],
            ];
            let minimum: u32 = *neighbors.iter().min().unwrap();
            if inp[(i, j)] < minimum {
                minima_array[(i - 1, j - 1)] = inp[(i, j)] + 1;
            }
        }
    }
    minima_array
}

fn bfs(inp: &ndarray::Array2<u32>) -> Vec<u32> {
    let mut array_copy = inp.clone();
    for element in &mut array_copy {
        *element = (*element < 9) as u32;
    }
    println!("{}", array_copy);
    let mut basin_counts = Vec::new();
    let mut new_basin = Vec::new();
    loop {
        let mut finished = true;
        if new_basin.len() == 0 {
            for i in 1..array_copy.shape()[0] - 1 {
                for j in 1..array_copy.shape()[1] - 1 {
                    if array_copy[(i, j)] == 1 {
                        new_basin.push((i as i32, j as i32));
                        finished = false;
                        break;
                    }
                }
                if finished == false {
                    break;
                }
            }
        }

        if finished {
            let arr = ndarray::Array::from_vec(basin_counts.clone());
            println!("{}", arr);
            return basin_counts;
        } else {
            let mut count = 0;
            while new_basin.len() > 0 {
                let element = new_basin.pop().unwrap();
                if array_copy[(element.0 as usize, element.1 as usize)] == 1 {
                    count += 1;
                    array_copy[(element.0 as usize, element.1 as usize)] = 2;
                } else {
                    continue;
                }
                let neighbors: Vec<(i32, i32)> = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];
                for neighbor in &neighbors {
                    let neighbor_indices = ((element.0 + neighbor.0), (element.1 + neighbor.1));
                    if (neighbor_indices.0 == 0
                        || neighbor_indices.1 == 0
                        || neighbor_indices.0 == (array_copy.shape()[0] - 1) as i32
                        || neighbor_indices.1 == (array_copy.shape()[1] - 1) as i32)
                    {
                        continue;
                    }
                    if array_copy[(neighbor_indices.0 as usize, neighbor_indices.1 as usize)] == 1 {
                        new_basin.push(neighbor_indices)
                    }
                }
            }
            println!("{}", array_copy);
            basin_counts.push(count);
        }
    }
}
pub fn day9() {
    let real_input = fs::read_to_string("input9.txt").unwrap();
    let parsed_input = split_input(&real_input);
    let bordered = add_border(&parsed_input);
    println!("{}", bordered);
    let minima_array = find_minima(&bordered);
    let result = minima_array.sum();
    println!("{}", minima_array);
    println!("{}", result);
    let mut basin_counts = bfs(&bordered);
    basin_counts.sort();
    println!(
        "{}",
        basin_counts[basin_counts.len() - 1]
            * basin_counts[basin_counts.len() - 2]
            * basin_counts[basin_counts.len() - 3]
    );
}
