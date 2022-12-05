use std::collections::HashSet;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut total = 0;
	for sack in input.lines() {
		let (left, right) = sack.split_at(sack.len() / 2);
		let left_char_set: HashSet<char> = left.chars().collect();
		let right_char_set: HashSet<char> = right.chars().collect();
		let common_char_set: HashSet<_> = left_char_set.intersection(&right_char_set).collect();
		if let Some(&&c) = common_char_set.iter().next() {
			total += match c.is_lowercase() {
				true => c as u8 - b'a' + 1,
				false => c as u8 - b'A' + 27,
			};
		}
	}
	Ok(total.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut total = 0;
	let mut lines = input.lines();
	while let (Some(a), Some(b), Some(c)) = (lines.next(), lines.next(), lines.next()) {
		let x = a
			.chars()
			.find(|&letter| b.contains(c) && c.contains(letter))
			.unwrap();
		total += match x.is_lowercase() {
			true => x as u8 - b'a' + 1,
			false => x as u8 - b'A' + 27,
		};
	}
	Ok(total.to_string())
}
