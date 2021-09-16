import brownie


def test_level_up(rm, daily, owner, summoners2):
    assert len(summoners2) == 3
    for s in summoners2:
        assert rm.xp(s) == 1000e18
        assert rm.level(s) == 1

    with brownie.reverts():
        daily.level_up(summoners2)

    rm.setApprovalForAll(daily, True)
    tx = daily.level_up(summoners2)
    print(tx.gas_used)

    for s in summoners2:
        assert rm.xp(s) == 0
        assert rm.level(s) == 2


