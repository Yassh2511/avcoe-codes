// FibonacciRecursive

import java.util.Scanner;

public class FibonacciRecursive {

    static int fibonacciRecursive(int n) {
        if (n <= 1)
            return n;
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();

        System.out.println("Fibonacci(" + n + ") = " + fibonacciRecursive(n));
        sc.close();
    }
}

// Time Complexity: O(2^n)
// Space Complexity: O(n)
