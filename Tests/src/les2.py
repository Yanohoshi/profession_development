def solve(boys: list, girls: list):
    result = ""  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"

    if len(boys) == len(girls):
        sorted_boys = sorted(boys)
        sorted_girls = sorted(girls)

        pairs = []
        for boy, girl in zip(sorted_boys,
                             sorted_girls):
            pairs.append(f"{boy} и {girl}")

        result = ", ".join(pairs)
    else:
        result = "Кто-то может остаться без пары!"
    return result
