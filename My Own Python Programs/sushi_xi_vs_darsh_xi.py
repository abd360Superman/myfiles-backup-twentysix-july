import random

sushixi = {'Chris Gayle' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Jos Buttler' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Virat Kohli(c)' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'AB de Villiers' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'KL Rahul(wk)' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Sanju Samson' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Rashid Khan' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Bhuvneshwar Kumar' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Mohammed Shami' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Thangarasu Natarajan' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Yuzvendra Chahal' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False}}
sushixiplayers = list(sushixi.keys())
sushixibowlers = {'Yuzvendra Chahal' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Thangarasu Natarajan' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Mohammed Shami' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Bhuvneshwar Kumar' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Rashid Khan' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Chris Gayle' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []}}
sushixibowlingplayers = list(sushixibowlers.keys())
sushixifow = []
darshxi = {'Shikhar Dhawan' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Rohit Sharma' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Suresh Raina' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Kieron Pollard' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'MS Dhoni(c)(wk)' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Andre Russell' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Ravindra Jadeja' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Harbhajan Singh' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Kagiso Rabada' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Trent Boult' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False},
           'Jasprit Bumrah' : {'runs' : 0, 'balls' : 0, 'strike-rate' : 0, 'out' : False}}
darshxiplayers = list(darshxi.keys())
darshxibowlers = {'Jasprit Bumrah' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Trent Boult' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Kagiso Rabada' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Harbhajan Singh' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Ravindra Jadeja' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []},
                  'Andre Russell' : {'balls' : 0, 'runs' : 0, 'wickets' : 0, 'bats-out' : []}}
darshxibowlingplayers = list(darshxibowlers.keys())
darshxifow = []

runs = [7, 6, 6, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

bat1 = None
bat2 = None
bowl1 = None
bowl2 = None
bat1team = None
bat2team = None
bat1players = None
bat2players = None
bowl1opts = None
bowl2opts = None
bowl1playlist = None
bowl2playlist = None
bat1fow = None
bat2fow = None

toss = random.randint(0, 1)
if toss == 0:
    bat1team = darshxi
    bat1players = darshxiplayers
    bat1fow =  darshxifow
    bowl1opts = sushixibowlers
    bowl1playlist = sushixibowlingplayers
    bat2team = sushixi
    bat2players = sushixiplayers
    bat2fow = sushixifow
    bowl2opts = darshxibowlers
    bowl2playlist = darshxibowlingplayers
    
    bat1 = 'Darsh XI'
    bowl1 = 'Sushi XI'
    bat2 = 'Sushi XI'
    bowl2 = 'Darsh XI'
else:
    bat1team = sushixi
    bat1players = sushixiplayers
    bat1fow = sushixifow
    bowl1opts = darshxibowlers
    bowl1playlist = darshxibowlingplayers
    bat2team = darshxi
    bat2players = darshxiplayers
    bat2fow = darshxifow
    bowl2opts = sushixibowlers
    bowl2playlist = sushixibowlingplayers
    
    bat1 = 'Sushi XI'
    bowl1 = 'Darsh XI'
    bat2 = 'Darsh XI'
    bowl2 = 'Sushi XI'

print('Batting First: ' + bat1)
print('Bowling First: ' + bowl1)
print('Batting Second: ' + bat2)
print('Bowling Second: ' + bowl2)

bat1runs = 0
bat1wickets = 0
strikebat = bat1players[0]
nonstrikebat = bat1players[1]
bowler = random.choice(bowl1playlist)

def overDone(n, i) :
    global bowler
    if ((n % 6) != 1) or (n == 1):
        return False
    else:
        prevBowler = bowler
        if i == 1:
            while (prevBowler == bowler) or (bowl1opts[bowler]['balls'] >= 24):
                bowler = random.choice(bowl1playlist)
        if i == 2:
            while (prevBowler == bowler) or (bowl2opts[bowler]['balls'] >= 24):
                bowler = random.choice(bowl2playlist)
        return True

for i in range(1, 121):
    if overDone(int(i), 1):
        temp = strikebat
        strikebat = nonstrikebat
        nonstrikebat = temp
    bat1team[strikebat]['balls'] += 1
    bowl1opts[bowler]['balls'] += 1
    runs_on_ball = random.choice(runs)
    if runs_on_ball == 7:
        bat1wickets += 1
        bat1team[strikebat]['out'] = True
        bowl1opts[bowler]['wickets'] += 1
        bowl1opts[bowler]['bats-out'].append(strikebat)
        bat1fow.append(str(bat1runs) + '/' + str(bat1wickets) + ': ' + strikebat)
        if bat1wickets >= 10:
            break
        strikebat = bat1players[bat1wickets+1]
    elif runs_on_ball == 1:
        bat1team[strikebat]['runs'] += 1
        bowl1opts[bowler]['runs'] += 1
        bat1runs += 1
        temp = strikebat
        strikebat = nonstrikebat
        nonstrikebat = temp
    else:
        bat1team[strikebat]['runs'] += runs_on_ball
        bowl1opts[bowler]['runs'] += runs_on_ball
        bat1runs += runs_on_ball

target = bat1runs + 1
bat2runs = 0
bat2wickets = 0
strikebat = bat2players[0]
nonstrikebat = bat2players[1]
bowler = random.choice(bowl2playlist)

for j in range(1, 121):
    if overDone(int(j), 2):
        temp = strikebat
        strikebat = nonstrikebat
        nonstrikebat = temp
    bat2team[strikebat]['balls'] += 1
    bowl2opts[bowler]['balls'] += 1
    runs_on_ball = random.choice(runs)
    if runs_on_ball == 7:
        bat2wickets += 1
        bat2team[strikebat]['out'] = True
        bowl2opts[bowler]['wickets'] += 1
        bowl2opts[bowler]['bats-out'].append(strikebat)
        bat2fow.append(str(bat2runs) + '/' + str(bat2wickets) + ': ' + strikebat)
        if bat2wickets >= 10:
            break
        strikebat = bat2players[bat2wickets+1]
    elif runs_on_ball == 1:
        bat2team[strikebat]['runs'] += 1
        bowl2opts[bowler]['runs'] += 1
        bat2runs += 1
        temp = strikebat
        strikebat = nonstrikebat
        nonstrikebat = temp
    else:
        bat2team[strikebat]['runs'] += runs_on_ball
        bowl2opts[bowler]['runs'] += runs_on_ball
        bat2runs += runs_on_ball
    if bat2runs >= target:
        break

print('First Innings')
for a in range(11):
    r = bat1team[bat1players[a]]['runs']
    b = bat1team[bat1players[a]]['balls']
    if b == 0:
        print(bat1players[a] + ': DNB')
        continue
    bat1team[bat1players[a]]['strike-rate'] = round((r / b) * 100, 2)
    sr = bat1team[bat1players[a]]['strike-rate']
    o = bat1team[bat1players[a]]['out']
    if o:
        print(bat1players[a] + ': ' + str(r) + ' in ' + str(b) + ' balls at strike rate of ' + str(sr))
    else:
        print(bat1players[a] + ': ' + str(r) + '* in ' + str(b) + ' balls at strike rate of ' + str(sr))
print('Total: ' + str(bat1runs) + '/' + str(bat1wickets))

print('Bowling: ')
for q in range(6):
    b = bowl1opts[bowl1playlist[q]]['balls']
    if b == 0:
        print(bowl1playlist[q] + ': DNB')
    r = bowl1opts[bowl1playlist[q]]['runs']
    w = bowl1opts[bowl1playlist[q]]['wickets']
    peopleOut = ', '.join(bowl1opts[bowl1playlist[q]]['bats-out'])
    if peopleOut:
        print(bowl1playlist[q] + ': ' + str(r) + '/' + str(w) + ' in ' + str(b) + ' balls and got ' + peopleOut + ' out')
    else:
        print(bowl1playlist[q] + ': Gave ' + str(r) + ' in ' + str(b) + ' and no wicket taken')
print('FOW: ' + ', '.join(bat1fow))
print('Target: ' + str(target))

print('Second Innings')
for x in range(11):
    r = bat2team[bat2players[x]]['runs']
    b = bat2team[bat2players[x]]['balls']
    if b == 0:
        print(bat2players[x] + ': DNB')
        continue
    bat2team[bat2players[x]]['strike-rate'] = round((r / b) * 100, 2)
    sr = bat2team[bat2players[x]]['strike-rate']
    o = bat2team[bat2players[x]]['out']
    if o:
        print(bat2players[x] + ': ' + str(r) + ' in ' + str(b) + ' balls at strike rate of ' + str(sr))
    else:
        print(bat2players[x] + ': ' + str(r) + '* in ' + str(b) + ' balls at strike rate of ' + str(sr))
print('Total: ' + str(bat2runs) + '/' + str(bat2wickets))

print('Bowling: ')
for z in range(6):
    b = bowl2opts[bowl2playlist[z]]['balls']
    if b == 0:
        print(bowl2playlist[z] + ': DNB')
    r = bowl2opts[bowl2playlist[z]]['runs']
    w = bowl2opts[bowl2playlist[z]]['wickets']
    peopleOut = ', '.join(bowl2opts[bowl2playlist[z]]['bats-out'])
    if peopleOut:
        print(bowl2playlist[z] + ': ' + str(r) + '/' + str(w) + ' in ' + str(b) + ' balls and got ' + peopleOut + ' out')
    else:
        print(bowl2playlist[z] + ': Gave ' + str(r) + ' in ' + str(b) + ' and no wicket taken')
print('FOW: ' + ', '.join(bat2fow))
print('GAME OVER')

winMargin = 0
if bat1runs > bat2runs:
    winMargin = bat1runs - bat2runs
    print(bat1 + ' win by ' + str(winMargin) + ' runs')
elif bat1runs < bat2runs:
    winMargin = 10 - bat2wickets
    print(bat2 + ' win by ' + str(winMargin) + ' wickets')
else:
    print('Match Draw')
