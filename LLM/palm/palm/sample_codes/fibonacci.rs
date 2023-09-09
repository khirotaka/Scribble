fn fibonacci_recursive(n: u32) -> u32 {
    if n <= 1 {
        n
    } else {
        fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    }
}

fn main() {
    println!("{}", fibonacci_recursive(10));  // 10番目のフィボナッチ数を表示します
}
