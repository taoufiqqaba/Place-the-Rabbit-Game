import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Place the Rabbit Game! ")
field =  [["🌿", "🌿", "🌿" ], ["🌿", "🌿", "🌿" ], ["🌿", "🌿", "🌿" ]]
print(f"{field[0]} \n{field[1]} \n{field[2]}" )

print("Where Should the Rabbit Go? 🐇")
position = (input("Please Choose a Row and a Colomn: "))

row = int(position[0])
colomn = int(position[1])

field[row -1][colomn-1] = "🐇"
print("Success...\n ")

print(f"{field[0]} \n{field[1]} \n{field[2]} ")