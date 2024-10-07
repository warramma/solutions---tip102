def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    
    output = []
    while stack:
        output.append(stack.pop())
    
    return output

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))