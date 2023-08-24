#include <stdio.h>
#include<iostream>
using namespace std;
void insertionSort(int arr[],int n)
{
    int i,j;
    for(i=1;i<n;i++){
        j=i-1;
        while(j>=0)
        {
            if(arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            j--;
        }
        
    }
    for(i=0;i<5;i++)
    cout<<"\t"<<arr[i];
    
    
}
int main()
{
   int arr[]={5,4,3,2,1};
   insertionSort(arr,5);

    return 0;
}
