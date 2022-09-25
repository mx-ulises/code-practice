fn greet_world() {
    let english = "Hello, world!";
    let south_german = "Grüß Gott!";
    let japanese = "ハロー・ワールド";
    let languages = [english, south_german, japanese];
    for language in languages.iter() {
        println!("{}", &language);
    }
}

fn main() {
    greet_world();
}
