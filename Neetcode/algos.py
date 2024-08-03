def removeDuplicates(arr):
    l = 1
    for r in range(1,len(arr)):
        if arr[r-1] !=arr[r]:
            arr[l] = arr[r]
            l+=1
    return l

def removeElement(arr, val):
    l = 0
    for r in range(len(arr)):
        if arr[r] != val:
            arr[l] = arr[r]
            l+=1
    return l

# rmeove Kth samllerst element from BST
def KthSamllestBST(root,k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.value
        root = root.right