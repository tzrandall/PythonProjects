hoursNeeded = int(input('How many hours do you need to work this week? '))
minutesNeeded = hoursNeeded * 60
secondsNeeded = minutesNeeded * 60

hoursHad = int(input('How many hours have you worked this week? '))
minutesHad = int(input('How many minutes have you worked this week? '))
minutesHad = minutesHad + (hoursHad * 60)
secondsHad = minutesHad * 60

timeLeft = secondsNeeded - secondsHad

secondsLeft = int(timeLeft % 60)
minutesLeft = int((timeLeft / 60) % 60)
hoursLeft = int((timeLeft / 60) / 60)

print(f'You need to work {hoursLeft} hours and {minutesLeft} minutes.')