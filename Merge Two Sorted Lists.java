/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result=new ListNode(-1);
        ListNode list_cur=result;
        while(l1!=null && l2!=null)
        {
            if(l1.val<l2.val)
            {
                list_cur.next=l1;
                l1=l1.next;
            }
            else
            {
                list_cur.next=l2;
                l2=l2.next;
            }
            list_cur=list_cur.next;
        }
        if(l1==null)
            list_cur.next=l2;
        if(l2==null)
            list_cur.next=l1;
        return  result.next;
    }
}
