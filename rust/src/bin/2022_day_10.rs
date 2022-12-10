fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let register_values = simulate(input);

	let mut total = 0;
	for (i, val) in register_values.iter().skip(19).step_by(40).enumerate() {
		let i = i as i32;
		let cycle = 20 + i * 40;
		let signal_strength = cycle * val;
		total += signal_strength;
	}

	Ok(total.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let register_values = simulate(input);

	let mut screen = String::new();
	for (i, val) in register_values.iter().enumerate() {
		let cycle = i as i32;
		if cycle % 40 == 0 {
			screen.push('\n');
		}
		if (val - cycle % 40).abs() <= 1 {
			screen.push('#');
		} else {
			screen.push('.');
		}
	}

	Ok(screen.trim().into())
}

fn simulate(program: String) -> Vec<i32> {
	let mut x = 1;
	let mut register_values = Vec::new();

	for line in program.lines() {
		let instruction = &line[..4];
		match instruction {
			"addx" => {
				let v: i32 = line[5..].parse().unwrap();
				register_values.push(x);
				register_values.push(x);
				x += v;
			}
			"noop" => {
				register_values.push(x);
			}
			_ => unreachable!("bad instruction '{}'", instruction),
		}
	}
	register_values
}
