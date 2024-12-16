from typing import List

def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    # 按房间面积降序排列
    rooms.sort(key=lambda x: x[1], reverse=True)
    results = [-1] * len(queries)
    query_indices = sorted(range(len(queries)), key=lambda x: queries[x][1], reverse=True)
    
    available_rooms = []  # 用于存储可用的房间编号
    room_index = 0
    
    for query_index in query_indices:
        target_room_number, target_size = queries[query_index]
        
        # 将满足面积条件的房间加入可用房间列表，并保持排序
        while room_index < len(rooms) and rooms[room_index][1] >= target_size:
            available_rooms.append(rooms[room_index][0])
            room_index += 1
        
        # 对可用房间进行排序
        available_rooms.sort()
        
        # 查找最接近的房间
        closest_room = -1
        left = 0
        right = len(available_rooms) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if available_rooms[mid] < target_room_number:
                left = mid + 1
            else:
                right = mid - 1
        
        # 检查左侧和右侧的房间
        if left < len(available_rooms):  # 右侧元素
            closest_room = available_rooms[left]
        if right >= 0:  # 左侧元素
            if closest_room == -1 or abs(available_rooms[right] - target_room_number) <= abs(closest_room - target_room_number):
                closest_room = available_rooms[right]
        
        results[query_index] = closest_room

    return results