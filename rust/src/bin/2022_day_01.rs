fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut elf_calories: Vec<usize> = Vec::new();
	let elves = input.split("\n\n");
	for elf in elves {
		let calories = elf.lines().map(|line| line.parse::<usize>().unwrap()).sum();
		elf_calories.push(calories);
	}

	let biggest = elf_calories.iter().max().unwrap();
	Ok(biggest.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut elf_calories: Vec<usize> = Vec::new();
	let elves = input.split("\n\n");
	for elf in elves {
		let calories = elf.lines().map(|line| line.parse::<usize>().unwrap()).sum();
		elf_calories.push(calories);
	}

	elf_calories.sort();
	elf_calories.reverse();
	let total: usize = elf_calories.iter().take(3).sum();
	Ok(total.to_string())
}
