use lib::{get_mean}; 
use std::time::Instant;

fn main() {
    let mut data: Vec<f64> = (1..1_000_000).map(|i| i as f64).collect();

    // Measure the time for get_mean
    let start = Instant::now();
    match get_mean(&data) {
        Ok(mean) => println!("Mean: {}", mean),
        Err(e) => println!("Error calculating mean: {}", e),
    }
    let duration = start.elapsed();
    println!("Time taken by get_mean: {} microseconds", duration.as_micros());
}