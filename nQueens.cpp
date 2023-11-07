#include<iostream>
using namespace std;

int ld[30]={0};
int rd[30]={0};
int cl[30]={0};

bool nqueen(int** arr,int x,int n)
{
	if(x>=n)
	{
		return true;
	}
	for(int i=0;i<n;i++)
	{
		if(ld[i-x+n-1] != 1 && rd[i+x] != 1 && cl[i] != 1)
		{
			arr[i][x]=1;
			ld[i-x+n-1]=1;
			rd[i+x]=1;
			cl[i]=1;
			
			if(nqueen(arr,x+1,n))
			{
				return true;
			}
			arr[i][x]=0;
			ld[i-x+n-1]=0;
			rd[i+x]=0;
			cl[i]=0;
			
		}
	}
	return false;
}
int main()
{	
	int n;
	cout<<"Enter the n Value :";
	cin>>n;
	
	int** arr =new int*[n];
	
	for(int i=0;i<n;i++)
	{
		arr[i] = new int[n];
		
		for(int j=0;j<n;j++)
		{
			arr[i][j]=0;
		}
	}
	if(nqueen(arr,0,n))
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cout<<arr[i][j]<<" ";
			}
			cout<<"\n";
		}
	}
}
