/**
 * Problem: Q0.152 - Average of Array Elements
 * Category: General
 * Difficulty: Medium
 * Platform: SEED-IT Platform (https://seed-it.com)
 * Date Solved: 2026-10-08
 * Language: java
 * Test Cases: 30 / 30 Passed (100%)
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int size = sc.nextInt();
        int[] arr = new int[size];
        for(int i = 0;i<size;i++){
            arr[i] = sc.nextInt();
            sum +=arr[i];
        }
        int avg = sum / size;
        System.out.println(avg);

    }
}
