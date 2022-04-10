from brownie import network
from scripts.common import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import pytest, time


def test_can_create_advanced_collectible_2():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing.")
    # Act
    advanced_collectible, create_collectible_tx = deploy_and_create()
    request_id = create_collectible_tx.events["requestedCollectible"]["requestId"]
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.ownerOf(0) == get_account()
