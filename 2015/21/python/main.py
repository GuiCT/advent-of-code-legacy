from math import ceil
import itertools

PLAYER_HP = 100
BOSS_HP = 109
BOSS_DMG = 8
BOSS_ARMOR = 2

weapons_names = ["Dagger", "Shortsword", "Warhammer", "Longsword", "Greataxe"]
weapons_cost = [8, 10, 25, 40, 74]
weapons_damage = [4, 5, 6, 7, 8]
weapons = [
    {"name": name, "cost": cost, "damage": damage} for (
        name, cost, damage) in zip(weapons_names, weapons_cost, weapons_damage)]

armors_names = ["Leather", "Chainmail", "Splintmail",
                "Bandedmail", "Platemail", "None"]
armors_cost = [13, 31, 53, 75, 102, 0]
armors_armor = [1, 2, 3, 4, 5, 0]
armors = [
    {"name": name, "cost": cost, "armor": armor} for (
        name, cost, armor) in zip(armors_names, armors_cost, armors_armor)]

rings_names = [
    "Damage +1",
    "Damage +2",
    "Damage +3",
    "Defense +1",
    "Defense +2",
    "Defense +3",
    "None",
    "None",
]
rings_cost = [25, 50, 100, 20, 40, 80, 0, 0]
rings_damage = [1, 2, 3, 0, 0, 0, 0, 0]
rings_armor = [0, 0, 0, 1, 2, 3, 0, 0]
rings = [
    {"name": name, "cost": cost, "damage": damage, "armor": armor} for (
        name, cost, damage, armor) in zip(rings_names, rings_cost, rings_damage, rings_armor)]


min_gold = 1e+6  # lazy way to compare
max_gold = -1
for weapon in weapons:
    for armor in armors:
        for ring_1, ring_2 in itertools.combinations(rings, 2):
            player_dmg = (
                weapon["damage"] +
                ring_1["damage"] +
                ring_2["damage"]
            )

            player_armor = (
                armor["armor"] +
                ring_1["armor"] +
                ring_2["armor"]
            )

            player_hit_to_boss = max(1, player_dmg - BOSS_ARMOR)
            boss_hit_to_player = max(1, BOSS_DMG - player_armor)
            rounds_to_kill_player = ceil(PLAYER_HP / boss_hit_to_player)
            rounds_to_kill_boss = ceil(BOSS_HP / player_hit_to_boss)

            total_gold = (
                weapon["cost"] +
                armor["cost"] +
                ring_1["cost"] +
                ring_2["cost"]
            )
            if rounds_to_kill_player >= rounds_to_kill_boss:
                min_gold = min(min_gold, total_gold)
            else:
                max_gold = max(max_gold, total_gold)

print(f"Part 1 result is {min_gold}")
print(f"Part 2 result is {max_gold}")
