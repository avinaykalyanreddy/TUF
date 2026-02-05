/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


int *sort(int *nums,int numsSize){

    int mid = numsSize/2;

    if (numsSize <= 1){

        return nums;
    }
    int *left_arr = (int*)malloc(sizeof(int)*mid);
    int *right_arr = (int*)malloc(sizeof(int)*(numsSize-mid));

    int i = 0;

    while (i < mid){

        left_arr[i] = nums[i];
        i += 1;
    }

    while (i < numsSize){

        right_arr[i-mid] = nums[i];
        i += 1;
    }

    int *left = sort(left_arr,mid);
    int *right = sort(right_arr,numsSize-mid);

    int j = 0,k = 0;

    int *res = (int*)malloc(sizeof(int)*numsSize);
    int l = 0;
    while ( j < mid && k < numsSize-mid){

        if (left[j] < right[k]){

            res[l] = left[j];
            j += 1;
            l += 1;
        }
        else{

            res[l] = right[k];
            k += 1;
            l += 1;
        }
    }

    while ( j < mid){

        res[l] = left[j];

        j += 1;
        l += 1;
    }

    while (k < numsSize-mid){

        res[l] = right[k];

        k += 1;
        l += 1;
    }
    free(left);
    free(right);
    return res;



}
int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    return sort(nums,numsSize);
}