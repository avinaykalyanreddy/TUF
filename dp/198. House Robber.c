/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


*/

int robber(int idx,int seen[],int numsSize, int *arr){

    if (idx >= numsSize){
        return 0;
    }

    if (seen[idx] == -1){

        int left = robber(idx+2,seen,numsSize,arr);
        int right = robber(idx+1,seen,numsSize,arr);

        if (arr[idx] + left > right){

            seen[idx] = arr[idx] + left;
        }
        else{

            seen[idx] = right;
        }
    }

    return seen[idx];
}
int rob(int* nums, int numsSize) {

       int seen[numsSize];

    for (int i = 0; i < numsSize; i++) {
        seen[i] = -1;
    }


        return robber(0,seen,numsSize,nums);
}