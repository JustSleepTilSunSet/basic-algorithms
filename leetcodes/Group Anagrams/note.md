# <Problem #2> <Group Anagrams>  (<Medium>)
Link: <https://leetcode.com/problems/group-anagrams/description/>
Status: ☐ Unsolved ✅ Solved (self) ☐ Solved (after hint)  
Last reviewed: 2025-08-09 | Next: D+3

## 0) One-liner
- Problem in one sentence:
    - Use character frequency tuple as the grouping key to avoid hash collisions from total value.

## 1) Constraints → Implications
  

- 1 <= strs.length <= 10^4 -> Needs O(N·L) or better, where L is average word length.
- 0 <= strs[i].length <= 100 -> Support to count each words.
- strs[i] consists of lowercase English letters. -> 26-character alphabet enables.

## 2) Recognized Patterns (pick)
  
- Maps
- Frequency counting

## 3) Approaches
  
### A. Map.
  
#### Idea: 
    
- Tag a unique key for letters.
- If the letters have same composition,it will join to the group of particular key.
  
#### Time complexity:
  
- N is number of strings; L is the average word length.”.
- O(N·L)
  
#### Core:
  
``` python
    """
    alpha_dictionary is a map.

    {"a":0,"b":0,...."z":0}
    """
    # 1. Define alpha dictionary.

    # 2. Frequency.
    for word in content:
        alpha_dictionary[word] = alpha_dictionary[word]+1

    # 3. Generate key string.
    result_key = "" 
    for key in alpha_dictionary.keys():
        if alpha_dictionary[key] == 0:
            continue
        result_key = result_key + (key+str(alpha_dictionary[key]))
    
    if result_board.get(result_key) is None:
        result_board[result_key] = [content]
    else:
        result_board[result_key].append(content)
```
#### Why it fails:
  
##### Key collisions
  
- strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
- "ill" and "duh" have same total value.
    - In this submisison:
        ``` python
            for key in alpha_dictionary.keys():
            if alpha_dictionary[key] == 0:
                continue
            result_key = result_key + (key+str(alpha_dictionary[key]))
        ```

### B. Optimal
  
- Core idea:
    - Binarize content.
    ``` python
    # Group strings by their character frequency
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    result[tuple(count)].append(s)
    ```
  
## 4) Mistakes I made
  
- Used a “total value” key, which causes collisions for different anagrams.
  
## 5) What I learned
  
- Build rule of a key for the map:
  1. Thinking for key of map should avoid collisions.
  2. The key should be simple, deterministic, and cheap to compute.

- "ord" and "chr" there are convert between characters and their ASCII code.
