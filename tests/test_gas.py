# import pytest
#
#
# @pytest.mark.parametrize('amount', [1, 2, 3, 10, 50, 100])
# def test_cellar_gas(rm, daily, attr, cellar, owner, amount):
#     summoners = []
#     for _ in range(amount):
#         tx = rm.summon(1, {'from': owner})
#         s = tx.events['summoned']['summoner']
#         attr.point_buy(s, 22, 8, 8, 8, 8, 8)
#         summoners.append(s)
#
#     rm.setApprovalForAll(daily, True)
#     tx = daily.cellar(summoners, summoners)
#     print(f"{amount} summoners: {tx.gas_used} gas. {tx.gas_used // amount} per summoner.")