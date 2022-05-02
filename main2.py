import pandas


data = pandas.read_csv("Squirrel_Data.csv")


squirrel = data['Primary Fur Color']
black = squirrel[squirrel == 'Black']
red = squirrel[squirrel == 'Cinnamon']
gray = squirrel[squirrel == 'Gray']
black_n = (black.count())
red_n = (red.count())
gray_n = gray.count()
squirrel1 = {'fur colors': ['black', 'red', 'gray'],
             'count': [black_n, red_n, gray_n]

}



table = pandas.DataFrame(squirrel1)
table.to_csv('new_data')