#analyze given solution

def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result


def two_pointer_approach(engagements):
    left = 0
    right = len(engagements) - 1
    results = [0] * len(engagements)
    spot = len(results) - 1

    while left <= right:
        if abs(engagements[left]) > abs(engagements[right]):
            results[spot] = engagements[left] ** 2
            left += 1
        else:
            results[spot] = engagements[right] ** 2
            right -= 1
        spot -= 1
        
    return results


print(two_pointer_approach([-4, -1, 0, 3, 10]))
print(two_pointer_approach([-7, -3, 2, 3, 11]))