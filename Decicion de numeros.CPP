#include <iostream>
#include <conio.h>

int n;
int main()
{
    cout<<"Ingresa un numero: "<<endl;
    cin>>n;
    if(n==0){
    cout<<"El numero "<<n<<" es nulo.";
    } else{
    if(n>0){
    cout<<"El numero "<<n<<" es positivo.";
    }else{
    cout<<"El numero "<<n<<" es negativo.";
    }
      }
getch () ;
return 0;
}