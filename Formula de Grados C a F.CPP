#include <iostream.h>
#include <conio.h>

float GradosC, GradosF;
	void main()
{
	cout<<"Ingresar Grados Centigrados para la conversion: ";cin>>GradosC;
	GradosF=GradosC*9/5+32;
	cout<<"Los grados Fahrenheit son: "<<GradosF;
	getch();
return;
}
