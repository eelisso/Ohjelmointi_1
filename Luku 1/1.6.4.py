benefit = float(input("Enter the amount of the study benefits: "))
index = 1.0117
index_raise = index*benefit
print(f"If the index raise is {(index-1)*100:.2f} percent, the study benefit,\n"
      f"after a raise, would be {index_raise} euros\n"
      f"and if there was another index raise, the study\n"
      f"benefits would be as much as {index*index_raise} euros")

