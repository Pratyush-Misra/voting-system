import os
# from abc import ABC, abstractmethod


# class VoteCaster(ABC):
#     @abstractmethod
#     def caste_vote(self):
#         pass



class Party:
    name = ""
    party_members = []


class Voter:
    name = ""
    age = 0
    unique_id = ""

    def __init__(self, name, age, u_id):
        self.name = name
        self.age = age
        self.unique_id = u_id


class Candidate:
    name = ""
    age = 0
    unique_id = ""
    party_name = ""


class Election:
    name = ""
    desc = ""
    position_of_interest = ""
    area_code = ""
    is_open = False
    has_ended = False
    winner = ""

    def __init__(self, name, desc, poi, a_code):
        self.name = name
        self.desc = desc
        self.position_of_interest = poi
        self.area_code = a_code
        self.candidates_with_votes = dict()
        self.voters = set()

    def addCandidate(self, c: Candidate):
        if self.has_ended == False and self.is_open == False:
            if c in self.candidates_with_votes.keys():
                print('Candidate Already Registered\n')
            else:
                self.candidates_with_votes[c] = 0

        elif self.has_ended == False and self.is_open == True:
            print('Voting Has Already Started!!\n')

        else:
            print(
                f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!\n')

    def removeCandidate(self, c: Candidate):
        if self.has_ended == False and self.is_open == False:
            if c in self.candidates_with_votes.keys():
                del self.candidates_with_votes[c]
                print('Candidate Removed!\n')
            else:
                print('Candidate Is Not Registered For The Election.\n')

        elif self.has_ended == False and self.is_open == True:
            print('Voting Has Already Started!!')

        else:
            print(
                f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!')

    def addVote(self, c: Candidate, v: Voter):
        if v in self.voters:
            print('You Have Already Voted')
        else:
            self.candidates_with_votes[c] += 1
            self.voters.add(v.unique_id)
            print('Vote Casted!')

    def announceWinner(self):
        if self.has_ended == True:
            max_votes = 0
            for candidate in self.candidates_with_votes.keys():
                if self.candidates_with_votes[candidate] > max_votes:
                    self.winner = candidate
                    max_votes = self.candidates_with_votes[candidate]
            return self.winner
        else:
            return 'Voting Is Still In Process!! Cannot Announce Winner'

    def __str__(self):
        term_size = os.get_terminal_size()
        print("-" * term_size.columns)
        return (f'\nName : {self.name}\t\t\t\t\t\t\t\t\t\t\t\t\t\t Open : {self.is_open}\nPosition : {self.position_of_interest}\nDescription : {self.desc}\nArea Code : {self.area_code}\n')


class ElectionCommission:
    all_voters = None
    all_elections = None
    list_of_open_elections = None

    def __init__(self):
        self.all_voters = dict()
        self.all_elections = dict()
        self.list_of_open_elections = dict()

    def createElection(self, name, desc, poi, a_code):
        e = Election(name, desc, poi, a_code)
        if a_code not in self.all_elections.keys():
            self.all_elections[a_code] = list()

        self.all_elections[a_code].append(e)

    def openElection(self, e: Election):
        if e.has_ended == False:
            if e.is_open == True:
                print('Election Already Open For Voting\n')
            else:
                e.is_open = True
                if e.area_code not in self.list_of_open_elections.keys():
                    self.list_of_open_elections[e.area_code] = list()

            self.list_of_open_elections[e.area_code].append(e)
            print('Election Open For Voting !!\n')

        else:
            print(
                f'Election Has Ended\n{e.winner} Won The Election with {e.candidates_with_votes[e.winner]} Votes!!')

    def closeElection(self, e: Election):
        if e.has_ended == False:
            if e.is_open == False:
                print('Election is Already Closed For Voting\n')
            else:
                print('Election Closed For Voting !! Waiting For Results..\n')

        else:
            print(
                f'Election Has Ended\n{e.winner} Won The Election with {e.candidates_with_votes[e.winner]} Votes!!')

    def endElection(self, e: Election):
        if e.has_ended:
            print(
                f'Election Has Ended\n{e.winner} Won The Election with {e.candidates_with_votes[e.winner]} Votes!!')
        else:
            e.has_ended = True
            print('Election Ended!! Waiting For Winner Declaration!!')

    def showAllElections(self):
        for area in self.all_elections:
            print(area)
            for election in self.all_elections[area]:
                print(election)

    def submitNomination(self, e: Election, c: Candidate):
        e.addCandidate(c)

    def cancelNomination(self, e: Election, c: Candidate):
        e.removeCandidate(c)

    def getWinner(self, e: Election):
        print(e.announceWinner().name)


class Login:
    user_name = ""
    password = ""

    pass


class VotingSystem:
    choice = 0
    ec = None

    def __init__(self):
        self.ec = ElectionCommission()
        print("\t\te-Voting System\t\t\n")
        print("[1] : Login\n")
        print("[2] : New User? SignUp\n")
        while self.choice not in [1, 2]:
            self.choice = int(input("Please input your choice (1 or 2)\n"))

    def authenticate(self):
        if self.choice == 1:
            pass
        elif self.choice == 2:
            pass
        else:
            pass


if __name__ == "__main__":
    ec = ElectionCommission()
    print(len(ec.all_elections))
    ec.createElection(
        "Lok Sabha", "kjsadj hag ahsgdAHUJDG yags ahgsvdJAGHSDV jhgvsdahg", "MLA", "D92")
    print(len(ec.all_elections))
    v = VotingSystem()
    pass
