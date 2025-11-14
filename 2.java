
//FibonacciIterative

import java.util.Scanner;

class FibonacciIterative {

    static int fibonacciIterative(int n) {
        if (n <= 1)
            return n;

        int prev = 0, curr = 1, next;
        for (int i = 2; i <= n; i++) {
            next = prev + curr;
            prev = curr;
            curr = next;
        }
        return curr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();

        System.out.println("Fibonacci(" + n + ") = " + fibonacciIterative(n));
        sc.close();
    }
}

// Time Complexity: O(n)
// Space Complexity: O(1)
