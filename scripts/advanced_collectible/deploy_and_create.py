from brownie import AdvancedCollectible, network, config
from scripts.common import get_account, get_contract, fund_with_link, OPENSEA_URL


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    fund_with_link(advanced_collectible.address)
    create_collectible_tx = advanced_collectible.createCollectible({"from": account})
    create_collectible_tx.wait(1)
    print("New NFT Collectible created.")
    return advanced_collectible, create_collectible_tx


def main():
    deploy_and_create()
