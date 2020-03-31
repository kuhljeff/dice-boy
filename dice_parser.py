from re import compile
from random import randint

class BaseComponent:
    def evaluate(self):
        pass

class RollComponent(BaseComponent):
    
    def __init__(self):
        self.count = "" 
        self.die = ""

    def evaluate(self):
        total = 0
        rolls = []
        countInt = int(self.count)
        dieInt = int(self.die)
        for i in range(0, countInt):
            roll = randint(1, dieInt)
            total += roll
            rolls.append(roll)
        return total, rolls

class ConstantComponent(BaseComponent):

    def __init__(self):
        self.count = ""

    def evaluate(self):
        countInt = int(self.count)
        return countInt, [countInt]

def parseSingle(rollString) -> "BaseComponent":
    rollString = rollString.lower().replace(" ", "")
    if "d" in rollString:
        roll = RollComponent()
    else:
        roll = ConstantComponent()
    buildCount = True
    for c in rollString:
        if c == "d":
            buildCount = False
            continue
        if buildCount:
            roll.count += c
        else:
            roll.die += c
    return roll

def parse(rollString): 
    rollRegex = compile(r"\b(\d+\s*[dD]\s*\d+|\d+)\b")
    opRegex = compile(r"\+|\-")
    rolls = list(map(parseSingle, rollRegex.findall(rollString)))
    ops = opRegex.findall(rollString)
    if len(rolls) != len(ops) + 1:
        raise ValueError("Wrong number of args")
    first = rolls.pop(0)
    total, individuals = first.evaluate()
    for i in range(0, len(rolls)):
        op = ops[i]
        roll = rolls[i]
        nextRoll, nextIndividuals = roll.evaluate()
        if op == "+":
            total += nextRoll
            individuals.extend(nextIndividuals)
        else:
            total -= nextRoll
            nextIndividuals = map(lambda r : r * -1, nextIndividuals)
            individuals.extend(nextIndividuals)
    return total, individuals 
