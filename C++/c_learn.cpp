// C++学习
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

// 结构体
struct sd
{
	string name;
};

// 牛逼的初始化方法
// struct initialName
// {
// 	string name;
// } name = {
// 	"sss"
// };




int main(){

	// char dog[8] = {'b', 'e', 'a', 'u', 'x', ' ', 'I', 'I'};
	// char cat[8] = {'f', 'a', 't', 'e', 's', 's', 'a', '\0'};
	// cout<<cat<<endl;
	// return 0;

	// const int SIZE = 15;
	// char name1[SIZE];
	// char name2[SIZE] = "C++Boy";

	// cout<<"hello, i am"<<name2<<endl;
	// cout<<"what's your name?"<<endl;
	// cin>>name1;
	// cout<<"well,"<<name1<<"your name has "<<strlen(name1)<<"chars";

	// // getline() 接受一行的输入
	// const int SIZE = 20;
	// char names[SIZE];
	// char dessert[SIZE];

	// cout<<"输入你的名称"<<endl;
	// cin.getline(names, SIZE);
	// cout<<"输入你喜欢的食物"<<endl;
	// cin.getline(dessert, SIZE);
	// cout<<"你好,"<<names<<",你喜欢的食物是"<<dessert<<endl;

	// string str = "sss";

	// cout<<str[0];

	// 指针 地址
	int update = 6;
	// int 表示该指针指向吃一个int类型的变量地址
	int* p;
	p = &update;

	cout<<p<<endl;

	cout<<*p<<endl;

}