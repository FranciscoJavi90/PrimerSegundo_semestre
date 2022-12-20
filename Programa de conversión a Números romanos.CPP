#include<iostream.h>
#include<conio.h>
void main()
{
cout<<"PROGRAMA CONVERSION NUMEROS ENTEROS A ROMANOS \n"<<endl;
	int x;
	cout<<"Ingrese un numero: ";
   cin>>x;
  if ((x>=1)&&(x<=100))
  {
   cout<<"Numero romano convertido: ";
		if(x>=100)	{cout<<"C"	;x=x-100; }
		if(x>=90)	{cout<<"XC"	;x=x-90;  }
		if(x>=50)	{cout<<"L"	;x=x-50;  }
		if(x>=40)	{cout<<"XL"	;x=x-40;  }
		if(x>=30)	{cout<<"X"	;x=x-10;  }
		if(x>=20)	{cout<<"X"	;x=x-10;  }
		if(x>=10)	{cout<<"X"	;x=x-10;  }
		if(x>=9)		{cout<<"IX"	;x=x-9;	 }
		if(x>=5)		{cout<<"V"	;x=x-5;	 }
		if(x>=4)		{cout<<"IV"	;x=x-4;	 }
		if(x>=3)		{cout<<"III";x=x-3;	 }
		if(x>=2)		{cout<<"II"	;x=x-2;	 }
		if(x>=1)		{cout<<"I"	;x=x-1;	 }
 }
  else
     {
      cout<<"Ingrese un numero entre 0-100"<<endl;
     	}
getch();
return;
}
