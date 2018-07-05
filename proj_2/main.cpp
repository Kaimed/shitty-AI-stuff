#include <fstream>
#include <iostream>
#include <vector>
#include "Student.h"
using namespace std;

int main(){
  fstream fin1;
  fin1.open("input1.txt");
  Student Kevin(fin1);
  cout<<Kevin.get_pref();
}
