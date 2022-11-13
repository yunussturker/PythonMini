import random
import datetime

def getBirth(numOfBirth):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    
    for i in range(numOfBirth):
        startOfYear= datetime.date(2000,1,1)

        randNumOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randNumOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a+1:]):
                if birthdayA == birthdayB:
                    return birthdayA

Months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 
'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('>>> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break
print()

print('Here are', numBdays, 'birthdays:')
birthdays = getBirth(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')

    monthName = Months[birthday.month-1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = Months[match.month-1]
    dateText = f'{monthName} {match.day}'
    print('Multiple people have a birthday on', dateText)
else:
    print('There are no matching birthdays.')
print()

print('Generating', numBdays, 'random birthdays 100.000 times.')
input('Press Enter to begin..')

print("Let's run another 100.000 simulations.")
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulation run.')
    birthdays = getBirth(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100.000 simulations run.")

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')