def is_symmetrical_title(title):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    stripped = "".join([char for char in title.lower() if char in letters])
   
    start = 0
    end = len(stripped) - 1

    while start < end:
        if stripped[start] != stripped[end]:
            return False
        start += 1
        end -= 1
    
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 