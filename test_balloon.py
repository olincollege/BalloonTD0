"""
Tests for balloon.py module.

This module contains unit tests for balloon classes:
    * Basic balloon attributes
    * Movement mechanics
    * Damage and popping behavior
    * Child balloon spawning
    * Balloon tier relationships
"""

import pytest
import pygame
from balloon import (
    RedBalloon,
    BlueBalloon,
    GreenBalloon,
    MoabBalloon,
    balloon_tiers,
)


@pytest.fixture(scope="module", autouse=True)
def pygame_setup():
    """
    Initialize and tear down Pygame once for all tests in the module.
    """
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()


@pytest.fixture
def waypoints():
    """
    Return a simple horizontal path for balloon movement.
    """
    return [(0, 0), (10, 0), (20, 0), (30, 0)]


def test_red_balloon_basic(waypoints):
    """Tests RedBalloon initialization and attributes.

    Args:
        waypoints: A fixture providing a simple horizontal path.

    Tests:
        Verifies basic balloon properties:
            * Correct type identifier
            * Health value
            * Reward amount
            * Damage value
            * Color tuple
    """
    b = RedBalloon(waypoints)
    assert b.type == "red"
    assert b.health == 1
    assert b.reward == 3
    assert b.damage == 1
    assert b.color == (255, 0, 0)


def test_balloon_movement(waypoints):
    """
    Ensure that a balloon eventually reaches the end of the path when moved repeatedly.

    Asserts:
        - At least one call to b.move() returns True (meaning it reached the end)
    """
    b = BlueBalloon(waypoints)
    reached_end = False
    for _ in range(10):
        if b.move():
            reached_end = True
            break
    assert reached_end


def test_balloon_downgrade(waypoints):
    """
    Verify that damaging a BlueBalloon spawns a RedBalloon as its child.

    Asserts:
        - One child is returned
        - The child is an instance of RedBalloon
    """
    b = BlueBalloon(waypoints)
    children = b.take_damage(1)
    assert len(children) == 1
    assert isinstance(children[0], RedBalloon)


def test_balloon_pops_fully(waypoints):
    """
    Confirm that a RedBalloon with 1 health pops completely when taking 1 damage.

    Asserts:
        - No children are returned (empty list)
    """
    b = RedBalloon(waypoints)
    result = b.take_damage(1)
    assert result == []


def test_moab_spawns_children(waypoints):
    """
    Ensure that destroying a MOAB spawns 40 GreenBalloons with specific attributes.

    Asserts:
        - 40 children are returned
        - Each child is an instance of GreenBalloon
        - Each child has 'offset' and 'skip_frames' attributes
    """
    moab = MoabBalloon(waypoints)
    children = moab.take_damage(999)
    assert len(children) == 40
    for child in children:
        assert isinstance(child, GreenBalloon)
        assert hasattr(child, "offset")
        assert hasattr(child, "skip_frames")


def test_balloon_tiers_names():
    """
    Validate that the balloon_tiers list has the correct tier names in order.

    Asserts:
        - Names extracted from balloon_tiers match:
          ["red", "blue", "green", "yellow", "pink", "moab"]
    """
    names = [name for name, _ in balloon_tiers]
    assert names == ["red", "blue", "green", "yellow", "pink", "moab"]
