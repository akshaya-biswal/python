# break : exits the loop entirely
# continue : skips the current iteration and proceeds to the next one

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)
