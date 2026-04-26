from collections import deque
#TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ─── Task 1
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print("=" * 50)
print("Task 1-Two Sum")
print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(twoSum([3, 2, 4], 6))        # [1, 2]
print(twoSum([3, 3], 6))           # [0, 1]


# ─── Task 2
def firstUniqChar(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


print("=" * 50)
print("Task 2-First Non-Repeating Character")
print(firstUniqChar("leetcode"))       # 0
print(firstUniqChar("loveleetcode"))   # 2
print(firstUniqChar("aabb"))           # -1


# ─── Task 3
def isIsomorphic(s, t):
    s_to_t, t_to_s = {}, {}
    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            if ct in t_to_s:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
    return True


print("=" * 50)
print("Task 3-Isomorphic Strings")
print(isIsomorphic("egg", "add"))    # True
print(isIsomorphic("foo", "bar"))    # False
print(isIsomorphic("paper", "title"))  # True


# ─── Task 4
def isHappy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True


print("=" * 50)
print("Task 4-Happy Number")
print(isHappy(19))   # True
print(isHappy(2))    # False
print(isHappy(1))    # True


# ─── Task 5
def levelOrder(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result


print("=" * 50)
print("Task 5-Level Order Traversal")
print(levelOrder(build_tree([3, 9, 20, None, None, 15, 7])))  # [[3],[9,20],[15,7]]
print(levelOrder(build_tree([1])))                             # [[1]]
print(levelOrder(None))                                        # []


# ─── Task 6
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


print("=" * 50)
print("Task 6-Maximum Depth")
print(maxDepth(build_tree([3, 9, 20, None, None, 15, 7])))  # 3
print(maxDepth(build_tree([1, None, 2])))                    # 2
print(maxDepth(None))                                        # 0


# ─── Task 7
def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right: return True
        if not left or not right:  return False
        return (left.val == right.val and
                isMirror(left.left,  right.right) and
                isMirror(left.right, right.left))
    return isMirror(root.left, root.right)


print("=" * 50)
print("Task 7-Symmetric Tree")
print(isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))          # True
print(isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))     # False


# ─── Task 8
def longestConsecutive(root):
    result = [0]
    def dfs(node, parent_val, length):
        if not node: return
        length = length + 1 if node.val == parent_val + 1 else 1
        result[0] = max(result[0], length)
        dfs(node.left,  node.val, length)
        dfs(node.right, node.val, length)
    dfs(root, root.val - 1, 0)
    return result[0]


print("=" * 50)
print("Task 8-Longest Consecutive Path")
# Tree: 1 → 3 → [2, 4 → 5]  longest: 3→4→5 = 3
root8 = build_tree([1, None, 3, 2, 4, None, None, None, 5])
print(longestConsecutive(root8))           # 3
print(longestConsecutive(build_tree([1, 2, 3])))  # 2 (1→2)


# ─── Task 9
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


print("=" * 50)
print("Task 9-Sort Colors")
a = [2, 0, 2, 1, 1, 0]; sortColors(a); print(a)  # [0,0,1,1,2,2]
b = [2, 0, 1];           sortColors(b); print(b)  # [0,1,2]
c = [0];                 sortColors(c); print(c)  # [0]


# ─── Task 10
def quickSort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quickSort(nums, low, pi - 1)
        quickSort(nums, pi + 1, high)


print("=" * 50)
print("Task 10-Quick Sort")
a = [3, 6, 8, 10, 1, 2, 1]; quickSort(a); print(a)  # [1,1,2,3,6,8,10]
b = [5, -1, 0, 3];          quickSort(b); print(b)  # [-1,0,3,5]
c = [1];                     quickSort(c); print(c)  # [1]


# ─── Task 11
def mergeSort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i];  i += 1
        else:
            nums[k] = right[j]; j += 1
        k += 1
    while i < len(left):  nums[k] = left[i];  i += 1; k += 1
    while j < len(right): nums[k] = right[j]; j += 1; k += 1


print("=" * 50)
print("Task 11-Merge Sort")
a = [5, 2, 4, 6, 1, 3]; mergeSort(a); print(a)  # [1,2,3,4,5,6]
b = [9, 7, 5, 3, 1];    mergeSort(b); print(b)  # [1,3,5,7,9]
c = [1];                 mergeSort(c); print(c)  # [1]


# ─── Task 12
def heapSort(nums):
    n = len(nums)

    def heapify(n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and nums[l] > nums[largest]: largest = l
        if r < n and nums[r] > nums[largest]: largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(i, 0)


print("=" * 50)
print("Task 12-Heap Sort")
a = [12, 11, 13, 5, 6, 7]; heapSort(a); print(a)  # [5,6,7,11,12,13]
b = [4, 2, 9, 1, 8];       heapSort(b); print(b)  # [1,2,4,8,9]
c = [1];                    heapSort(c); print(c)  # [1]

print("=" * 50)
