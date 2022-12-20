// saber si un numero es par o impar.

#include<iostream.h>
#include<conio.h>

 int N;

void main()
{

cout<<"ingrese un numero:  ";
cin>>N;

	if(N==0)
{
   cout<<"es un numero igual a 0";
}
else
{

	if(N%2==0)
{
   cout<<"es un numero par";
}
else
{
	cout<<"es un numero impar";
}
}
       getch();
       return;

}