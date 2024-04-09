#include <stdio.h>

// Tail Call Optimization
// compilador gcc
// Flag -O2 <-- Otimização nível 2

// contar de 0 a 120000 recursivamente
void contar(unsigned long long n, unsigned long long i){
	if(i > n) return;
	else{
		printf("%lld ", i);
		contar(n, i+1);
	}
}

int main(void){
	
	contar(120000, 0);
	
	printf("\n\nFinalizou corretamente (=\n");
	getc(stdin);
	return 0;
}

// recursao.exe    <-- compilado SEM -O2 (stack overflow)
// recursaoTCO.exe <-- compilado COM -O2 (procedimento ITERATIVO na RECURSÃO)
