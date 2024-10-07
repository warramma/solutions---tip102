from collections import deque
def edit_post(post):
    queue = deque()
    words = post.split()
    for word in words:
        queue.appendleft(word[::-1])
    result = []
    while queue:
        result.append(queue.pop())
    return " ".join(result)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 