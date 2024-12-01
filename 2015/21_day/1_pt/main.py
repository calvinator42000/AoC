import sys

def solve(data):
    ## (<hit_points>, <damage>, <armor>)
    boss_stats = parseData(data)
    ## (<damage>, <cost>)
    weapon_list = [(4,8),(5,10),(6,25),(7,40),(8,74)]
    ## (<armor>, <cost>)
    armor_list = [(0,0),(1,13),(2,31),(3,53),(4,75),(5,102)]
    ## (<damage>, <armor>, <cost>)
    ring_list = [(0,0,0),(0,0,0),(1,0,25),(2,0,50),(3,0,100),(0,1,20),(0,2,40),(0,3,80)]
    combination_list = generateCombinations(weapon_list, armor_list, ring_list)
    combination_list.sort(key = lambda x: x[2])
    for combination in combination_list:
        player_stats = (100, combination[0], combination[1])
        if simulateBattle(player_stats, boss_stats):
            return combination[2]
    return None

def simulateBattle(player_stats, boss_stats):
    player_hp = player_stats[0]
    boss_hp = boss_stats[0]
    player_turn = True
    while player_hp > 0 and boss_hp > 0:
        if player_turn:
            boss_hp -= max(1, player_stats[1] - boss_stats[2])
        else:
            player_hp -= max(1, boss_stats[1] - player_stats[2])
        player_turn = not player_turn
    if boss_hp <= 0:
        return True
    else:
        return False

def generateCombinations(weapon_list, armor_list, ring_list):
    combination_list = []
    for weapon_index in range(len(weapon_list)):
        for armor_index in range(len(armor_list)):
            for ring_1_index in range(len(ring_list)):
                for ring_2_index in range(len(ring_list)):
                    if ring_2_index != ring_1_index:
                        weapon = weapon_list[weapon_index]
                        armor = armor_list[armor_index]
                        ring_1 = ring_list[ring_1_index]
                        ring_2 = ring_list[ring_2_index]
                        total_cost = weapon[1] + armor[1] + ring_1[2] + ring_2[2]
                        total_damage = weapon[0] + ring_1[0] + ring_2[0]
                        total_armor = armor[0] + ring_1[1] + ring_2[1]
                        combination_list.append((total_damage, total_armor, total_cost, (weapon, armor, ring_1, ring_2)))
    return combination_list


def parseData(data):
    data_lines = data.split('\n')
    hit_points = int(data_lines[0].split(' ')[2])
    damage = int(data_lines[1].split(' ')[1])
    armor = int(data_lines[2].split(' ')[1])
    return (hit_points, damage, armor)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
