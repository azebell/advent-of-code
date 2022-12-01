pub fn run_solver<F>(solver1: F, solver2: F) -> Result<String, String>
where
	F: Fn(String) -> Result<String, String>,
{
	let config = read_config(std::env::args().skip(1))?;
	match config.part {
		1 => solver1(config.input),
		2 => solver2(config.input),
		_ => Err(format!("Invalid challenge part '{}'", config.part)),
	}
}

struct Config {
	part: usize,
	input: String,
}

fn read_config(mut args: impl Iterator<Item = String>) -> Result<Config, String> {
	let part: usize = args
		.next()
		.ok_or("Challenge part not specified")?
		.parse()
		.or(Err("Unable to determine challenge part"))?;

	let input = match args.next() {
		Some(filepath) => read_file(filepath)?,
		None => read_stdin()?,
	};

	Ok(Config { part, input })
}

fn read_stdin() -> Result<String, String> {
	let mut buffer = String::new();
	for line in std::io::stdin().lines() {
		buffer.push_str(&line.map_err(|e| e.to_string())?);
		buffer.push('\n');
	}
	Ok(buffer)
}

fn read_file(filepath: String) -> Result<String, String> {
	std::fs::read_to_string(filepath).map_err(|e| e.to_string())
}
