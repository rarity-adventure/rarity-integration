def test_names(lib, barb):
    assert lib.name(barb) == "Conan"
    assert lib.description(barb) == "Conan, Level 2 Barbarian"


def test_scores(lib, barb):
    assert lib.ability_scores(barb) == (18, 14, 14, 10, 10, 8)
    assert lib.ability_scores_full(barb) == ((18, 14, 14, 10, 10, 8), (4, 2, 2, 0, 0, -1), 32, 32)
    assert lib.ability_modifiers(barb) == (4, 2, 2, 0, 0, -1)


def test_core(lib, barb):
    core = lib.base(barb)
    assert core[0] == "Conan"
    assert core[3] == 1
    assert core[4] == 2


def test_gold(lib, barb):
    print(lib.gold(barb))
    assert lib.gold(barb) == (0, 1000e18, 0)


def test_materials(lib, barb):
    mats = lib.materials(barb)
    assert len(mats) == 1
    assert mats[0][1] == 8


def test_skills(lib, barb):
    skills = lib.skills(1947680)
    assert sum(skills[0]) == 4
    assert sum(skills[1]) == 6
    assert skills[2:] == (32, 4)


def test_items(lib, owner):
    items = lib.items1(owner)
    assert items[0] == (2, 12, 1631467054, 466789)

