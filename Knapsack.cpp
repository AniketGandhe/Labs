#include <iostream>

using namespace std;

int knapsack(int W, int weights[], int values[], int totalItems) {
    int dp[totalItems + 1][W + 1];

    for (int i = 0; i <= totalItems; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (weights[i - 1] <= w) {
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[totalItems][W];
}

int main() {
    int W, totalItems;
    cout << "Enter the maximum weight capacity of the knapsack: ";
    cin >> W;
    cout << "Enter the total number of items: ";
    cin >> totalItems;

    int weights[totalItems];
    int values[totalItems];

    for (int i = 0; i < totalItems; i++) {
        cout << "Enter the weight of item " << i + 1 << ": ";
        cin >> weights[i];
        cout << "Enter the value of item " << i + 1 << ": ";
        cin >> values[i];
    }

    int max_value = knapsack(W, weights, values, totalItems);

    cout << "Maximum value that can be obtained: " << max_value << endl;

    return 0;
}

