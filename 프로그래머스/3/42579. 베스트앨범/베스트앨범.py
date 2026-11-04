def solution(genres, plays):
    answer = []

    # 1. 장르별 총 재생 횟수와 노래 정보 저장
    genre_total = {}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 횟수
        genre_total[genre] = genre_total.get(genre, 0) + play

        # 장르별 노래 정보 (재생 횟수, 고유 번호)
        if genre not in genre_songs:
            genre_songs[genre] = []

        genre_songs[genre].append((play, i))

    # 2. 총 재생 횟수가 많은 장르부터 정렬
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda x: genre_total[x],
        reverse=True
    )

    # 3. 장르별 노래를 재생 횟수 내림차순, 고유 번호 오름차순 정렬
    for genre in sorted_genres:
        songs = sorted(
            genre_songs[genre],
            key=lambda x: (-x[0], x[1])
        )

        # 4. 장르별 최대 2곡 선택
        for play, idx in songs[:2]:
            answer.append(idx)

    return answer