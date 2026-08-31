from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)

    time = 0
    current_weight = 0

    for truck in truck_weights:
        while True:
            time += 1

            # 다리에서 트럭 한 대가 나감
            current_weight -= bridge.popleft()

            # 현재 트럭이 올라갈 수 있으면 진입
            if current_weight + truck <= weight:
                bridge.append(truck)
                current_weight += truck
                break

            # 못 올라가면 빈칸 유지
            bridge.append(0)

    # 마지막 트럭이 다리를 건너는 시간
    return time + bridge_length