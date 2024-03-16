from pulp import LpMaximize, LpProblem, LpVariable, lpSum

model = LpProblem(name="maximize-production", sense=LpMaximize)
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

model += (2 * lemonade + 1 * fruit_juice <= 100, "water_constraint") 
model += (1 * lemonade <= 50, "sugar_constraint")  
model += (1 * lemonade <= 30, "lemon_juice_constraint")  
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")  

model += lpSum([lemonade, fruit_juice])

status = model.solve()

lemonade_value = lemonade.value()
fruit_juice_value = fruit_juice.value()
total_products = lemonade_value + fruit_juice_value

print(f"Виробити лимонаду: {lemonade_value}")
print(f"Виробити фруктового соку: {fruit_juice_value}")
print(f"Загальна кількість продуктів: {total_products}")