#include <iostream>
#include <string>
using namespace std;

int main(){
    int starter = 5; //Overall length of string
    char startChar = 65; //Starting character value ("A")
    string output = "";

    for(int i = 0; i < starter; i++){
        output = startChar;
        cout << output;
        startChar++;
    }
    return 0;
}
