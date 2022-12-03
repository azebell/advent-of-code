use std::collections::HashMap;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut atlas = HashMap::new();
	let mut position = (0, 0);
	atlas.insert(position, 1);

	for c in input.chars() {
		let movement = match c {
			'<' => (-1, 0),
			'>' => (1, 0),
			'^' => (0, 1),
			'v' => (0, -1),
			_ => panic!("Invalid move '{}'", c),
		};
		position.0 += movement.0;
		position.1 += movement.1;
		*atlas.entry(position).or_insert(1) += 1;
	}

	Ok(atlas.keys().count().to_string())
}

fn part2(input: String) -> Result<String, String> {
	type Atlas = HashMap<(i32, i32), i32>;
	let mut atlas = HashMap::new();
	atlas.insert((0, 0), 2);

	fn deliver(mut atlas: Atlas, directions: impl Iterator<Item = char>) -> Atlas {
		let mut position = (0, 0);
		for c in directions {
			let movement = match c {
				'<' => (-1, 0),
				'>' => (1, 0),
				'^' => (0, 1),
				'v' => (0, -1),
				_ => panic!("Invalid move '{}'", c),
			};
			position.0 += movement.0;
			position.1 += movement.1;
			*atlas.entry(position).or_insert(1) += 1;
		}
		atlas
	}

	atlas = deliver(atlas, input.chars().step_by(2));
	atlas = deliver(atlas, input.chars().skip(1).step_by(2));

	Ok(atlas.keys().count().to_string())
}
