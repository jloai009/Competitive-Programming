//  SPOJ - NHAY - A Needle in the Haystack
//  https://www.spoj.com/problems/NHAY/

#include <bits/stdc++.h>
using namespace std;

vector<int> findOcurrences(int len_needle, string &haystack, string &needle) {
    string KMPString = needle + '\x00' + haystack;

    int k = 0, N = KMPString.size();

    vector<int> LPS(N), ocurrences;

    for(int i = 1; i < N; ++i) {
        while (k > 0 and KMPString[i] != KMPString[k]) {
            k = LPS[k -1];
        }

        k += KMPString[i] == KMPString[k];
        
        LPS[i] = k;

        if (LPS[i] == len_needle) {
            ocurrences.push_back(i - len_needle*2);
        }
    }

    return ocurrences;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int len_needle;
    string haystack, needle;

    while (cin >> len_needle) {
        cin >> needle;
        cin >> haystack;

        vector<int> ocurrences = findOcurrences(len_needle, haystack, needle);

        for (int i : ocurrences) {
            cout << i << "\n";
        }

        cout << "\n";
    }
}