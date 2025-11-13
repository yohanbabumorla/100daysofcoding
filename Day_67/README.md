🚀 100 Days of Code: Days 67-68

Binary Search - The Log(n) Breakthrough!

Leveled up from linear O(n) searching to logarithmic O(log n)! These two days introduced me to one of the most elegant algorithms in computer science.

📅 Day 67: Classic Binary Search

Problem 704: Binary Search Find target value in sorted array, return index or -1 if not found.

Approach: Implemented the divide-and-conquer strategy! Started with pointers at both ends, repeatedly halved the search space by comparing middle element with target.

Complexity:
Time: O(log n) 🚀
Space: O(1)

The Magic: Instead of checking every element (O(n)), binary search eliminates half the array with each comparison. For 1 million elements, linear search needs up to 1M checks, binary search needs only ~20!

🔗 https://lnkd.in/gmnSXZfv

📅 Day 68: Search Insert Position

Problem 35: Search Insert Position Find target in sorted array. If found, return index. If not found, return the index where it would be inserted.

Approach: Modified binary search to track potential insert position! Used a buffer variable to remember the last valid position checked.

Complexity:
Time: O(log n)
Space: O(1)

Challenge: The twist here is handling the "not found" case - need to determine correct insertion point to maintain sorted order.

🔗 https://lnkd.in/gCwTWYHC

💡 Binary Search Template Discovered
Both problems follow the same pattern:

1. Initialize left and right pointers
2. While left <= right:
 - Calculate mid point
 - Compare mid with target
 - Adjust search space
3. Handle result

This template is universal for binary search problems!

🎯 Key Learnings

✅ O(log n) is powerful: Massive performance gain over O(n) for large datasets
✅ Sorted arrays unlock optimization: Binary search only works on sorted data
✅ Pattern recognition: Problem 35 is just binary search + insertion logic
✅ Edge cases matter: Handling boundaries (left <= right) is crucial

📊 Algorithm Comparison
Linear Search (Days 62-66): O(n)
Check every element sequentially
Works on unsorted arrays
Binary Search (Days 67-68): O(log n) ✨
Halve search space each step
Requires sorted arrays
100x faster for large datasets

More two-pointer + binary search combos
The jump from O(n) to O(log n) feels like unlocking a superpower!

"Divide and conquer." ⚡
