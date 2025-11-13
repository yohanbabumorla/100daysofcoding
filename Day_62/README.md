🚀 100 Days of Code: Day 62

Array Searching - Finding What You Need

Today shifted focus from modifying arrays to searching within them! Explored three fundamental searching patterns that form the backbone of data retrieval.

🔍 Problem 1: Linear Search

Challenge: Check if a given number exists in the array and return its index (or -1 if not found)
Approach: Implemented classic linear search using index-based iteration. The function returns immediately upon finding the target, or -1 if the element doesn't exist.
Complexity:
⏱️ Time: O(n)
💾 Space: O(1)

Insight: Linear search is the foundation of all searching algorithms. The early return optimization stops searching as soon as we find a match!

📊 Problem 2: Count Occurrences

Challenge: Count how many times a specific number appears in the array
Approach: Used a counter variable and traversed the entire array, incrementing count whenever the target element was found.
Complexity:
⏱️ Time: O(n)
💾 Space: O(1)

Insight: Unlike linear search, this requires checking ALL elements since duplicates can appear anywhere. No early exit possible!

🎯 Problem 3: Find First Occurrence

Challenge: Return the index of the first occurrence of a given number
Approach: Similar to linear search but with explicit edge case handling for empty arrays and clearer messaging when element isn't found.
Complexity:
⏱️ Time: O(n)
💾 Space: O(1)

Insight: This is essentially linear search with better error handling. The key difference from counting is that we can stop at the FIRST match!

💡 Key Distinctions Learned
Today's problems highlighted subtle but important differences:
✅ Early Exit vs Full Traversal:
Linear search & first occurrence: Can stop when found (best case O(1))
Count occurrences: Must check every element (always O(n))
✅ Return Values Matter:
Index-based returns for position-finding
Count-based returns for frequency analysis
-1 or None for "not found" cases
✅ Edge Case Handling:
Empty array checks prevent errors
Clear error messages vs silent failures

🎓 Connecting the Dots
Days 57-60: Reading arrays (traversal, sum, min/max) Day 61: Writing arrays (reverse, swap, replace) Day 62: Searching arrays (find, count, locate) ✨
I'm building a complete toolkit for array operations! Each category builds on the previous one:
Read → Modify → Search
These patterns are appearing everywhere in more complex problems!

hashtag#100DaysOfCode hashtag#Python hashtag#Arrays hashtag#Algorithms hashtag#LinearSearch hashtag#DataStructures hashtag#CodingJourney
