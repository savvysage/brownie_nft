from brownie import network
from scripts.common import get_account, NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.simple_collectible.deploy_and_create import deploy_and_create
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing.")
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
