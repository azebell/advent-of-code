use std::collections::HashSet;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut head = (0, 0);
	let mut tail = (0, 0);
	let mut visited = HashSet::from([tail]);

	for line in input.lines() {
		let (direction, steps) = line.split_once(' ').unwrap();
		let (dx, dy) = movement(direction).unwrap();
		let steps: isize = steps.parse().unwrap();
		for _ in 0..steps {
			head = (head.0 + dx, head.1 + dy);
			tail = shift_tail(&head, &tail);
			visited.insert(tail);
		}
	}
	Ok(visited.len().to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut head = (0, 0);
	let mut knots = [(0, 0); 9];
	let mut visited = HashSet::from([(0, 0)]);

	for line in input.lines() {
		let (direction, steps) = line.split_once(' ').unwrap();
		let (dx, dy) = movement(direction).unwrap();
		let steps: isize = steps.parse().unwrap();
		for _ in 0..steps {
			head = (head.0 + dx, head.1 + dy);
			let mut curr = head;
			for i in 0..knots.len() {
				knots[i] = shift_tail(&curr, &knots[i]);
				curr = knots[i];
			}
			visited.insert(*knots.last().unwrap());
		}
	}
	Ok(visited.len().to_string())
}

fn movement(direction: &str) -> Result<(isize, isize), String> {
	match direction {
		"U" => Ok((0, 1)),
		"D" => Ok((0, -1)),
		"L" => Ok((-1, 0)),
		"R" => Ok((1, 0)),
		_ => Err("Invalid direction provided".into()),
	}
}

fn shift_tail(head: &(isize, isize), tail: &(isize, isize)) -> (isize, isize) {
	let (dx, dy) = match (head.0 - tail.0, head.1 - tail.1) {
		(-1..=1, -1..=1) => (0, 0),
		(x, y) => (unit(x), unit(y)),
	};
	(tail.0 + dx, tail.1 + dy)
}

fn unit(a: isize) -> isize {
	if a > 0 {
		1
	} else if a < 0 {
		-1
	} else {
		0
	}
}
