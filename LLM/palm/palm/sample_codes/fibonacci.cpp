#include <iostream>

int fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2);
    }
}

int main() {
    std::cout << fibonacci_recursive(10) << std::endl;  // 10番目のフィボナッチ数を表示します
    return 0;
}
