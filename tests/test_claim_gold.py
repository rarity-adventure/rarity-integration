import brownie


def test_claim_no_approval(rm, daily, gold, owner, summoners2):
    assert len(summoners2) == 3
    for s in summoners2:
        assert gold.balanceOf(s) == 0

    with brownie.reverts():
        daily.claim_gold(summoners2, [])

    rm.setApprovalForAll(daily, True)

    with brownie.reverts():
        daily.claim_gold(summoners2, [])


def test_get_approved(rm, daily, gold, owner, summoners2):
    is_approved = daily.is_approved(summoners2)
    assert is_approved == (False, False, False)

    need_approval = [s for s, approved in zip(summoners2, is_approved) if not approved]
    assert summoners2 == need_approval

    with brownie.reverts():
        daily.approve_all(need_approval)

    rm.setApprovalForAll(daily, True)

    daily.approve_all(need_approval)

    is_approved = daily.is_approved(summoners2)
    assert is_approved == (True, True, True)

    need_approval = [s for s, approved in zip(summoners2, is_approved) if not approved]
    assert not need_approval


def test_claim(rm, daily, gold, owner, summoners2):
    rm.setApprovalForAll(daily, True)
    daily.level_up(summoners2)
    for s in summoners2:
        assert gold.balanceOf(s) == 0
        assert rm.level(s) == 2

    is_approved = daily.is_approved(summoners2)
    need_approval = [s for s, approved in zip(summoners2, is_approved) if not approved]

    with brownie.reverts():
        daily.claim_gold(summoners2, [])

    tx = daily.claim_gold(summoners2, need_approval)
    print(tx.gas_used)

    for s in summoners2:
        assert gold.balanceOf(s) == 1000e18
