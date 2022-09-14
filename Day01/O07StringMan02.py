
st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print("find".center(40, "-"))
print(f"st :{st}")

res = st.find("l")
print(f"res :{res}")

res = st.find("l", st.find("l") + 1)
print(f"res :{res}")

res = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"res :{res}")

print(f"st1 :{st1}")
res = st1.find("the")
print(f"res :{res}")

res = st1.find("the", st1.find("the") + 1)
print(f"res :{res}")

print("replace".center(40, "-"))
print(f"st :{st}")

res = st.replace('l', "L")
print(f"res :{res}")

res = st.replace('l', "L", 1)
print(f"res :{res}")

print(f"st1 :{st1}")
res= st1.replace("the", "The")
print(f"res :{res}")

res= st1.replace("the", "The", 1)
print(f"res :{res}")

# maketrans, translate
print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'           # length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
