# You are given an array audiences consisting of positive integers
# representing the audience size for different performances at a music festival.
# Return the combined audience size of all performances in audiences 
# with the maximum audience size.

# The audience size of a performance is 
# the number of people who attended that performance.

#input = array
#output = maxaudience * number of max occurances

def max_audience_performances(audiences):
    max_audience = max(audiences)

    my_dict = {}

    for audience in audiences:
        if audience == max_audience:
            if max_audience in my_dict:
                my_dict[max_audience] +=1
            else:
                my_dict[max_audience] = 1

    return max_audience * my_dict[max_audience]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))