
st = "hello world"
print(f"st :{st}")
print("-" * 40)

print(f"st[0]  :{st[0]}")                # strings are stored like a list
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 40)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

# reverse indexing
print("-" * 40)
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 40)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

# strings are immutable
print("-" * 40)
st = "hello world"
print(f"st[6] :{st[6]}")
# st[6] = "W"
# TypeError: 'str' object does not support item assignment
"""
in oops we do have setter and getter methods
in case of immutable objects the class will not have setter methods

"""
print(dir(st))

st = "Hello World"
# reverse the string case
print(f"st :{st}")
print(f"reverse of st :{st.swapcase()}")
