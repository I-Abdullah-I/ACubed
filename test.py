accounts = 'facebook:      abdullah@gmail.com        , twitter: @TheEternalOrion'

account = accounts.split(',')

social_array = {}

for acc in account:
    acc = acc.split(':')
    print(acc)
    social_array[acc[0].strip()] = acc[1].strip()

print(social_array)