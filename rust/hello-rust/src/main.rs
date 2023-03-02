use ferris_says::say;
use std::io::{stdout, BufWriter};

fn main() {
    //println!("");
    // Defines stdout to be stdout function?
    let stdout = stdout();
    let message = String::from("happy pride!");
    let width = message.chars().count();

    let mut writer = BufWriter::new(stdout.lock());
    say(message.as_bytes(), width, &mut writer).unwrap();
    
}
