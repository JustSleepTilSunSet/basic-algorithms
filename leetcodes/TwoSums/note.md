# <Problem #1> <Two Sum>  (<Easy>)
Link: <https://leetcode.com/problems/two-sum/description/>
Status: ☐ Unsolved ✅ Solved (self) ☐ Solved (after hint)  
Last reviewed: 2025-08-03 | Next: D+3

## 0) One-liner
- Problem in one sentence:
    - Find two distinct indices `i` and `j` such that `nums[i] + nums[j] == target`.

## 1) Constraints → Implications

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer → no need to handle multiple or ambiguous solutions.
- Large range of nums → must avoid brute-force (O(n²)) for performance.

## 2) Recognized Patterns (pick)
- Array/Hash

## 3) Approaches
### A. Map.
- Idea: 
    - Use a map to store previously seen numbers while iterating.
- Time complexity:
    - n is length of num list.
    - O(n)
- Why it fails:
    - nums = [-3,4,3,90] target = 0
        - In this submisison:
        ``` python
            if num > target: # This unexpectable input.
                continue
        ```
    - nums = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1] target = 11
        - In this submisison:
        ``` python
            if lookup.get(pair) is None:
                lookup[pair] = index # It's wrong index.
            else:
                return [lookup[pair],index] # If the solution be matched, will output wrong answer.
        ```
### B. Optimal
- Core idea (1–3 bullets):
    - Match pair in specify map.
    ``` python
        # Traverse nums.
        index = 0
        for num in nums:
            pair = target - num
            if lookup.get(pair) is None:
                lookup[pair] = index
            else:
                return [lookup[pair],index]
            lookup[num]=index
            index+=1
        return []
    ```
  
## 4) Mistakes I made (for review)
- Thought the input list was sorted.
- Misused `map.get(pair)` and inserted wrong index.
  
## 5) What I learned
- Don't assume input structure (e.g., sorted) unless stated.
- Always update the map after checking for match.