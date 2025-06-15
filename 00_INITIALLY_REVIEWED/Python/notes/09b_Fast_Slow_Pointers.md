# Fast & Slow Pointers

<details>
<summary><strong>💡 Fast/Slow Pointer Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Fast/Slow Pointers: Off-by-one errors in cycle detection
# 2. Not handling edge cases (empty list, single node)
# 3. Forgetting to check if fast.next exists before fast.next.next
# 4. Wrong mathematical reasoning for cycle detection

# ✅ BEST PRACTICES:
# 1. Always check fast and fast.next before moving fast pointer
# 2. Use Floyd's cycle detection algorithm for cycle problems
# 3. Two-phase approach: detect cycle, then find cycle start
# 4. Consider dummy node for edge cases in linked list modifications

# 🎯 WHEN TO USE FAST/SLOW POINTERS:
# - Cycle detection in linked lists or arrays
# - Finding middle element of linked list
# - Detecting palindromes in linked lists
# - Removing nth node from end
```

</details>



<details>
<summary><strong>Fast & Slow Pointers</strong></summary>

```python
# Time Complexity: O(n) for most two-pointer problems
# Space Complexity: O(1)

# 🧠 KEY INSIGHT: Fast/slow pointers detect cycles and find middle elements
# Fast moves 2 steps, slow moves 1 step - they meet if there's a cycle

# Linked List Cycle
# Problem: Detect if linked list has a cycle
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# 💡 INSIGHT: If there's a cycle, fast will eventually catch up to slow
# Think of it as two runners on a circular track

# Find Cycle Start
# Problem: Find the node where cycle begins
def detect_cycle(head):
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if cycle exists
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find cycle start
    # Move one pointer to head, keep other at meeting point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# 🧠 MATHEMATICAL INSIGHT: Why does this work?
# If cycle starts at distance 'a' from head and has length 'c':
# When they meet, slow traveled 'a + b', fast traveled 'a + b + c'
# Since fast = 2 * slow: a + b + c = 2(a + b) → c = a + b
# So distance from head to cycle start = distance from meeting point to cycle start

# Find Duplicate Number
# Problem: Find duplicate number in array containing n+1 integers from 1 to n
def find_duplicate(nums):
    # Treat array as implicit linked list
    # nums[i] points to nums[nums[i]]
    
    # Phase 1: Find intersection point
    slow = fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# 💡 INSIGHT: This is Floyd's cycle detection applied to arrays!
# The duplicate number is the "cycle start" in the implicit linked list

# Happy Number
# Problem: Determine if number is happy (sum of squares of digits eventually becomes 1)
def is_happy(n):
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    
    while True:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
        if fast == 1:
            return True
        
        if slow == fast:  # Cycle detected
            return False

# Find Middle of Linked List
def find_middle(head):
    """Find middle node of linked list"""
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Palindrome Linked List
def is_palindrome_linked_list(head):
    """Check if linked list is palindrome"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(slow)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Remove Nth Node From End
def remove_nth_from_end(head, n):
    """Remove nth node from end of linked list"""
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node from end
    second.next = second.next.next
    
    return dummy.next

# Reorder List
def reorder_list(head):
    """Reorder list: L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→..."""
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Split into two halves
    second_half = slow.next
    slow.next = None
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(second_half)
    
    # Merge two halves
    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        
        first_half.next = second_half
        second_half.next = temp1
        
        first_half = temp1
        second_half = temp2
```

</details> 