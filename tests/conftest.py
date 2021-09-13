import pytest
from brownie import *


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass


@pytest.fixture(scope="module")
def owner():
    yield accounts[-1]


@pytest.fixture(scope="module")
def lib():
    yield rarity_library.deploy({'from': accounts[0]})
