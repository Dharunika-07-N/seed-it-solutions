/**
 * Problem: Q0.149 - Subtracting Triangular Numbers from Total
 * Category: General
 * Difficulty: Medium
 * Platform: SEED-IT Platform (https://seed-it.com)
 * Date Solved: 2026-10-03
 * Language: java
 * Test Cases: 30 / 30 Passed (100%)
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int sum = 0;
        int[] arr = new int[size];
        for(int i =0 ; i<size;i++){
            arr[i] = sc.nextInt();
            sum += arr[i];
        }
        for(int i =0 ;i<size;i++){
            int ans = sum - arr[i];
            System.out.print(ans+" ");
            sum = sum - arr[i];

        }

    }
}
