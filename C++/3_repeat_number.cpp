// 数组中重复的数字
// 给定一个数组，数组中一些元素是重复的，找出数组中任意一个重复的数字
// 直接判断是否有重复数字
#include <iostream>
#include <cstdio>
using namespace std;

// 使用数组 建立hash表，将原数组中的元素存进hash表中，检查是否有重复的数字
bool repeat_number(int numbers[], int lenght){
	int numbers_hash[50]={0};
	int repeat_number_ = false; 
	// 考虑边界值 当输入为空时，直接返回
	if(lenght <= 0){
		return false;
	}

	// 边界值 数组元素大小应该在 0——n-1范围内
	for (int i = 0; i < lenght; ++i)
	{
		if(numbers[i] < 0 || numbers[i] >= lenght-1){
			return false;
		}
	}

	for (int i = 0; i < lenght; ++i)
	{
		numbers_hash[numbers[i]] += 1;
	}

	for (int i = 0; i < lenght; ++i)
	{
		if(numbers_hash[i]>1){
			repeat_number_ = true;
			break;
		}
	}

	return repeat_number_;
}

// offer 思想
bool duplicate(int numbers[], int length, int* duplication){

	// 边界值 若数组长度小于零 直接返回
	if(numbers == nullptr || length <= 0){
		return false;
	}

	// 边界值 所有数字都应该在 0 - n-1 范围之内
	for (int i = 0; i < length; ++i)
	{
		if(numbers[i] < 0 || numbers[i] > (length-1)){
			return false;
		}
	}

	// 遍历 搜索是否有重复元素
	// 双循环 但是循环时只是交换两次，因此总的时间复杂度为O(n)
	for (int i = 0; i < length; ++i)
	{
		while(numbers[i] != i){
			if(numbers[i] == numbers[numbers[i]]){
				return true;
			}
			int tmp = numbers[i];
			numbers[i] = numbers[tmp];
			numbers[tmp] = tmp;
		}
	}

	return false;


}


int main(){
	int numbers[] = {1, 1, 2, 2};
	int length = 0;
	// bool a = repeat_number(numbers, length);
	// bool a = duplicate
	cout<<a<<endl;
}