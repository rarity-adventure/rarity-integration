import brownie
from brownie import Wei
from brownie.network.account import PublicKeyAccount


def test_tips(rm, daily, owner, accounts, summoners):
    TIP = Wei("1 ether")
    accounts[0].transfer(owner, TIP)
    assert owner.balance() >= TIP

    donation_address = PublicKeyAccount("0x5eC86d4d826bF3e12Ee2486B9dF01d7CFa99B6Ca")
    initial_donation = donation_address.balance()
    initial_daily = daily.balance()
    assert initial_daily == 0

    daily.transfer_tips({'from': owner})
    assert initial_donation == donation_address.balance()

    rm.setApprovalForAll(daily, True, {'from': owner})
    daily.adventure(summoners, {'from': owner, 'value': TIP})

    assert initial_daily + TIP == daily.balance()
    assert initial_donation == donation_address.balance()

    daily.transfer_tips()

    assert initial_daily == daily.balance()
    assert initial_donation + TIP == donation_address.balance()
    print("TIP:", (donation_address.balance() - initial_donation).to("ether"), "FTM")

