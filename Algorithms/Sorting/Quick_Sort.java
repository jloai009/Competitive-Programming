import java.util.*;

class Quick_Sort {

  private static int partition(int[] array, int left, int right){
    int pivot = array[right];
    int ptr = left;
    for(int i = left; i < right; i++){
      if(array[i] < pivot){
        int temp = array[i];
        array[i] = array[ptr];
        array[ptr] = temp;
        ptr++;
      }
    }
    int temp = array[right];
    array[right] = array[ptr];
    array[ptr] = temp;
    return ptr;
  }
  
  private static void qs(int[] array, int left, int right){
    if(right-left > 0){
      int pivotIndex = partition(array, left, right);
      qs(array, left, pivotIndex-1);
      qs(array, pivotIndex+1, right);
    }
  }
  
  public static int[] quickSort(int[] array) {
    // Write your code here.
    qs(array, 0, array.length - 1);
    return array;
  }
}
