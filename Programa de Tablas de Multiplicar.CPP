#include<iostream.h>
#include<conio.h>

int num,cont=1,mul;

void main()
{
  	cout<<" INTRODUCE UNA TABLA DE MULTIPLICAR DE 1 a 10.""\n";
	cin>>num;
if (num<=10)
{
cout<<"Si es un intervalo correcto.";
}
else
{
cout<<"No es un intervalo correcto.";
}
while(cont<11)
{
  mul=cont*num;
  cout<<"\n";
  cout<<num;
  cout<<"x";
  cout<<cont;
  cout<<"=";
  cout<<mul;
  cont=cont+1;
}
getch();
return;
}
