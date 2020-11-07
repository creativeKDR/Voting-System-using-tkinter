print("Welcome to KDR's Voting System....")
nominee_name = input("Enter Nominee Name:")
nominee2_name = input("Enter Nominee 2nd Name:")
# name = input("Enter Your Name:")
# age = int(input("Enter Your Age:"))
# voteid = int(input("Enter Your Vote Id:"))
vote_id = [1, 2, 3, 4, 5]
vote_len = len(vote_id)
no_of_vote1 = 0
no_of_vote2 = 0

# nominee1 = 1
# nominee2 = 2

while True:
    if vote_id == []:
        print("Voting Session is Over....")
        if no_of_vote1 > no_of_vote2:
            per = (no_of_vote1/vote_len)*100
            print(nominee_name," has Won with", per, "% Votes")
            break

        elif no_of_vote2 > no_of_vote1:
            per = (no_of_vote2/vote_len)*100
            print(nominee2_name," has Won with", per, "% Votes")
            break
    else:
        voter = int(input("Enter Your Voter Id:"))
        if voter in vote_id:
            print("You Are a Voter")
            vote_id.remove(voter)
            vote = int(input("Enter Your Vote:"))
            if vote == 1:
                no_of_vote1 += 1
                print("Thank You For Voting.....")
            elif vote == 2:
                no_of_vote2 += 1
                print("Thank You For Voting.....")
        else:
            print("You Are Not Eligible to Vote or You have already Voted!")
