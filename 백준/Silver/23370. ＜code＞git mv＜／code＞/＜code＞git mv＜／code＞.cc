#include <iostream>
#include <vector>
#include <string>




using namespace std;



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string a;
    string b;


    cin >> a;
    cin >> b;

    int a_st = 0;
    int b_st = 0;


    vector<string> words_a;
    vector<string> words_b;





    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '/') {
            words_a.push_back(a.substr(a_st, i - a_st));
            a_st = i + 1;
        }
    }
    words_a.push_back(a.substr(a_st)); 


    
    for (int i = 0; i < b.length(); i++) {
        if (b[i] == '/') {
            words_b.push_back(b.substr(b_st, i - b_st));
            b_st = i + 1;
        }
    }
    words_b.push_back(b.substr(b_st));




    int i = 0;
    while (i < words_a.size() && i < words_b.size() && words_a[i] == words_b[i]) {
        i++;
    }


    int j = 0;
    while (j < (words_a.size() - i) && j < (words_b.size() - i) && words_a[words_a.size() - 1 - j] == words_b[words_b.size() - 1 - j]) {
        j++;
    }




    string A = "";
    for (int p = 0; p < i; p++) {
        if (p > 0) A += "/";
        A += words_a[p];
    }

    


    string D = "";
    for (int p = 0; p < j; p++) {
        if (p > 0) D = "/" + D;
        D = words_a[words_a.size() - 1 - p] + D;
    }

    


    string B, C;
    for (int k = i; k < words_a.size() - j; k++) {
        if (!B.empty()) {
            B += "/";
        }
        B += words_a[k];
    }
    
    for (int k = i; k < words_b.size() - j; k++) {
        if (!C.empty()) {
            C += "/";
        }
        C += words_b[k];
    }



    if (!A.empty()) {
        A += "/";
    }
    if (!D.empty()) {
        D = "/" + D; 
    }



    cout << A << "{" << B << " => " << C << "}" << D;

}
