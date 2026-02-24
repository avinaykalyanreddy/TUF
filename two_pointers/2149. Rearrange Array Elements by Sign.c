/*You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.*/

// nums = [3,1,-2,-5,2,-4]

int *rearrangeArray(int *nums, int numsSize, int *returnSize)
{

    int positive = 0, negative = 1, i;

    int *res = (int *)malloc(sizeof(int) * numsSize);

    for (i = 0; i < numsSize; i++)
    {

        if (nums[i] > 0)
        {

            res[positive] = nums[i];

            positive += 2;
        }
        else
        {

            res[negative] = nums[i];

            negative += 2;
        }
    }

    *returnSize = numsSize;

    return res;
}