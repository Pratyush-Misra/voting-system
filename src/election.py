import os
# import main as m


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

    # def addCandidate(self, c: m.Candidate):
    #     if self.has_ended == False and self.is_open == False:
    #         if c in self.candidates_with_votes.keys():
    #             print('Candidate Already Registered\n')
    #         else:
    #             self.candidates_with_votes[c] = 0

    #     elif self.has_ended == False and self.is_open == True:
    #         print('Voting Has Already Started!!\n')

    #     else:
    #         print(
    #             f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!\n')

    # def removeCandidate(self, c: m.Candidate):
    #     if self.has_ended == False and self.is_open == False:
    #         if c in self.candidates_with_votes.keys():
    #             del self.candidates_with_votes[c]
    #             print('Candidate Removed!\n')
    #         else:
    #             print('Candidate Is Not Registered For The Election.\n')

    #     elif self.has_ended == False and self.is_open == True:
    #         print('Voting Has Already Started!!')

    #     else:
    #         print(
    #             f'Election Has Ended\n{self.winner} Won The Election with {self.candidates_with_votes[self.winner]} Votes!!')

    # def addVote(self, c: m.Candidate, v: m.Voter):
    #     if v in self.voters:
    #         print('You Have Already Voted')
    #     else:
    #         self.candidates_with_votes[c] += 1
    #         self.voters.add(v.unique_id)
    #         print('Vote Casted!')

    # def announceWinner(self):
    #     if self.has_ended == True:
    #         max_votes = 0
    #         for candidate in self.candidates_with_votes.keys():
    #             if self.candidates_with_votes[candidate] > max_votes:
    #                 self.winner = candidate
    #                 max_votes = self.candidates_with_votes[candidate]
    #         return self.winner
    #     else:
    #         print(f'Voting Is Still In Process!! Cannot Announce Winner')

    # def __str__(self):
    #     term_size = os.get_terminal_size()
    #     print("-" * term_size.columns)
    #     return (f'\nName : {self.name}\nPosition : {self.positionOfInterest}\nDescription : {self.desc}\nArea Code : {self.areaCode}\n')
