# Next Permutation

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/next-permutation/

---

# Next Permutation - Problem Analysis

## Problem Understanding
The task is to find the next lexicographically greater permutation of an array in-place. If no such permutation exists (the array is in descending order, which is the largest permutation), we must rearrange it to the smallest permutation (ascending order).

## Key Insights
1. **Lexicographic Order**: Similar to dictionary order for sequences
2. **Next Greater Permutation**: We need to find the smallest permutation that is strictly greater than the current one
3. **In-place Constraint**: Must use O(1) extra memory

## Algorithm
The optimal algorithm works as follows:

1. **Find the pivot**: Scan from right to left to find the first index `i` where `nums[i] < nums[i+1]`
   - This is the first position where we can make a larger permutation
   - If no such index exists, the array is in descending order (largest permutation)

2. **Find the swap candidate**: Find the largest index `j > i` such that `nums[j] > nums[i]`
   - This is the smallest element greater than `nums[i]` to the right of position `i`

3. **Swap**: Exchange `nums[i]` and `nums[j]`

4. **Reverse the suffix**: Reverse the subarray from `i+1` to the end
   - This ensures the suffix is in its smallest (ascending) order
   - Making the overall permutation the next smallest greater permutation

## Time and Space Complexity
- **Time Complexity**: O(n) - We make at most 3 passes through the array (finding pivot, finding swap candidate, reversing)
- **Space Complexity**: O(1) - Only using a constant amount of extra memory

## Example Walkthroughs

### Example 1: [1,2,3] → [1,3,2]
- Pivot: i=1 (nums[1]=2 < nums[2]=3)
- Swap candidate: j=2 (nums[2]=3 > nums[1]=2)
- Swap: [1,3,2]
- Reverse suffix (single element): [1,3,2]

### Example 2: [3,2,1] → [1,2,3]
- No pivot found (descending order)
- Reverse entire array: [1,2,3]

### Example 3: [1,1,5] → [1,5,1]
- Pivot: i=1 (nums[1]=1 < nums[2]=5)
- Swap candidate: j=2 (nums[2]=5 > nums[1]=1)
- Swap: [1,5,1]
- Reverse suffix: [1,5,1]

### Example 4: [1,3,2] → [2,1,3]
- Pivot: i=0 (nums[0]=1 < nums[1]=3)
- Swap candidate: j=2 (nums[2]=2 > nums[0]=1)
- Swap: [2,3,1]
- Reverse suffix [3,1] → [1,3]: [2,1,3]

## Correctness Proof

**Lemma 1**: After step 1, the suffix `nums[i+1:]` is in descending order.
*Proof*: By definition, `i` is the rightmost index where `nums[i] < nums[i+1]`, so everything to the right is in descending order.

**Lemma 2**: After step 4, the suffix is in ascending order (minimum order).
*Proof*: Reversing a descending sequence produces an ascending sequence.

**Lemma 3**: The algorithm produces the lexicographically smallest permutation greater than the original.
*Proof**:
- We choose the rightmost position to modify, keeping the prefix as large as possible
- We swap with the smallest element greater than `nums[i]`, ensuring minimal increase
- We sort the suffix in ascending order, ensuring it's the smallest possible suffix

Therefore, the algorithm correctly finds the next permutation.