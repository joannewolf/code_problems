teamNumber = 7
courtNumber = 2
beStaff = False

def printResult(schedule):
    roundLen = len(schedule)
    allTeams = set(range(1, teamNumber + 1))
    for i in range(roundLen):
        roundSize = len(schedule[i])
        playedTeams = set()
        print("Round {:d}: ".format(i), end = " ")
        if not beStaff:
            for j in range(0, roundSize, 2):
                firstTeam = min(schedule[i][j], schedule[i][j + 1])
                secondTeam = max(schedule[i][j], schedule[i][j + 1])
                print("({:d}, {:d}) ".format(firstTeam, secondTeam), end = " ")
                playedTeams.add(schedule[i][j])
                playedTeams.add(schedule[i][j + 1])
        else:
            for j in range(0, roundSize, 3):
                firstTeam = min(schedule[i][j], schedule[i][j + 1])
                secondTeam = max(schedule[i][j], schedule[i][j + 1])
                print("({:d}, {:d}) [{:d}]".format(firstTeam, secondTeam, schedule[i][j + 2]), end = " ")
                playedTeams.add(schedule[i][j])
                playedTeams.add(schedule[i][j + 1])
                playedTeams.add(schedule[i][j + 2])

        breakTeams = allTeams - playedTeams
        print("break: ", end = "")
        print(*breakTeams, sep = ", ")

def getSchedule():
    schedule = []
    teams = list(range(0, teamNumber + 1)) if (teamNumber % 2 == 1) else list(range(1, teamNumber + 1))

    for i in range(1, len(teams)):
        temp = list([teams[0]]) + teams[i:] + teams[1:i]
        round = []
        for j in range(0, int(len(teams) / 2)):
            if temp[j] != 0 and temp[len(teams) - j - 1] != 0:
                round.append(temp[j])
                round.append(temp[len(teams) - j - 1])
        for j in range(0, len(round), courtNumber * 2):
            schedule.append(round[j : j + courtNumber * 2])
        # schedule.append(round)
    # else:
    # to-do
    return schedule

printResult(getSchedule())