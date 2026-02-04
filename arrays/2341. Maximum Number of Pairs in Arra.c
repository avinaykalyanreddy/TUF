int* numberOfPairs(int* nums, int numsSize, int* returnSize) {



    int arr[101] = {0};

    for(int i = 0; i < numsSize ; i++){

        arr[nums[i]] += 1;
    }

    int single = 0;
    int pairs = 0;

    for(int i = 0; i < 101; i++){

        single += arr[i]%2;
        pairs += arr[i]/2;
    }

    int* result = (int*)malloc(2 * sizeof(int));

    result[0] = pairs;
    result[1] = single;
    *returnSize = 2;

    return result;
}