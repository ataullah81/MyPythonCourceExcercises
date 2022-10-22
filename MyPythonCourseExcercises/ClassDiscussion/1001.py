n = int(input())
roundMatches = 0
totalMatches = 0
teamsAdvance = 0
i = 1
strExplanation = "Explanation: Details of the tournament:\n"
strTotalMatches = "Total number of matches = "
while n > 1:
    if n % 2 == 0:
        teamsAdvance = int(n / 2)
    else:
        teamsAdvance = int(n / 2) + 1

    roundMatches = int(n / 2)
    totalMatches += roundMatches
    strP = ""
    if i == 1:
        strTotalMatches += f"{roundMatches}"
        strP = "st"
    elif i == 2:
        strTotalMatches += f" + {roundMatches}"
        strP = "nd"
    elif i == 3:
        strTotalMatches += f" + {roundMatches}"
        strP = "rd"
    else:
        strTotalMatches += f" + {roundMatches}"
        strP = "th"
    strExplanation += f"- {i}{strP} Round: Teams = {n}, Matches = {roundMatches}, and {teamsAdvance} teams advance.\n"
    i += 1
    n = teamsAdvance
    print(n)
print(totalMatches)
print(strExplanation)
print(strTotalMatches)
