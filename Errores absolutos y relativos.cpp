#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int opcion;
  double valorReal, valorAproximado, valorMaximo, valorMinimo;

  cout << "Seleccione el caso: " << endl;
  cout << "1) Valor real - Valor aproximado" << endl;
  cout << "2) (Valor maximo - Valor minimo) / 2" << endl;
  cin >> opcion;

  switch (opcion) {
    case 1:
      cout << "Ingrese el valor real: ";
      cin >> valorReal;
      cout << "Ingrese el valor aproximado: ";
      cin >> valorAproximado;
      break;
    case 2:
      cout << "Ingrese el valor maximo: ";
      cin >> valorMaximo;
      cout << "Ingrese el valor minimo: ";
      cin >> valorMinimo;
      break;
    default:
      cout << "Opción no valida." << endl;
      return 1;
  }

  double errorAbsoluto;
  switch (opcion) {
    case 1:
      errorAbsoluto = abs(valorReal - valorAproximado);
      break;
    case 2:
      errorAbsoluto = (valorMaximo - valorMinimo) / 2;
      break;
  }

  double errorRelativo;
  switch (opcion) {
    case 1:
      errorRelativo = (errorAbsoluto / valorReal) * 100;
      break;
    case 2:
      errorRelativo = (errorAbsoluto / valorMaximo) * 100;
      break;
  }

  cout << "Error absoluto: " << errorAbsoluto << endl;
  cout << "Error relativo: " << errorRelativo << " %" << endl;

  return 0;
}
