# algorithm.py
def bubble_sort_generator(arr):
    """
    純邏輯：每次發生比較或交換時，yield 當前的狀態。
    回傳格式：(目前陣列狀態, 正在比較的索引1, 正在比較的索引2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # 狀態 1：準備比較
            yield (arr.copy(), j, j+1)
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # 狀態 2：發生交換後
                yield (arr.copy(), j, j+1)
