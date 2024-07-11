# students_dict = dict()
# students_dict['X10000'] = 'Michael' # Assign the key X10000, the value Michael
# students_dict['X10002'] = 'Neil'    # Assign the key X10002, the value Neil
# students_dict['X10001'] = 'Karen'   # Assign the key X10001, the value Karen
#
# print(students_dict)

#
# callList = dict()
# callList['charlotte'] = "0903838484"
# callList['mike'] = "0903833223"
#
# print(callList['charlotte'])

# states = ['CA', 'NY', 'KY']
# population  = [39557045, 19542209, 4468402]
#
# # Your code here
# statepopulation = dict()
#
# for i in states:
#     for j in population:
#         statepopulation[i] = j
#
# print(statepopulation)
# print(f'CA:{statepopulation['CA']} ')
# print(f'NY:{statepopulation['NY']} ')
# print(f'KY:{statepopulation['KY']} ')

# Example 3

# students_dict = dict()
# students_dict['X10000'] = 'Michael'
# students_dict['X10002'] = 'Neil'
# students_dict['X10001'] = 'Karen'
#
# for student_id in students_dict.keys():
#     print(students_dict[student_id])
# # Output:
# #
# # Michael
# # Neil
# # Karen

#
# callList = dict()
# callList['charlotte'] = "0903838484"
# callList['mike'] = "0903833223"
# callList['jade'] = "0923323225"
#
#
# for number in callList.keys():
#     print(callList[number])

# callList = dict()
# callList['charlotte'] = "0903838484"
# callList['mike'] = "0903833223"
# callList['jade'] = "0923323225"
#
#
# for key,value in callList.items():
#     print(f"{key}: {value}")

#
# states_abbrev = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
#                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
#                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
#                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
#                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
#
# states_full = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
#     "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
#     "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
#     "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
#     "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
#     "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
#     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
#     "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
# ]
#
#
# states_dict = dict(zip(states_abbrev, states_full))
# alternative = states_dict.copy()
# alternative.pop('AL')
#
# # print(" ,".join(statesDict.keys()))
# print(alternative)
# print(states_dict)

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


keys_to_remove = [state.upper() for state in states if state.startswith('M')]


print(keys_to_remove)