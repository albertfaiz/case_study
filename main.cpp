// main.cpp
#include <iostream>
#include <random>
#include <cstdlib>
int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " N\n";
        return 1;
    }
    const int n = std::atoi(argv[1]);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    int hits = 0;
    for (int i = 0; i < n; ++i) {
        double x = dis(gen);
        double y = dis(gen);
        if (x*x + y*y < 1.0)
            hits++;
    }
    double pi = 4.0 * static_cast<double>(hits) / n;
    std::cout << "n=" << n << ", pi=" << pi << std::endl;
    return 0;
}
