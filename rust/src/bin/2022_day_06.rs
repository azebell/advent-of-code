use std::collections::HashSet;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	for (i, window) in input.as_bytes().windows(4).enumerate() {
		let mut char_set = HashSet::new();
		if window.iter().all(|c| char_set.insert(c)) {
			return Ok((i + 4).to_string());
		}
	}
	Err("No marker found".to_string())
}

fn part2(input: String) -> Result<String, String> {
	for (i, window) in input.as_bytes().windows(14).enumerate() {
		let mut char_set = HashSet::new();
		if window.iter().all(|c| char_set.insert(c)) {
			return Ok((i + 14).to_string());
		}
	}
	Err("No marker found".to_string())
}
