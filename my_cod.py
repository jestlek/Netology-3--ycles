# Exercise1
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
	boys.sort()
	girls.sort()
	happy_couples = zip(boys, girls)
	print('Идеальные пары:')
	for couple in happy_couples:
		print(' и '.join(couple))
else:
	print('Количество человек в списках не совпадает. Кто-то может остаться без пары!')

# Exercise2
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]
person = 5
# for dish, ingrs in cook_book:
# 	print(f'{dish[0].upper()}{dish[1:]}:')
# 	for ing in ingrs:
# 		print(f'{ing[0]}, {ing[1] * person}{ing[2]}')
# 	print()
for dish, ingrs in cook_book:
  res = f'{dish.capitalize()}:\n' + '\n'.join(f'{name}, {q * person} {measure}' for name, q, measure in ingrs)   
  print(res)
  print()
