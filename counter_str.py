print("Введите последовательность букв")
string=input()
f={}
for i in string:
    f[i]=f.get(i,0)+1
print(f)