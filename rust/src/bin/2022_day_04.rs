fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut contained = 0;
	for pair in input.lines() {
		let mut pair = pair.split(',');
		let left = pair.next().unwrap();
		let left: Vec<usize> = left.split('-').map(|x| x.parse().unwrap()).collect();
		let right = pair.next().unwrap();
		let right: Vec<usize> = right.split('-').map(|x| x.parse().unwrap()).collect();

		if (left[0] >= right[0] && left[1] <= right[1])
			|| (right[0] >= left[0] && right[1] <= left[1])
		{
			contained += 1
		}
	}
	Ok(contained.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut overlap = 0;
	for pair in input.lines() {
		let mut pair = pair.split(',');
		let left = pair.next().unwrap();
		let left: Vec<usize> = left.split('-').map(|x| x.parse().unwrap()).collect();
		let right = pair.next().unwrap();
		let right: Vec<usize> = right.split('-').map(|x| x.parse().unwrap()).collect();

		if left[0] <= right[1] && left[1] >= right[0] {
			overlap += 1
		}
	}
	Ok(overlap.to_string())
}
