# Ronand Joy 71210774
# Soal 2

kalimat  = input("Masukkan sebuah kata/kalimat: ")
karakter = input("Masukkan karakter yang ingin disisipkan: ")

def case1(kalimat,karakter):
    answer = ""
    for i in kalimat.upper():
        answer += i + " " + karakter + " "
    return answer
    
def case2(kalimat,karakter):
    answer = kalimat.replace(" ", " " + karakter + " ")
    return answer
    
        
print (case1(kalimat,karakter))
print (case2(kalimat,karakter))