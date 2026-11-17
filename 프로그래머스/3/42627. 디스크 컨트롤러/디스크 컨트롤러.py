import heapq

def solution(jobs):
    answer = 0
    time = 0
    idx = 0
    count = 0

    # 요청 시각을 기준으로 정렬
    jobs.sort()

    # 작업 대기 큐
    heap = []

    while count < len(jobs):

        # 현재 시점까지 요청된 작업을 힙에 추가
        while idx < len(jobs) and jobs[idx][0] <= time:
            request, duration = jobs[idx]
            heapq.heappush(heap, (duration, request))
            idx += 1

        if heap:
            # 소요 시간이 가장 짧은 작업 선택
            duration, request = heapq.heappop(heap)

            # 작업 종료 시각 갱신
            time += duration

            # 반환 시간 누적
            answer += time - request

            count += 1

        else:
            # 처리할 작업이 없다면 다음 요청 시각으로 이동
            time = jobs[idx][0]

    return answer // len(jobs)