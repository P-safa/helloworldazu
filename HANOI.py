def TowerHanoi(s_tower, d_tower, h_tower , n):
    if n == 1:
        print("Move rock 1 from rod", s_tower, "to rod", d_tower) # shart baraye kamtarin meghdar ke 1 hast
        return
    TowerHanoi(n - 1, s_tower, h_tower, d_tower)
    print("Move rod", n, "from rod", s_tower, "to rod", d_tower)
    TowerHanoi(n - 1, h_tower, d_tower, s_tower)

n = int(input("please provide the number of rocks: ")) # vorodi az user
TowerHanoi(n, 'A', 'C', 'B') # ba meghdari komak az doostan neveshtam