#review from peer session today

#problem 1

'''
function returns species with highest conservation priority

input: list of dictionaries
output: species name for species with lowest population
'''

# def most_endangered(species_list):
#     lowest = float("inf")
#     output_species = None
#     for species in species_list:
#         if species["population"] < lowest:
#             lowest = species["population"]
#             output_species = species
#     return output_species["name"]

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))


#problem 2 -------------------------
#identify endangered species
'''
input: endangered species in a string and observed species in string
output: # of observed species that are endangered
'''

#challenge - use a set

'''
using a set: lookup in set in O(1) time
whlie checking if something is in an iterable is O(n) time
'''

# def count_endangered_species(endangered_species, observed_species):
#     endangered = set(endangered_species)
#     count = 0
#     for species in observed_species:
#         if species in endangered:
#             count+=1
    
#     return count

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2)) 

#problem 3 ------ navigate the research station

# '''
# input: station_layout with letters, and string of observation points
# output: total time to visit observation points
# '''

# def navigate_research_station(station_layout, observations):
#     totaltime = 0
#     previous = 0

#     dict = {}
#     for idx, char in enumerate(station_layout):
#         dict[char] = idx
#     for char in observations:
#         if char in dict:
#             totaltime += abs(previous - dict[char])
#             previous = dict[char]
    
#     return totaltime

# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"

# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))


#problem 4 ----------prioritize endangered species
'''
input = two lists, one observed one priority
output = observed sorted by priority order with everything not in priority added to the end of the result in ascending order
'''
'''
PLAN - 
use a dictionary to get frequencies of different species
using if statements
> if something in priority then add to the result as much times as the count in frequencydictionary
> if not, add that to a leftover list
> combines the two lists at the end with .extend()
'''