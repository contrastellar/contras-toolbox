#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[]){
    int starter = (signed int) *argv[1]; //Overall length of string
    char startChar = *argv[2]; //Starting character value ("A")
    string output = "";
    string debug = "\nstarting char: " + startChar;
    string debug2 = "\nstarting pos:" + starter;
    cout << debug << debug2 << "\n";

    for(int i = 0; i < starter; i++){
        output = startChar;
        cout << output;
        
    } 
    return 0;
}
