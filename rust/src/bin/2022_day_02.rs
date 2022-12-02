fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let shape_points = [1, 2, 3];

	let mut points = 0;

	for line in input.lines() {
		let mut characters = line.chars();
		let p = characters.next().unwrap() as isize - 'A' as isize;
		let q = characters.skip(1).next().unwrap() as isize - 'X' as isize;

		points += shape_points[q as usize];
		points += match q - p {
			1 | -2 => 6, // win
			0 => 3,      // draw
			_ => 0,      // loss
		};
	}
	Ok(points.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let shape_points = [1, 2, 3];

	let mut points = 0;

	for line in input.lines() {
		let mut characters = line.chars();
		let p = characters.next().unwrap() as isize - 'A' as isize;
		let q = characters.skip(1).next().unwrap() as isize - 'X' as isize;

		points += q * 3;
		let offset = match q {
			0 => -1, // should lose
			1 => 0,  // should draw
			_ => 1,  // should win
		};
		let shape = modulo(p + offset, 3);
		points += shape_points[shape as usize];
	}
	Ok(points.to_string())
}

fn modulo(a: isize, b: isize) -> isize {
	((a % b) + b) % b
}
