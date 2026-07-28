def solution(today, terms, privacies):
    answer = []

    # 날짜를 총 일수로 변환
    def convert_date(date):
        year, month, day = map(int, date.split("."))
        return year * 12 * 28 + month * 28 + day

    today_date = convert_date(today)

    # 약관별 유효기간 저장
    term_dict = {}

    for term in terms:
        term_type, period = term.split()
        term_dict[term_type] = int(period)

    # 개인정보별 파기 여부 확인
    for index, privacy in enumerate(privacies):
        collected_date, term_type = privacy.split()

        expiration_date = (
            convert_date(collected_date)
            + term_dict[term_type] * 28
        )

        if expiration_date <= today_date:
            answer.append(index + 1)

    return answer