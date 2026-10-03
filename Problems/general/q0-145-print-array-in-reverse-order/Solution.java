/**
 * Problem: Q0.145 - Print Array in Reverse Order
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
        int[] arr = new int[size];
        for(int i=0;i<size;i++){
            arr[i] = sc.nextInt();
        }
        for(int i =size-1;i>=0;i--){
            System.out.print(arr[i]+" ");
        }
    }
}
