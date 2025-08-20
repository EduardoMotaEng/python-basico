#Descrição física pessoal (exercício com variáveis)

name = "Eduardo"
age = 19 # Anos
height = 1.78 # Metros
weight = 70 # Quilogramas
eye_color = "dark_brown"
hair_color = "black"

#Cálculo de índice de massa corporal (IMC / BMI)
bmi = weight / (height **2)

print("=== Perfil Físico ===")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height} m")
print(f"Weight: {weight} kg")
print(f"Eye color: {eye_color}")
print(f"Hair color: {hair_color}")
print(f"BMI: {round(bmi, 2)}")
