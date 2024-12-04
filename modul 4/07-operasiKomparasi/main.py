# operasi komperasi perbasndingan

# perhatikan 
"""
  hasil dari operasi komparasi
    selalu bertipe data boolean
    (true/false)
"""
# >,<,>=,<=,==,!=,is, dan is not
  
a = 4
b = 2

#lebih dari >
print("===lebih dari(>)")
hasil = a > 3 # true
print(a, ">", 3, "+", hasil)
hasil = b > 3 # false
print(b, ">", 3, "=", hasil)
hasil = b > 2 
print(b, ">", 2, "=", hasil)
# kurang dari < 
print("===kurang dari(<)")
print(a, "<", 3, "+", hasil)
hasil = b < 3 # false
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)