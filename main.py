import random
Aqshy = {
        'element'  : 'fire',
        'magic'    : 'fireball',
        'feature'  : "burning lands",
        'artefact' : 'rageblade',
        'command'  : "blazing fervour",
}
Chamon = {
        'element'  :'metal',
        'magic'    :"metamorphic warding",
        'feature'  :"transmutative lands",
        'artefact' :"plate of PP",
        'command'  :"living blades",
}
Ghur = {
        'element'  :'beasts',
        'magic'    :'wildform',
        'feature'  :"savage lands",
        'artefact' :"predatos's torc",
        'command'  :"feral roar",
}
Ghyran = {
        'element'  :'life',
        'magic'    :'shield',
        'feature'  :"verdant lands",
        'artefact' :"everspring diadem",
        'command'  :"command the land",
}
Hysh = {
        'element'  :'lights',
        'magic'    :"puriti of defens",
        'feature'  :"dazzling lands",
        'artefact' :"suari trueblade",
        'command'  :'enlightenment',
}
Shyish = {
        'element'  :'death',
        'magic'    :'necroqueke',
        'feature'  :"terminal lands",
        'artefact' :"re-rell save of 1 for attacks",
        'command'  :"amethast aura",
}
Ulgu = {
        'element'  :'shadow',
        'magic'    :'judgement',
        'feature'  :"penumbral lands",
        'artefact' :"re-rell wound of 1 for melee weapon attacks",
        'command'  :"om me!",
}
worlds_list = [
        'Aqshy',
        'Chamon',
        'Ghur',
        'Ghyran',
        'Hysh',
        'Shyish',
        'Ulgu'
]
world = random.choice(list(worlds_list))
print("Выборан случайного мира из списка - ", world)
if world == 'Aqshy':
        print(Aqshy)
elif world == 'Chamon':
        print(Chamon)
elif world == 'Ghur':
        print(Ghur)
elif world == 'Ghyran':
        print(Ghyran)
elif world == 'Hysh':
        print(Hysh)
elif world == 'Shyish':
        print(Shyish)
elif world == 'Ulgu':
        print(Ulgu)
else:
        print('errorishka')
