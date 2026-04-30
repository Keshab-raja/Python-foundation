# SECTION 3: STAR PATTERNS
# ─────────────────────────────────────────────────────────
# A classic nested loop exercise — great for understanding the pattern.

rows = 5

print("\n--- Square ---")
for i in range(rows):
    for j in range(rows):
        print("★ ", end="")
    print()

print("\n--- Right triangle ---")
for i in range(1, rows + 1):
    for j in range(i):     # inner loop runs i times (grows each row)
        print("★ ", end="")
    print()

print("\n--- Pyramid ---")
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")    # leading spaces
    for j in range(2 * i - 1):        # stars per row: 1, 3, 5, 7, 9
        print("★", end="")
    print()


# ─────────────────────────────────────────────────────────
# SECTION 4: REAL USE — COMPARE EVERY PAIR IN A LIST
# ─────────────────────────────────────────────────────────
# Find all pairs of students with the same score.
students = [("Alice", 85), ("Bob", 72), ("Charlie", 85), ("Diana", 91), ("Eve", 72)]

print("\n--- Students with matching scores ---")
for i in range(len(students)):
    for j in range(i + 1, len(students)):    # j starts AFTER i (avoid repeats)
        name1, score1 = students[i]
        name2, score2 = students[j]
        if score1 == score2:
            print(f"  {name1} and {name2} both scored {score1}")