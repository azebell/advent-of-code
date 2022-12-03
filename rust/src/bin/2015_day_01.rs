fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let up_count = input.matches('(').count();
	let down_count = input.matches(')').count();
	Ok((up_count - down_count).to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut floor = 0;
	let mut position = 1;
	for c in input.chars() {
		floor += match c {
			'(' => 1,
			')' => -1,
			_ => 0,
		};
		if floor < 0 {
			break;
		}
		position += 1;
	}
	Ok(position.to_string())
}
