from brownie import AdvancedCollectible
from scripts.common import get_account, fund_with_link


def create_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    create_collectible_tx = advanced_collectible.createCollectible({"from": account})
    create_collectible_tx.wait(1)
    print("New NFT Collectible created.")
    return create_collectible_tx


def main():
    create_collectible()
