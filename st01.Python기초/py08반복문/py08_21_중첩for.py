# 중첩 for문

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********


# A
for x in range(1, 11, 1):
    print("**********")

print("------------------------------------")

for x in range(1, 11, 1):
    for y in range(1, 11, 1):
        print("*", end="")
    print("")


print("------------------------------------")

# B
# y==1 x== 1부터 1까지 ,
# y == 2  x==1부터 2까지
for y in range(1, 11, 1):
    for x in range(1, 11, y+1):
        print("*",  end="")
    print("")


print("------------------------------------")

# c

for y in range(1, 11, 1):
    for x in range(y+1, 11, 1):
        print ("*", end="")
    print("")


