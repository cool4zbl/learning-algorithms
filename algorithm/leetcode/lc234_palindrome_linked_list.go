/**
    https://leetcode.com/problems/palindrome-linked-list/
**/
package algorithm

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	fast, slow := head, head

	for fast.Next != nil && fast.Next.Next != nil {
		slow, fast = slow.Next, fast.Next.Next
	}

	slow = reverseList(slow.Next)

	for slow != nil {
		if slow.Val != head.Val {
			return false
		}
		slow, head = slow.Next, head.Next
	}

	return true

}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode

	for head != nil {
		// next := head.Next
		// head.Next = prev
		// prev = head
		// head = next

		head.Next, prev, head = prev, head, head.Next
	}
	return prev
}
