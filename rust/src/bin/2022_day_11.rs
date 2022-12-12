use std::str::FromStr;

fn main() {
	match aoc::run_solver::<fn(_) -> _>(part1, part2) {
		Ok(result) => println!("{}", result),
		Err(e) => println!("{}", e),
	}
}

fn part1(input: String) -> Result<String, String> {
	let mut monkeys: Vec<Monkey> = input
		.split("\n\n")
		.map(|chunk| chunk.parse().unwrap())
		.collect();

	let mut ranks = vec![0; monkeys.len()];

	for _ in 0..20 {
		for m in 0..monkeys.len() {
			let Monkey { test, yes, no, .. } = monkeys[m];
			for i in 0..monkeys[m].items.len() {
				ranks[m] += 1;
				let mut item = monkeys[m].items[i];
				item = update(item, &monkeys[m].operation);
				item /= 3;
				if item % test == 0 {
					monkeys[yes].items.push(item);
				} else {
					monkeys[no].items.push(item);
				}
			}
			monkeys[m].items.clear();
		}
	}

	ranks.sort();
	let answer = ranks.pop().unwrap() * ranks.pop().unwrap();

	Ok(answer.to_string())
}

fn update(item: u64, operation: &Operation) -> u64 {
	match operation {
		Operation::Add(c) => item + c,
		Operation::Multiply(c) => item * c,
		Operation::Double => item * 2,
		Operation::Square => item * item,
	}
}

fn part2(input: String) -> Result<String, String> {
	let mut monkeys: Vec<Monkey> = input
		.split("\n\n")
		.map(|chunk| chunk.parse().unwrap())
		.collect();

	let mut ranks = vec![0; monkeys.len()];

	let mod_prod = monkeys.iter().fold(1, |acc, monkey| acc * monkey.test);

	for _ in 0..10000 {
		for m in 0..monkeys.len() {
			let Monkey { test, yes, no, .. } = monkeys[m];
			for i in 0..monkeys[m].items.len() {
				ranks[m] += 1;
				let mut item = monkeys[m].items[i];
				item = update(item, &monkeys[m].operation);
				item %= mod_prod;
				if item % test == 0 {
					monkeys[yes].items.push(item);
				} else {
					monkeys[no].items.push(item);
				}
			}
			monkeys[m].items.clear();
		}
	}

	ranks.sort();
	let a = ranks.pop().unwrap() as u128;
	let b = ranks.pop().unwrap() as u128;
	let answer = a * b;

	Ok(answer.to_string())
}

struct Monkey {
	items: Vec<u64>,
	operation: Operation,
	test: u64,
	yes: usize,
	no: usize,
}

impl FromStr for Monkey {
	type Err = String;

	fn from_str(s: &str) -> Result<Self, Self::Err> {
		let lines: Vec<_> = s.lines().collect();

		let items: Vec<_> = lines[1].split_once(": ").unwrap().1.split(", ").collect();
		let items = items.iter().map(|item| item.parse().unwrap()).collect();

		let operation = lines[2].split_once("= ").unwrap().1.parse().unwrap();

		let test = lines[3].split_whitespace().last().unwrap().parse().unwrap();
		let yes = lines[4].split_whitespace().last().unwrap().parse().unwrap();
		let no = lines[5].split_whitespace().last().unwrap().parse().unwrap();

		Ok(Monkey {
			items,
			operation,
			test,
			yes,
			no,
		})
	}
}

enum Operation {
	Add(u64),
	Multiply(u64),
	Double,
	Square,
}

impl FromStr for Operation {
	type Err = String;

	fn from_str(s: &str) -> Result<Self, Self::Err> {
		let mut tokens = s.split_whitespace();
		tokens.next();
		match tokens.next().unwrap() {
			"+" => match tokens.next().unwrap() {
				"old" => Ok(Operation::Double),
				x => Ok(Operation::Add(x.parse().unwrap())),
			},
			"*" => match tokens.next().unwrap() {
				"old" => Ok(Operation::Square),
				x => Ok(Operation::Multiply(x.parse().unwrap())),
			},
			_ => Err("Invalid operator".to_string()),
		}
	}
}
