/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.
******************************************************************************/
#include <iostream>
using namespace std;

int main() {
    int num1, num2,op;
    cout << "Seleccione una operación:" << endl;
    cout << "Sumar(1)" << endl;
    cout << "Restar(2)" << endl;
    cout << "Multiplicar(3)" << endl;
    cout << "Dividir(4)" << endl;
    cin >> op;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    switch(op){
        case 1:
            cout << "La suma es: " << num1 + num2 << endl;
            break;
        case 2:
            cout << "La resta es: " << num1 - num2 << endl;
            break;
        case 3:
            cout << "La multiplicación es: " << num1 * num2 << endl;
            break;
        case 4:{
            if (num2 != 0) 
                cout << "La división es: " << num1 / num2 << endl;
    }
            break;
    return 0;
}
}




