use ndarray::{array, concatenate, Array, Array1, ArrayView1, Axis};
fn input() -> Array1<i32> {
    array![
        1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 5, 1, 1, 1, 4, 5, 1, 1, 1, 3, 4,
        1, 1, 1, 1, 1, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 3, 1, 3, 1, 1, 1, 5, 1, 1, 1, 1,
        1, 5, 4, 1, 2, 4, 4, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 4, 3, 1, 1, 1, 1, 1, 1, 1, 5, 1,
        3, 1, 4, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 4, 1, 3, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 1, 1, 1,
        1, 2, 1, 1, 1, 1, 4, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 3, 3,
        1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2, 1, 1, 1, 4, 1, 1,
        1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 3, 1, 2, 1, 1, 5, 4, 1, 1, 2, 1, 1, 1, 3,
        1, 4, 1, 1, 1, 1, 3, 1, 2, 5, 1, 1, 1, 5, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 2, 2, 2, 2,
        4, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 4, 2, 1, 4, 1, 1, 1, 1, 1, 5, 1, 1, 4, 2, 1,
        1, 2, 5, 4, 2, 1, 1, 1, 1, 4, 2, 3, 5, 2, 1, 5, 1, 3, 1, 1, 5, 1, 1, 4, 5, 1, 1, 1, 1, 4
    ]
}
fn test_input() -> Array1<i32> {
    array![3, 4, 3, 1, 2]
}
fn iterate(input: &mut Array1<i32>) {
    let count_elements = input.iter().filter(|&&x| x == 0).count();
    let new_elements: Array1<i32> = Array::from_elem(count_elements, 8);
    input.mapv_inplace(|x| match x {
        0 => 7,
        _ => x,
    });
    input.mapv_inplace(|x| x - 1);
    *input = concatenate![Axis(0), input.view(), new_elements.view()];
}
fn iterate_fast(old_count: [i64; 9]) -> [i64; 9] {
    let mut new_count = [0; 9];
    for entry in (1..=8).rev() {
        new_count[(entry - 1)] = old_count[entry];
    }
    new_count[8] = old_count[0];
    new_count[6] += old_count[0];

    new_count
}
fn parse_numbers(inp: Array1<i32>) -> [i64; 9] {
    let mut count = [0; 9];
    for entry in inp.iter() {
        count[*entry as usize] += 1;
    }

    count
}

pub fn day6() {
    let mut input = parse_numbers(input());
    println!("{}", input.len());
    for i in 0..256 {
        println!("{}", ArrayView1::<i64>::from(&input));
        input = iterate_fast(input);
    }
    println!("{}", input.iter().sum::<i64>());
}
