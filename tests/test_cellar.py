import brownie


def test_cellar(rm, daily, attr, cellar, owner, summoners):
    for s in summoners:
        assert cellar.balanceOf(s) == 0
        assert sum(attr.ability_scores(s)) == 0
        assert not attr.character_created(s)
        attr.point_buy(s, 22, 8, 8, 8, 8, 8)
        assert attr.ability_scores(s) == (22, 8, 8, 8, 8, 8)
        assert attr.character_created(s)

    rm.setApprovalForAll(daily, True)

    with brownie.reverts():
        daily.cellar(summoners, [])

    is_approved = daily.is_approved(summoners)
    need_approval = [s for s, approved in zip(summoners, is_approved) if not approved]

    tx = daily.cellar(summoners, need_approval)
    gas1 = tx.gas_used

    mat_balance = [cellar.balanceOf(s) for s in summoners]
    for s in summoners:
        assert cellar.balanceOf(s) > 0

    # Test for second day
    brownie.chain.sleep(60 * 60 * 25)
    brownie.chain.mine()

    is_approved = daily.is_approved(summoners)
    need_approval = [s for s, approved in zip(summoners, is_approved) if not approved]
    assert need_approval == []

    tx = daily.cellar(summoners, [])
    gas2 = tx.gas_used

    for b, s in zip(mat_balance, summoners):
        assert cellar.balanceOf(s) > b

    assert gas1 > gas2
    print(gas1, gas2)




