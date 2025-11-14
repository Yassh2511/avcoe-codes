// SImplehuffman

import java.util.*;

class HuffmanNode implements Comparable<HuffmanNode> {
    char ch;
    int freq;
    HuffmanNode left, right;

    HuffmanNode(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
    }

    public int compareTo(HuffmanNode other) {
        return this.freq - other.freq;
    }
}

public class SimpleHuffman {

    static void printCodes(HuffmanNode root, String code) {
        if (root == null) return;

        if (root.left == null && root.right == null)
            System.out.println(root.ch + " : " + code);

        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = sc.nextLine();

        Map<Character, Integer> freq = new HashMap<>();
        for (char c : text.toCharArray())
            freq.put(c, freq.getOrDefault(c, 0) + 1);

        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>();
        for (var e : freq.entrySet())
            pq.add(new HuffmanNode(e.getKey(), e.getValue()));

        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();
            HuffmanNode parent = new HuffmanNode('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;
            pq.add(parent);
        }

        System.out.println("\nHuffman Codes:");
        printCodes(pq.peek(), "");

        sc.close();
    }
}
