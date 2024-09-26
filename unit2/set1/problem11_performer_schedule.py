def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False #change from True to False. equal length does NOT guarantee match, but unequal length does guarantee that the schedule does NOT follow the pattern

    char_to_genre = {} #
    genre_to_char = {}

    match = False
    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] == genre:
                match = True
                
            else:
                match = False
                break
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] == char:
                match = True
                
            else:
                match = False
                break
        else:
            genre_to_char[genre] = char

    return match

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))