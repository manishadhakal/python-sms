square={num: num**2 for num in range(1,11)}
print(square)

square={f"num of 1 is {num}":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k}:{v}")
#print(square)

num2={num:("even" if num%2==0 else"odd") for num in range(1,11)}
for k,v in num2.items():
    print(f"{k}:{v}")
#print(num2)