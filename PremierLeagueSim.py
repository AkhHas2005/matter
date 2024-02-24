#Premier League Table Simulator

GAMES = 38
Points = {'Win': 3, 'Draw':1, 'Loss': 0}

print('Welcome to the official Premier League Table Simulator! ')

team = input('Enter the team you want to simulate with: ')

points = 0

for num in range(GAMES):
	coinNum = 2
	for num in range(coinNum):
		results = []
		result = input('Enter the result of the coin: ')
		results.append(result)
		if num == coinNum - 1:
			if results[0] == 'Heads' and results[1] == 'Heads':
				gameResult = 'Win'
				