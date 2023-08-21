import matplotlib.pyplot as plt

current_balance = 33000
max_balance = 12000

used_percentage = (current_balance / max_balance) * 100
remaining_percentage = 100 - used_percentage

# Розрахунок перевищення витрат
if current_balance > max_balance:
    exceeded_amount = current_balance - max_balance
else:
    exceeded_amount = 0

sizes = [used_percentage, remaining_percentage]
colors = ['lightcoral', 'lightskyblue']


labels = ['Використано', 'Залишилося'] if exceeded_amount <= 0 else ['Використано', f'Залишилося\nПеревищено на {exceeded_amount}']

plt.pie(sizes, labels=labels, colors=colors, autopct='%.1f%%', startangle=90,
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'})

plt.axis('equal')
plt.show()
