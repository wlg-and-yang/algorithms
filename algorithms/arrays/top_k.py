from collections import Counter
import heapq

def top_k(arr, k):
    # 使用Counter来计算每个元素的出现次数
    # counts = Counter(arr)
    if k <= len(arr):
        arr.sort(reverse=True)
        top_k_elements = arr[:k]
    else:
        return -1
        # assert k <= len(arr), f"k的值({k})超出了arr的长度({len(arr)})"
    
    # # 使用heapq.nlargest来找到出现次数最多的前k个元素
    # # 返回的是一个元组列表，每个元组的形式为(出现次数, 元素)
    # top_k_elements = heapq.nlargest(k, counts.items(), key=lambda x: x[1])
    
    # # 提取元素
    # top_k_elements = [element for count, element in top_k_elements]
    
    return top_k_elements

# print(top_k([1, 2, 3, 2, 3, 4, 4, 4], 9))
