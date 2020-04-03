# TODO add persistence of votes

class Vote:

    def __init__(self, name):
        self.message = None
        self.name = name
        self.options = []

    def addOption(self, option):
        self.options.append((option, []))

    def voteForOption(self, option, voter):
        try:
            index = int(option) - 1
        except:
            index = next((i for i in range(0, len(self.options)) if self.options[i][0] == option), None) 
        if index is not None and index >= 0 and index < len(self.options):
            self.removeVoterFromAllOptions(voter)
            self.options[index][1].append(voter)
        else:
            raise ValueError

    def removeVoterFromAllOptions(self, voter):
        for option, voters in self.options:
            if voter in voters:
                voters.remove(voter)

votes = []

def getVoteByName(name):
    return next((v for v in votes if v.name == name), None)

def determineVote(name):
    if not name:
        if len(votes) > 0:
            return votes[-1]
        else:
            return None
    else:
        return getVoteByName(name)

def addVote(name):
    if getVoteByName(name) or not name:
        raise ValueError
    vote = Vote(name)
    votes.append(vote)
    return vote

def addOptionToVote(name, option):
    vote = determineVote(name)
    if not vote or not option: 
        raise ValueError
    vote.addOption(option)
    return vote

def voteForOption(name, option, voter):
    vote = determineVote(name)
    if not vote or not option:
        raise ValueError
    vote.voteForOption(option, voter)
    return vote

def closeVote(name):
    vote = determineVote(name)
    if not vote:
        raise ValueError
    votes.remove(vote)
    return vote

