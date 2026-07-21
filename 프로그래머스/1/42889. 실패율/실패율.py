def solution(N, stages):
    failure_rates = []
    challengers = len(stages)

    for stage in range(1, N + 1):
        failed_users = stages.count(stage)

        if challengers == 0:
            failure_rate = 0
        else:
            failure_rate = failed_users / challengers

        failure_rates.append((stage, failure_rate))
        challengers -= failed_users

    failure_rates.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, rate in failure_rates]