def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = []
    answer = 0

    for city in cities:
        city = city.lower()

        if city in cache:          # Cache Hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:                      # Cache Miss
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5

    return answer