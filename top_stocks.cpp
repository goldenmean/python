#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Custom struct to store stock information
struct StockInfo {
    string name;
    float maxPrice; // Maximum price observed
};

vector<string> get_top_stocks(vector<string> stocks, vector<vector<float>> prices) {
    vector<StockInfo> stockData; // Store stock information

    // Initialize stockData with stock names
    for (const auto& stock : stocks) {
        stockData.push_back({stock, 0.0f});
    }

    // Analyze stock prices
    for (size_t i = 0; i < prices.size(); ++i) {
        for (size_t j = 0; j < prices[i].size(); ++j) {
            if (prices[i][j] > stockData[j].maxPrice) {
                stockData[j].maxPrice = prices[i][j];
            }
        }
    }

    // Collect the names of top-performing stocks
    vector<string> topStocks;
    for (const auto& stock : stockData) {
        topStocks.push_back(stock.name);
    }

    return topStocks;
}

int main() {
    vector<string> stocks = {"AAPL", "GOOGL", "AMZN", "MSFT"};
    vector<vector<float> > prices = {
        {150.0f, 160.0f, 155.0f, 165.0f},
        {2500.0f, 2550.0f, 2520.0f, 2600.0f},
        {3200.0f, 3180.0f, 3250.0f, 3300.0f},
        {300.0f, 310.0f, 305.0f, 315.0f}
    };

    vector<string> topStocks = get_top_stocks(stocks, prices);

    cout << "Top-performing stocks:\n";
    for (const auto& stock : topStocks) {
        cout << stock << endl;
    }

    return 0;
}