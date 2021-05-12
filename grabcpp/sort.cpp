template <class T>
int linear_search(T arr[],T target,int size){
  for(int i = 0;i<size; i++){
    if(arr[i]==target){
      return i;
    }
  }
  return -1;
}

template <class T>
int binary_search(T arr[],T target,int start,int end){
  while(start<=end){
    int mid = (end - start)/2 + start;
    if(arr[mid] == target){
      return mid;
    }else if(arr[mid]<target){
      start = mid+1;
    }else{
      end = mid-1;
    }
  }
  return -1;
}

template <class T>
int greatest_less_than(T arr[],T target,int start,int end){
  int gltbinIndex=-1;
  while(start<=end){
    int mid = (end - start)/2 + start;
    if(arr[mid]>=target){
      end = mid -1;
    }else{
      gltbinIndex = mid;
      start = mid+1;
    }
  }
  return gltbinIndex;
}

template <class T> 
int smallest_greater_than(T arr[],T target,int start,int end){
  int sgtbinIndex = -1;
  while(start<=end){
    int mid = (end - start)/2 + start;
    if(arr[mid]<=target){
      start = mid+1;
    }else{
      sgtbinIndex = mid;
      end = mid -1;
    }
  }
  return sgtbinIndex;
}
