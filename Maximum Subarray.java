class Solution {
    public int maxSubArray(int[] nums) {
        int sum=Integer.MIN_VALUE,temp=0;
        
        for(int i=0;i<nums.length;i++)
        {
            if(temp<0)
                temp=nums[i];
            else
                temp=temp+nums[i];
            if(temp>sum)
                sum=temp;
        }
        return sum;
    }
}
