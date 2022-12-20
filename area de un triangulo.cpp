// obtener el area de un triangulo.

#include<iostream.h>
#include<conio.h>

 float base, altura, area;

void main()
{
gotoxy(20,4);
cout<<"obtener el area de un triangulo \n \n";

cout<<"ingrese la base del trisngulo:"<<endl;
cin>>base;
cout<<"ingrese la altura del triangulo:"<<endl;
cin>>altura;
area= base*altura/2;
cout<<"El area del triangulo es: "<<area;

       getch();
       return;
}

