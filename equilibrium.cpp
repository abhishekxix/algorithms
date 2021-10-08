#include <bits/stdc++.h>

using namespace std;

vector<int> eq(vector<int>& nums) {
  vector<int> result(0);
  int left_sum = 0;
  int total = 0;

  for (int num : nums) {
    total += num;
  }

  for (int i = 0; i < nums.size(); i++) {
    total -= nums[i];
    if (left_sum == total) {
      result.push_back(i);
    }
    left_sum += nums[i];
  }

  if (result.size() == 0) return vector<int>{-1};
  return result;
}

int main() {
  cout << "Enter the size of array: ";
  int size = 0;
  cin >> size;
  vector<int> nums(0);
  int temp;

  cout << "Enter the elements of the array: ";
  for (int i = 0; i < size; i++) {
    cin >> temp;
    nums.push_back(temp);
  }

  vector<int> result = eq(nums);
  for (int r : result) {
    cout << r << " ";
  }
  cout << endl;

  return 0;
}
