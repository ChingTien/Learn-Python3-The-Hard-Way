#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'Manhattan'
cities['OR'] = 'Portland'

#print out some cities
print('BLOCK 1')
print('-'*10)
print("NY state has:", cities['NY'])
print("OR state has:", cities['OR'])

#print some states
print('BLOCK 2')
print('-'*10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

#do it by using the state then cities dict
print('BLOCK 3')
print('-'*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#print every state abbreviation
print('BLOCK 4')
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#print every city in state
print('BLOCK 5')
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('BLOCK 6')
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbrevated as {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('BLOCK 7')
print('-'*10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("sorry, no Texas")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"the city for the state 'TX' is: {city}")