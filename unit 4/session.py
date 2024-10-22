##problem 3 -----
#time complexity = O(n)

# def identify_popular_creators(nft_collection):
#     freq_dict = {}
#     for nft in nft_collection: 
#         artist_name = nft.get("creator")
#         if artist_name in freq_dict:
#             freq_dict[artist_name] += 1
#         else:
#             freq_dict[artist_name] = 1
    
#     popular = [artist for artist, count in freq_dict.items() if count > 1]

#     return popular

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))


# #problem 4 - ---
# #time complexity = O(n)
# #space compleixty = O(n) because of the input_list
# def average_nft_value(nft_collection):
#     total = 0
#     count = 0
#     if len(nft_collection) == 0:
#         return total

#     for nft in nft_collection:
#         count += 1
#         total += nft.get("value")
    
#     return total/count

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))


#problem 5 --

def search_nft_by_tag(nft_collections, tag):
    names = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft.get("tags",[]):
                names.append(nft.get("name"))

    return names

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))


#problem 6

#problem 7

def validate_nft_actions(actions):
    stack = []

    for action in actions:
        if not stack:
            stack.append(action)
        else:
            if action == 'remove' and stack[-1] == "add":
                stack.pop()
            else:
                stack.append(action)
    return len(stack) == 0

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))