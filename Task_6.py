start_dist = float(input("Enter start distance: "))
tar_dist = float(input("Enter target distance: "))

cur_dist = start_dist
day = 1
print(f"Day {day}: {cur_dist:.2f}")

while cur_dist < tar_dist:
    day = day + 1
    cur_dist = cur_dist * 1.1
    print(f"Day {day}: {cur_dist:.2f}")

print(f"In {day} days sportsman will get target {tar_dist:.2f} distance")
