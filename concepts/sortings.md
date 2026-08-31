# 🔢 Sorting Algorithms

A concise overview of common sorting algorithms with their definitions, properties, and complexities.

---

## 🫧 Bubble Sort
**Definition**: A simple comparison-based algorithm.  
**Working**: Repeatedly compares adjacent elements and swaps them if they are in the wrong order.  

**Complexities**:  
- ⏳ Best: O(n) (already sorted)  
- ⏳ Average/Worst: O(n²)  
- 💾 Space: O(1)  
- ✅ Stable  

---

## 🌊 Merge Sort
**Definition**: A divide-and-conquer algorithm.  
**Working**: Recursively splits the array, then merges subarrays in sorted order.  

**Complexities**:  
- ⏳ Best/Average/Worst: O(n log n)  
- 💾 Space: O(n)  
- ✅ Stable  

---

## ⚡ Quick Sort
**Definition**: A divide-and-conquer algorithm.  
**Working**: Chooses a pivot, partitions elements into smaller/larger than pivot, then sorts recursively.  

**Complexities**:  
- ⏳ Best/Average: O(n log n)  
- ⏳ Worst: O(n²) (bad pivot choice)  
- 💾 Space: O(log n) (recursive stack)  
- ❌ Not Stable  

---

## 🃏 Insertion Sort
**Definition**: Builds the sorted list one item at a time.  
**Working**: Takes each element and inserts it into its correct place (like sorting playing cards).  

**Complexities**:  
- ⏳ Best: O(n) (nearly sorted)  
- ⏳ Average/Worst: O(n²)  
- 💾 Space: O(1)  
- ✅ Stable  

---

## 🎯 Selection Sort
**Definition**: Finds the minimum (or maximum) and places it in the correct position.  
**Working**: Divides the list into sorted and unsorted parts, growing the sorted region step by step.  

**Complexities**:  
- ⏳ Best/Average/Worst: O(n²)  
- 💾 Space: O(1)  
- ❌ Not Stable  

---

## 📊 Comparison Table

| Algorithm        | Best Case | Average Case | Worst Case | Space    | Stable |
|------------------|-----------|--------------|------------|----------|--------|
| 🫧 Bubble Sort   | O(n)      | O(n²)        | O(n²)      | O(1)     | ✅ Yes |
| 🌊 Merge Sort    | O(n log n)| O(n log n)   | O(n log n) | O(n)     | ✅ Yes |
| ⚡ Quick Sort    | O(n log n)| O(n log n)   | O(n²)      | O(log n) | ❌ No  |
| 🃏 Insertion     | O(n)      | O(n²)        | O(n²)      | O(1)     | ✅ Yes |
| 🎯 Selection    | O(n²)     | O(n²)        | O(n²)      | O(1)     | ❌ No  |

---

## 📝 Memory Trick

- 🫧 **Bubble Sort** → Swap adjacents until sorted  
- 🌊 **Merge Sort** → Split & merge  
- ⚡ **Quick Sort** → Pivot & partition  
- 🃏 **Insertion Sort** → Like sorting cards  
- 🎯 **Selection Sort** → Pick min/max and place  
