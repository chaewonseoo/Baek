table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) + (6 - t.split().index(lang)) * pref
    print(score)
    print(score.items())
    print(sorted(score.items(), key=lambda item: [-item[1], item[0]]))
    return sorted(score.items(), key=lambda item: [-item[1], item[0]])[0][0]

solution(table, languages, preference)
