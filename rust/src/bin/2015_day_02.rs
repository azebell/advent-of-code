fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut paper = 0;
	fn parse_dim(d: Option<&str>) -> Option<usize> {
		Some(d?.parse().unwrap())
	}
	for line in input.lines() {
		let mut dimensions = line.split("x");
		let l = parse_dim(dimensions.next()).unwrap();
		let w = parse_dim(dimensions.next()).unwrap();
		let h = parse_dim(dimensions.next()).unwrap();

		let surface = 2 * l * w + 2 * w * h + 2 * h * l;
		let slack = std::cmp::min(l * w, std::cmp::min(w * h, h * l));
		paper += surface + slack;
	}
	Ok(paper.to_string())
}

fn part2(input: String) -> Result<String, String> {
	let mut ribbon = 0;
	fn parse_dim(d: Option<&str>) -> Option<usize> {
		Some(d?.parse().unwrap())
	}
	for line in input.lines() {
		let mut dimensions = line.split("x");
		let l = parse_dim(dimensions.next()).unwrap();
		let w = parse_dim(dimensions.next()).unwrap();
		let h = parse_dim(dimensions.next()).unwrap();

		let biggest = std::cmp::max(l, std::cmp::max(w, h));

		let wrap = 2 * (l + w + h - biggest);
		let bow = l * w * h;
		ribbon += wrap + bow;
	}
	Ok(ribbon.to_string())
}
