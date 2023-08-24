/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<iostream>
using namespace std;
void bubbleSort(int arr[],int n)
{
    int i,j;
    for(i=1;i<n;i++){
        for(j=0;j<n-i;j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            
        }
        
    }
    for(i=0;i<5;i++)
    cout<<"\t"<<arr[i];
    
    
}
int main()
{
   int arr[]={1,2,3,4,5};
   bubbleSort(arr,5);

    return 0;
}
