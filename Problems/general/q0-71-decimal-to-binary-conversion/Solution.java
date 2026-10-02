/**
 * Problem: Q0.71 - Decimal to Binary Conversion
 * Category: General
 * Difficulty: Medium
 * Platform: SEED-IT Platform (https://seed-it.com)
 * Date Solved: 2026-10-02
 * Language: java
 * Test Cases: 30 / 30 Passed (100%)
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String binary="";
        while(num>0){
            int rem = num%2;
            binary = rem+binary;
            num = num/2;
        }
        System.out.println(binary);
    
    }
}
