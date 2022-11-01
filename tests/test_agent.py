import pytest
import sparc.client


def test_alive():
    agent = Agent()
    assert agent.alive()


def test_version():
    assert sparc.client.__version__ is not None
