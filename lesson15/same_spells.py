def same_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells & harry_spells

Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}
print(same_spells(Ron, Harry))



def unique_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.symmetric_difference(harry_spells)

print(unique_spells(Ron, Harry))



def add_new_spell(spells_list: set, new_spell: str) -> bool:
    b01 = new_spell not in spells_list
    print(b01)
    if b01 == True:
         spells_list.add(new_spell)
    return spells_list

print(add_new_spell(Ron, "Expelliarmus"))



