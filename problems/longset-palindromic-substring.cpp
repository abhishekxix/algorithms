#include <bits/stdc++.h>

using namespace std;


class Solution {
  private:
    vector<vector<int>> dp;

    bool isPalindrome(string& s, int l, int h) {
      int mid = l + (h-l)/2;

      for(int i = l; i <= mid; i++) {
        if(s[i]  != s[h - (i - l)]) return false;
      }

      return true;
    }

  public:
    string longestPalindrome(string s) {
      int l = s.length() + 1;
      dp = vector<vector<int>> (l, (vector<int> (l)));
      int ll = 0;
      int lh = 0;

      for(int i = 1; i < l; i++) {
        int length_this_time = 1;

        for(int j = i; j < l; j++) {
          int longest_so_far = max({dp[i-1][j], dp[i][j-1], dp[i-1][dp.size()-1]});

          int tmp = j - i +1;

          if(
            tmp > longest_so_far and
            s[i-1] == s[j-1] and
            isPalindrome(s, i - 1, j -1)
          )
            length_this_time = j - i + 1;

          int cmp = dp[i-1][j];
          if(length_this_time > cmp) {
            dp[i][j] = length_this_time;

            if(length_this_time > dp[i][j - 1] and length_this_time > dp[i-1][dp.size()-1]){
              ll = i - 1;
              lh = j - 1;
            }
          } else{
            dp[i][j] = dp[i-1][j];
          }

        }

      }
      return s.substr(ll, lh - ll + 1);
    }
};


int main(){
  Solution sol = Solution();
  sol.longestPalindrome("aaaa");
  return 0;
}
