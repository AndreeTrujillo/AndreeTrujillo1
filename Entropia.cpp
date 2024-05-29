#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

double calcularEntropia(const int* arr, int size) {
    unordered_map<int, int> mapaFrecuencia;
    for (int i = 0; i < size; ++i) {
        mapaFrecuencia[arr[i]]++;
    }

    double entropia = 0.0;
    for (const auto& par : mapaFrecuencia) {
        double probabilidad = static_cast<double>(par.second) / size;
        entropia -= probabilidad * log2(probabilidad);
    }

    return entropia;
}

int main() {
    int arr[] = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6}; // Array con más valores
    int size = sizeof(arr) / sizeof(arr[0]);

    double entropia = calcularEntropia(arr, size);
    cout << "Entropia del array: " << entropia << endl;

    return 0;
}
