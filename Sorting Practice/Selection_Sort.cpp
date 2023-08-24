#include <stdio.h>
#include<iostream>
using namespace std;
void selSort(int arr[],int n)
{
    int min_index,i,j;
    for(i=0;i<n;i++){
        min_index=i;
        for(j=i+1;j<n;j++)
        {
            if(arr[j]<arr[min_index])
            min_index=j;
        }
        int temp=arr[min_index];
        arr[min_index]=arr[i];
        arr[i]=temp;
    }
    for(i=0;i<5;i++)
    cout<<"\t"<<arr[i];
    
    
}
int main()
{
   int arr[]={1,2,3,4,5};
   selSort(arr,5);

    return 0;
}
