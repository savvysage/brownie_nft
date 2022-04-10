from brownie import AdvancedCollectible, network
from scripts.common import get_breed, get_account, OPENSEA_URL

breed_to_token_uri = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} collectibles!")
    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting token uri of {token_id}")
            set_token_uri(advanced_collectible, token_id, breed_to_token_uri[breed])


def set_token_uri(contract, token_id, token_uri):
    account = get_account()
    tx = contract.setTokenURI(token_id, token_uri, {"from": account})
    tx.wait(1)
    print("Token URI has been set.")
    print(f"You can view NFT @ {OPENSEA_URL.format(contract.address, token_id)}")
    print("Pleae wait up to 20mins then hit the refresh metadata button.")
