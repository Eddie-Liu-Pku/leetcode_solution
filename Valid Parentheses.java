class Solution {
    public boolean isValid(String s) 
    {
        char[] arr=s.toCharArray();
        Stack<Character> stack_temp=new Stack<Character> ();
        stack_temp.push(arr[0]);
        for(int i=1;i<s.length();i++)
        {
            if(stack_temp.isEmpty()!=true&& isMatch(stack_temp.peek(),arr[i]))
                stack_temp.pop();
            else
                stack_temp.push(arr[i]);
        }
        if(stack_temp.isEmpty())
            return true;
        else return false;
    }
    public boolean isMatch(char ch1, char ch2)
    {
        if((ch1=='(' && ch2==')')||(ch1=='[' && ch2==']')||(ch1=='{' && ch2=='}'))
            return true;
        else
            return false;
    }
}
