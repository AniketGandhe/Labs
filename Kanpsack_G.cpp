//Fractional Knapsack using Greedy Algorithm
#include <iostream>
using namespace std;

struct object
{
	float value;
	float weight;
	float ratio;
	void rt()
	{
		ratio = value/weight;
	}
};
void sortByRatio(object s[],int n)
{
	for(int i=1;i<n;i++)
	{
		for(int j=0;j<n-1;j++)
		{
			if(s[j].ratio > s[j+1].ratio)
			{
				object temp = s[j];
				s[j] = s[j+1];
				s[j+1] = temp;
			}
		}
	}
}
float profit(object s[],int n,float total)
{
	float temp =total;
	float profit =0;
	for(int i=n-1;i >=0 && temp >0;i--)
	{
		if(temp >=s[i].weight)
		{
			temp = temp - s[i].weight;
			profit = profit + s[i].value;
		}
		else if(temp <s[i].weight)
		{
		     profit = profit + (temp*s[i].ratio);
		     return profit;
		}
	}
	return profit;
}
int main()
{
	int num;
	float total;
	cout<<"Enter the Number of Object \n";
	cin>>num;
	cout<<"Enter the total weight\n";
	cin>>total;
	object obj[20];
	
	for(int i=0;i<num;i++)
	{
		cout<<"Enter value of the object:";
		cin>>obj[i].value;
		cout<<"Enter the weight of the object:";
		cin>>obj[i].weight;
		obj[i].rt();
	}
	sortByRatio(obj,num);
	
	for(int i=0;i<num;i++)
	{
		cout<<i<<" "<<obj[i].value<<" "<<obj[i].weight<<" "<<obj[i].ratio<<endl;
	}
		cout<<endl;
		float pr =profit(obj,num,total);
		cout<<"profit is"<<pr<<endl;
                return 0;
}

