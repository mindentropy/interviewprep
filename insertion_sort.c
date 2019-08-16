#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void ins_sort(int a[], int size)
{

	int i = 0, j = 1, key = 0;

	for(j = 1; j<size; j++) {
		key = a[j];
	
		i = j -1;
		while(i >= 0 && a[i] > key) {
			a[i+1] = a[i];
			i--;
		}
		a[i+1] = key;
	}
}

void dump(int a[], int size)
{
	int i = 0;
	for(i = 0; i<size; i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n");
}

int main(int argc, char **argv)
{
	int a[] = {5, 4, 3, 2, 1};
	int size = sizeof(a)/sizeof(int);
	
	dump(a,size);
	ins_sort(a,size);
	dump(a,size);

	return 0;
}
