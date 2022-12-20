#include<iostream.h>
#include<conio.h>
#include<locale.h>

int ano;

void main(){
	cout<<" AÑO BICIESTO";
	cout<<"\n\r -----------";
	cout<<"\n\r Ingrese un año: ";
	cin>>ano;
	if((ano%4==0)&&(ano%100!=0)||(ano%400==0)){
	cout<<"\n\r el ano: "<<ano<<" es biciesto";
	}else{
	cout<<"\n\r el ano: "<<ano<<" no es biciesto";
	}
getch();
}


