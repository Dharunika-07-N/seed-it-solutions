/**
 * Problem: Q0.25 - Basic_level_1_Datatypes_5
 * Category: General
 * Difficulty: Medium
 * Platform: SEED-IT Platform (https://seed-it.com)
 * Date Solved: 2026-09-22
 * Language: c
 * Test Cases: 30 / 30 Passed (100%)
 */

#include <stdio.h>
#include<string.h>
int main() {
    char input[50];
    fgets(input,sizeof(input),stdin);
    printf("%s %zu",input , strlen(input));
    return 0;
}
