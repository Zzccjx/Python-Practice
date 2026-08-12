print("BREAK STATEMENT")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\nCONTINUE STATEMENT")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nPASS STATEMENT")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
