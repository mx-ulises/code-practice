fn main() {
    let penguin_data = "\
    common name, length (cm)
    Little Penguin,33
    Yellow-eyed Penguin,65
    Fiordland Penguin,60
    Corrupted,data
    ";

    let penguin_data_lines = penguin_data.lines();

    for (i, line) in penguin_data_lines.enumerate() {
        // Skip header and blank lines
        if i == 0 || line.trim().len() == 0 {
            continue;
        }

        // Collect fields from line
        let fields:Vec<_> = line
          .split(',')
          .map(|field| field.trim())
          .collect();

        // Add debug logs
        if cfg!(debug_assertions) {
            eprintln!("debug: {:?} -> {:?}", line, fields);
        }

        // Get name and lengths and print if safe
        let name = fields[0];
        if let Ok(length) = fields[1].parse::<f32>() {
            println!("{}, {}cm", name, length);
        }
    }
}
