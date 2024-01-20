fn main() {
    let input = std::fs::read_to_string("../input.txt").unwrap();
    // let number_regex = regex::Regex::new(r"(\d+)").unwrap();
    let number_regex = regex::Regex::new(r"(-?\d+)").unwrap();
    let total_sum = number_regex
        .find_iter(input.as_str())
        .fold(0, |acc, number| {
            return acc + number.as_str().parse::<i32>().unwrap();
        });
    println!("[Part 1] Total sum: {}", total_sum);
    // They had us on the second part, not gonna lie
    // Won't do this now.
}
