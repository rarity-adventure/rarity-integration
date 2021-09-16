import brownie


def test_adventure(rm, daily, owner, summoners):
    assert len(summoners) == 3
    for s in summoners:
        assert rm.xp(s) == 0

    with brownie.reverts():
        daily.adventure(summoners)

    rm.setApprovalForAll(daily, True)
    tx = daily.adventure(summoners)
    print(tx.gas_used)

    for s in summoners:
        assert rm.xp(s) == 250e18


