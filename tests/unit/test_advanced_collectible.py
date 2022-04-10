from brownie import network
from scripts.common import (
    get_account,
    get_contract,
    NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import pytest


def test_can_create_advanced_collectible():
    # Arrange
    if network.show_active() not in NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing.")
    # Act
    advanced_collectible, create_collectible_tx = deploy_and_create()
    request_id = create_collectible_tx.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        request_id, random_number, advanced_collectible.address, {"from": get_account()}
    )
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.ownerOf(0) == get_account()
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
