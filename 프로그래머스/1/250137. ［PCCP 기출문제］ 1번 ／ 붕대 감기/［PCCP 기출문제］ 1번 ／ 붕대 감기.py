def solution(bandage, health, attacks):
    t, x, y = bandage

    hp = health          # 현재 체력
    combo = 0            # 연속 성공 횟수

    attack_idx = 0
    last_time = attacks[-1][0]

    for time in range(1, last_time + 1):

        # 공격 시간인 경우
        if attack_idx < len(attacks) and time == attacks[attack_idx][0]:
            hp -= attacks[attack_idx][1]

            if hp <= 0:
                return -1

            combo = 0
            attack_idx += 1

        # 공격이 없는 경우
        else:
            combo += 1
            hp = min(health, hp + x)

            if combo == t:
                hp = min(health, hp + y)
                combo = 0

    return hp