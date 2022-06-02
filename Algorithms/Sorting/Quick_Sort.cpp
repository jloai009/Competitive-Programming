#include <vector>
using namespace std;

int partition(vector<int>& array, int left, int right){
  int pivot = array[right];
  int ptr = left;
  for(int i = left; i < right; i++){
    if(array[i] < pivot){
      swap(array[i], array[ptr]);
        ptr++;
    }
  }

  swap(array[ptr], array[right]);
  return ptr;
}

void qs(vector<int>& array, int left, int right){
  if(right-left > 0){
    int pivot_index = partition(array, left, right);
    qs(array, left, pivot_index-1);
    qs(array, pivot_index+1, right);
  }
}

vector<int> quickSort(vector<int> array){
  qs(array, 0, array.size()-1);
  return array;
}