#include <iostream>
#include <set>
using namespace std;

int HuffmanCoding(vector<int> a) {
    int ans = 0;
    priority_queue<int, vector<int>, greater<int> > freqs;

    for (int freq : a) {
        freqs.push(freq);
    }

    while (freqs.size() > 1) {
        int first = freqs.top(); freqs.pop();
        int second = freqs.top(); freqs.pop();
        ans += first + second;
        freqs.push(first + second);
    }

    return ans;
}

int main() {
    string text;
    cin >> text;

    set<char> uniqueElements (text.begin(), text.end());
    string s(uniqueElements.begin(), uniqueElements.end());
    vector<int> count_letters;

    for (char c : s) {
        count_letters.push_back(count(text.begin(), text.end(), c));
    }
    cout << HuffmanCoding(count_letters) << '\n';

    return 0;
}
