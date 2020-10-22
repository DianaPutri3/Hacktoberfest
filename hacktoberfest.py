class participant:
    def __init__(self, name, age, pr):
        self.name = name
        self.age = age
        self.pr = pr

    def getPullRequests(self):
        return self.pr

    def getName(self):
        return self.name


class tshirts:
    def __init__(self, name):
        self.name = name
        self.owners = []

    def send_tshirt(self, participant):
        if participant.getPullRequests() >= 4:
            self.owners.append(participant)
            return True

    def getNames(self, part):
        for part in self.owners:
            print(part.getName())


p1 = participant("Max", 18, 4)
p2 = participant("Jonas", 21, 4)

shirt1 = tshirts("Hacktoberfest Tshirt")
shirt1.send_tshirt(p1)
shirt1.send_tshirt(p2)

shirt1.getNames(shirt1)
