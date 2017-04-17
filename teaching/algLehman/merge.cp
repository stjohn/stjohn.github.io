#include <iostream.h>
#include <math.h>

void merge_sort( int A[], int first, int last);
void merge( int A[], int p, int q, int r);

void main()
{
	int A[10], i,j;
	
	for ( i=0; i < 10; i++)
	{
		cout << "Enter number " << i+1 << ": ";
		cin >> A[i];
	}
	for ( i=0; i < 10; i++)
	{
		cout << A[i] << "  ";
	}
	
	merge_sort(A,0,9);
	
	cout << "\n\nThe sorted list is: \n";
	for ( i=0; i < 10; i++)
	{
		cout << A[i] << "  ";
	}

}
 
void merge_sort( int A[], int p, int r)
{
	if ( p < r )
	{
		int q = floor( (p+r)/2 );
		
		merge_sort(A, p, q);

		merge_sort(A, q+1, r);
		
		merge(A,p,q,r);
	}
}

void merge( int A[], int p, int q, int r)
{
	int B[10], current = 0, i = p, j = q+1;
	
	while ( current < r-p+1 )
	{
		if ( i > q )
		{
			B[current] = A[j];
			j++;
			current++;
		}
		else if ( j > r )
		{
			B[current] = A[i];
			i++;
			current++;
		}
		else if ( A[i] < A[j] )
		{
			B[current] = A[i];
			i++;
			current++;
		}
		else
		{
			B[current] = A[j];
			j++;
			current++;
		}
	}
	
	for ( i = p, j = 0; i <= r ; i++, j++)
		A[i] = B[j];
}