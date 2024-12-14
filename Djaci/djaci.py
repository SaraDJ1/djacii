najbolji=1.0
najgori=5.0
broj_djaka=int(input("Unesite broj djaka"))
for i in range(broj_djaka):
    zbir_ocena=0
    for i in range(5):
        ocena=int(input("Unesite ocenu djaka"))
        zbir_ocena=zbir_ocena + ocena
        
    prosek = zbir_ocena / 5
    if(prosek>najbolji):
        najbolji=prosek
    if(prosek<najgori):
        najgori=prosek

print("Najbolji prosek djaka je:",najbolji)
print("Najgori prosek djaka je:",najgori)
        