static int linear_search(int* arr,int size,int target){
  for(int i=0;i<size;i++){
    if(arr[i] == target){
      return i;
    }
  }
  return -1;
}

static int binarysearch(int* sortedarr,int target,int start,int end){
  while(start<=end){
    int mid = (end - start)/2 + start;
    if(sortedarr[mid] == target){return mid;}
    else if(sortedarr[mid]<target){start = mid + 1;}
    else{end = mid -1;}
  }
  return -1;
}
