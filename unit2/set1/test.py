# #problem 1-------------------------------------------------
# def lineup(artists, set_times):
# 	zipped = zip(artists, set_times)
# 	print(dict(zipped))

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []


# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))



#problem 2-----------------------------------------------
# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
# 	    return {'message': 'Artist not found'}

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

# #problem 3------------------------------------------------
# def total_sales(ticket_sales):
#     return sum(ticket_sales.values())

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

# def total_sales2(ticket_sales):
#     sum = 0
#     for ticket in ticket_sales:
#         sum += ticket_sales[ticket]
    
#     return sum

# print(total_sales(ticket_sales))


#problem 4 - scheduling conflict------------------------------
# def identify_conflicts(venue1_schedule, venue2_schedule):
#     conflicts = {}
#     for artist in venue1_schedule:
#         if artist in venue2_schedule and venue1_schedule[artist]==venue2_schedule[artist]:
#             conflicts[artist] = venue1_schedule[artist]
#     return conflicts

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))

#problem 5 ----------------------------------------------
