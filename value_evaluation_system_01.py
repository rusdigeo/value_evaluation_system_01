"""
Project  1 hari ke 4 (Value Evaluation System)
"""
#Rusdianto, S.Pd.

print("Hai, Selamat datang di sistem evaluasi")
print("Program ini membantu untuk mengecek nilai sekor siswa anda")
print("Tolong beri saya nominal angka dan saya akan menghitungnya")

name = input("Nama siswa anda? ")
grade = input("Nilai siswa anda? ")
subject = input("Subjek siswa anda? ")
score = input("Tolong beri saya Sekor? ")
score2 = input("Tolong beri saya Sekor? ")
total = (int(score)+int(score2))/2

print("\n")
print("Nama siswa: "+name)
print("Nilai: "+grade)
print("Sekor 1: "+score)
print("Score 2: "+score2)
print(score+"+"+score2+"="+str(total))

print("\n")
if total > 90:
    print("memperoleh nilai A. Kerja bagus")
elif total >=80:
    print("memperoleh nilai B. Bagus")
elif total >=70:
    print("memperoleh nilai C. Aku tau kamu bisa lebih baik lagi")
elif total >=60:
    print("memperoleh D. Coba tingkatka lebih baik lagi")
else:
    print("memperoleh D. belajar lebih giat lagi")



