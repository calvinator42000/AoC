import sys
def solve(data):
    data_list = data.split('\n')
    #boss = Character("Boss", int(data_list[0].split(' ')[2]), int(data_list[1].split(' ')[1]), 0, 0)
    #player = Character("Player", 50, 0, 0, 500)
    ## Spell = (id, mana_cost, damage, hp, armor, mana, duration)
    m = (0, 53, 4, 0, 0, 0, 1)
    d = (1, 73, 2, 2, 0, 0, 1)
    s = (2, 113, 0, 0, 7, 0, 6)
    p = (3, 173, 3, 0, 0, 0, 6)
    r = (4, 229, 0, 0, 0, 101, 5)
    spell_list = [m, d, s, p, r]
    #least_mana_used = simulateTurn(10, 250, 0, 13, 8, [], spell_list, True, 0, sys.maxsize)
    boss_hp = int(data_list[0].split(' ')[2])
    boss_damage = int(data_list[1].split(' ')[1])
    least_mana_used = simulateTurn(50, 500, 0, boss_hp, boss_damage, [], spell_list, True, 0, sys.maxsize)

    return least_mana_used

def simulateTurn(player_hp, player_mana, player_armor, boss_hp, boss_damage, active_spell_list, spell_list, player_turn, mana_used, least_mana_used):
    new_active_spell_list = []
    for active_spell in active_spell_list:
        boss_hp -= active_spell[2]
        player_hp += active_spell[3]
        player_armor += active_spell[4]
        player_mana += active_spell[5]
        if active_spell[6]-1 > 0:
            new_active_spell = (active_spell[0], active_spell[1], active_spell[2], active_spell[3], active_spell[4], active_spell[5], active_spell[6]-1)
            new_active_spell_list.append(new_active_spell)
    if boss_hp <= 0:
        return min(mana_used, least_mana_used)

    if player_turn:
        if player_mana < 53:
            return least_mana_used
        for spell in spell_list:
            if spell[1] <= player_mana:
                spell_valid = True
                for active_spell in new_active_spell_list:
                    if spell[0] == active_spell[0]:
                        spell_valid = False
                if spell_valid:
                    new_mana_used = mana_used + spell[1]
                    if new_mana_used <= least_mana_used:
                        least_mana_used = simulateTurn(player_hp, player_mana - spell[1], 0, boss_hp, boss_damage, new_active_spell_list + [spell], spell_list, False, new_mana_used, least_mana_used)
    else:
        total_damage = max(1, (boss_damage - player_armor))
        player_hp -= total_damage
        if player_hp <= 0:
            return least_mana_used
        least_mana_used = simulateTurn(player_hp, player_mana, 0, boss_hp, boss_damage, new_active_spell_list, spell_list, True, mana_used, least_mana_used)
    return least_mana_used

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
