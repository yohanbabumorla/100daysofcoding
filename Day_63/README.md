🚀 100 Days of Code: Day 63

Array Creation - Building From Scratch

Today explored array creation patterns - learning how to generate new arrays programmatically rather than working with existing ones. Discovered multiple ways to solve the same problem!

📐 Problem 1: Create Array of Squares

Challenge: Given a number n, create an array [1, 4, 9, 16, ...] up to n²
Approach: Looped from 1 to n, squared each number, and appended to a new array.

Complexity:
⏱️ Time: O(n)
💾 Space: O(n)

Insight: Building arrays dynamically requires both time (for computation) and space (to store results). The trade-off is unavoidable when creating new data!

🎨 Problem 2: Fill Array with a Value

Challenge: Create an array of size n filled with a specific number
Approach - Version 1 (Loop-based): Iterated n times, appending the value each time.

⏱️ Time: O(n)
💾 Space: O(n)

Approach - Version 2 (Python idiom): Used list multiplication: [val] * num

⏱️ Time: O(1) ✨
💾 Space: O(n)

Major Insight: Python's list multiplication is a built-in optimization! Instead of explicit looping (O(n)), it uses internal C-level operations making it effectively O(1) for the operation itself. This is a game-changer for filling arrays!

📋 Problem 3: Copy an Array

Challenge: Create a duplicate of an existing array
Approach - Manual Method: Looped through original array and appended each element to a new array.
Alternative Python Methods Discovered:
copied_array = array[:] (slicing)
copied_array = list(array) (type conversion)

Complexity (All methods):

⏱️ Time: O(n)
💾 Space: O(n)

Insight: Multiple ways to achieve the same result! While the manual loop helps understand the process, Python's built-in methods are more concise and often optimized under the hood.

💡 Key Learnings
Today's session revealed important patterns in array creation:
✅ Space-Time Relationship: Array creation almost always requires O(n) space - you can't create n elements without using n space!
✅ Python Idioms vs Explicit Loops: Built-in Python operations can be more efficient than manual loops
✅ Multiple Solutions: There's often more than one way to solve a problem - understanding trade-offs is key
✅ Shallow vs Deep Copy Awareness: Today's copying creates shallow copies - important to know for nested structures!

🎯 Pattern Recognition
Days 57-60: Reading arrays (traversal fundamentals) Day 61: Modifying arrays (transformations) Day 62: Searching arrays (finding elements) Day 63: Creating arrays (generation) ✨

The foundation is solid! Ready for more complex array algorithms.
