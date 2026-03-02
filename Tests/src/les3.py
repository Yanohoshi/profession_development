def solve2(phrases: list):
    result = []
    for phrase in phrases:
        clean_phrase = phrase.replace(" ", "").lower()
        if clean_phrase == clean_phrase[::-1]:
           result.append(phrase)
    return result


