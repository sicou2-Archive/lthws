# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Texas': 'TX',
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'OR': 'Salem',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['TX'] = 'San Antonio'

# Print out some cities
print('-' *10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Print some states
print('-' * 10)
print("Texas's abbreviation is: ", states['Texas'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using the state then cities dict
print('-' * 10)
print("Texas has:", cities[states['Texas']])
print("Florida has:", cities[states['Florida']])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    # It looks like .items() is what allows for 'state, abbrev' to work
    # here
    
# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
# Safely get a abbreviation by state that might not be there
state = states.get('Michigan')

if not state:
    print("Sorry, no Michigan.")
    
# Get a city with a default value
city = cities.get('MI', 'Does Not Exist')
print(f"The city for the state 'MI' is : {city}")