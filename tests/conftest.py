import pytest
from brownie import *

from scripts.abis import *


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass


@pytest.fixture(scope="module")
def owner():
    yield accounts[-1]


@pytest.fixture(scope="module")
def rm(owner):
    yield Contract.from_abi("RM", "0xce761D788DF608BD21bdd59d6f4B54b2e27F25Bb", abi=rm_abi, owner=owner)


@pytest.fixture(scope="module")
def gold(owner):
    yield Contract.from_abi("Gold", "0x2069B76Afe6b734Fb65D1d099E7ec64ee9CC76B2", abi=gold_abi, owner=owner)


@pytest.fixture(scope="module")
def cellar(owner):
    yield Contract.from_abi("Cellar", "0x2A0F1cB17680161cF255348dDFDeE94ea8Ca196A", abi=cellar_abi, owner=owner)


@pytest.fixture(scope="module")
def attr(owner):
    yield Contract.from_abi("Attr", "0xB5F5AF1087A8DA62A23b08C00C6ec9af21F397a1", abi=attr_abi, owner=owner)


@pytest.fixture(scope="module")
def daily(owner):
    yield owner.deploy(rarity_daily)


@pytest.fixture(scope="module")
def summoners(owner, rm):
    """ Level 1 """
    summoners = []
    for _ in range(3):
        tx = rm.summon(1, {'from': owner})
        summoners.append(tx.events['summoned']['summoner'])

    yield summoners


@pytest.fixture(scope="module")
def summoners2(owner, rm):
    """ Level 2 """
    summoners = []
    for _ in range(3):
        tx = rm.summon(1, {'from': owner})
        summoners.append(tx.events['summoned']['summoner'])

    # adventure 4 times
    for _ in range(4):
        for s in summoners:
            rm.adventure(s)
        chain.sleep(60 * 60 * 25)
        chain.mine()

    yield summoners


@pytest.fixture(scope="module")
def lib():
    yield rarity_library.deploy({'from': accounts[0]})
