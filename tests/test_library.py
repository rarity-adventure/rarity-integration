s1 = 466576
s2 = 466591
s3 = 555555


def test_names(lib):
    assert lib.name(s1) == "Conan"
    assert lib.description(s1) == "Conan, Level 2 Barbarian"


def test_scores(lib):
    assert lib.ability_scores(s1) == (18, 14, 14, 10, 10, 8)
    assert lib.ability_scores_full(s1) == ((18, 14, 14, 10, 10, 8), (4, 2, 2, 0, 0, -1), 32, 32, True)
    assert lib.ability_modifiers(s1) == (4, 2, 2, 0, 0, -1)


def test_core(lib):
    core = lib.base(s1)
    assert core[0] == "Conan"
    assert core[3] == 1
    assert core[4] == 2


def test_gold(lib):
    assert lib.gold(s1) == (0, 1000e18, 0)


def test_materials(lib):
    mats = lib.materials(s1)
    assert len(mats) == 1
    assert mats[0][1] == 8


def test_skills(lib):
    skills = lib.skills(1947680)
    assert sum(skills[0]) == 4
    assert sum(skills[1]) == 6
    assert skills[2:] == (32, 4)


def test_full(lib):
    lib.summoner_full(s1)
    lib.summoners_full([s1, s2])


def test_items(lib, owner):
    items = lib.items1(owner)
    assert items[0] == (2, 12, 1631467054, 466789)


# def test_daycare(lib):
#     misc = lib.misc(2454502)
#     assert misc[0] == 2


def test_print_full(lib):
    print(lib.summoner_full(2454502))


def test_not_owned_and_created(lib):
    lib.base(s3)
    lib.name(s3)
    lib.description(s3)
    lib.ability_scores(s3)
    lib.ability_modifiers(s3)
    lib.ability_scores_full(s3)
    lib.skills(s3)
    lib.gold(s3)
    lib.materials(s3)
    lib.summoner_full(s3)
    lib.summoners_full([s3, 555556]*5)



