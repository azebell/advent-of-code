use std::collections::VecDeque;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut stacks = vec![VecDeque::new(); 9];
	let (config, moves) = input.split_once("\n\n").unwrap();

	for line in config.lines() {
		for (i, c) in line.chars().skip(1).step_by(4).enumerate() {
			if c.is_alphabetic() {
				stacks[i].push_front(c);
			}
		}
	}

	for line in moves.lines() {
		let mut tokens = line.split_whitespace().skip(1).step_by(2);
		let qty: usize = tokens.next().unwrap().parse().unwrap();
		let source: usize = tokens.next().unwrap().parse().unwrap();
		let dest: usize = tokens.next().unwrap().parse().unwrap();

		for _ in 0..qty {
			let tmp = stacks[source - 1].pop_back().expect("stack has crates");
			stacks[dest - 1].push_back(tmp);
		}
	}

	let mut result = String::new();
	for mut stack in stacks {
		result.push(stack.pop_back().expect("stack won't be empty"));
	}
	Ok(result)
}

fn part2(input: String) -> Result<String, String> {
	let mut stacks = vec![VecDeque::new(); 9];
	let (config, moves) = input.split_once("\n\n").unwrap();

	for line in config.lines() {
		for (i, c) in line.chars().skip(1).step_by(4).enumerate() {
			if c.is_alphabetic() {
				stacks[i].push_front(c);
			}
		}
	}

	let mut tmp_stack = VecDeque::new();

	for line in moves.lines() {
		let mut tokens = line.split_whitespace().skip(1).step_by(2);
		let qty: usize = tokens.next().unwrap().parse().unwrap();
		let source: usize = tokens.next().unwrap().parse().unwrap();
		let dest: usize = tokens.next().unwrap().parse().unwrap();

		for _ in 0..qty {
			let tmp = stacks[source - 1].pop_back().expect("stack has crates");
			tmp_stack.push_back(tmp);
		}
		for _ in 0..qty {
			stacks[dest - 1].push_back(tmp_stack.pop_back().unwrap());
		}
	}

	let mut result = String::new();
	for mut stack in stacks {
		result.push(stack.pop_back().expect("stack won't be empty"));
	}
	Ok(result)
}
