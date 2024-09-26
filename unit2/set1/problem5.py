#problem 5------------
# As part of the festival, attendees cast
# votes for their favorite set. 
# Given a dictionary votes that maps
# attendees id numbers to the artist they voted for, 
# return the artist that had the most number of votes. 
# If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    my_dict = {}
    for voter in votes:
        artist = votes[voter]
        if artist in my_dict:
            my_dict[artist] += 1
        else:
            my_dict[artist] = 1
    
    artists = list(my_dict.keys())
    num_votes = list(my_dict.values())
    
    return artists[num_votes.index(max(num_votes))]

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))