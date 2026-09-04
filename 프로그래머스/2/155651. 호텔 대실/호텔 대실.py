import heapq

def solution(book_time):
    def convert(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    books = []

    for start, end in book_time:
        books.append((convert(start), convert(end)))

    books.sort()

    heap = []

    for start, end in books:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end + 10)

    return len(heap)