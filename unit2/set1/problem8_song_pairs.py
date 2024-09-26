#Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, 
# return the number of popular song pairs.

#A pair (i, j) is called popular if 
# the songs have the same popularity score and i < j.

#Hint: number of pairs = (n x n-1)/2

#use a dictionary and/or count to get number of ach value
#then get the values and return each value times itself minus 1 divided by 2


def num_popular_pairs(popularity_scores):
    counts = {}
    for score in popularity_scores:
        if score in counts:
            counts[score] +=1 
        else:
            counts[score] = 1

   
    return sum([i * (i-1)//2 for i in counts.values() if i > 1])

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))