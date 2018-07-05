#include <vector>
#include <fstream>
using namespace std;

class Student{
protected:
  vector<int> preferences;

public:
  Student(fstream f){
    for(int i = 0;i<5;i++){
      int hold;
      f>>hold;
      preferences.push_back(hold);
    }
  }

    int get_pref(){
      return preferences[1];
    };
};
