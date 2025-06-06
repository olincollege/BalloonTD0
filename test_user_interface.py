"""
Test file for UI interactions including TowerPurchasingUI and TowerMenu.

Covers:
- Button click handling (inside and outside)
- Toggle behavior of the tower menu
"""

import pytest
import pygame
from user_interface import TowerPurchasingUI, TowerMenu


@pytest.fixture(autouse=True)
def pygame_setup_and_teardown():
    """
    Initialize and clean up the pygame environment for tests.

    Yields:
        None: Allows test code to run with pygame initialized.

    Setup:
        Calls pygame.init() to initialize all imported pygame modules.
    Teardown:
        Calls pygame.quit() to uninitialize all pygame modules and clean up.
    """
    pygame.init()
    yield
    pygame.quit()


def test_tower_purchasing_ui_handles_click_inside():
    """
    Test that clicking inside a TowerPurchasingUI button triggers its callback.

    Asserts:
        - `button.handle_event(event)` is True: the button registers the click
        - `triggered["called"] is True`: the callback is successfully invoked
    """
    triggered = {"called": False}

    def callback():
        triggered["called"] = True

    button = TowerPurchasingUI((50, 50, 100, 40), "Test", callback, 100)
    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, {"button": 1, "pos": (60, 60)}
    )

    assert button.handle_event(event)
    assert triggered["called"]


def test_tower_purchasing_ui_ignores_click_outside():
    """
    Test that clicking outside a TowerPurchasingUI button does not trigger its callback.

    Asserts:
        - `button.handle_event(event)` is False: the click is ignored
        - `triggered["called"] is False`: the callback is not invoked
    """
    triggered = {"called": False}

    def callback():
        """
        Mark the callback as invoked by updating the triggered flag.

        This function sets triggered["called"] to True in the enclosing scope,
        indicating that the callback has been executed.
        """
        triggered["called"] = True

    button = TowerPurchasingUI((50, 50, 100, 40), "Test", callback, 100)
    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, {"button": 1, "pos": (10, 10)}
    )

    assert not button.handle_event(event)
    assert not triggered["called"]


def test_tower_menu_toggle_only():
    """
    Test the toggle functionality of the TowerMenu.

    Asserts:
        - Initially, `menu.expanded is True`
        - After toggle event, `menu.expanded is False`
        - After second toggle event, `menu.expanded is True`
    """
    game_ui = object()
    menu = TowerMenu((10, 10, 100, 100), game_ui)
    menu.toggle_button_rect = pygame.Rect(10, 10, 30, 30)

    toggle_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, {"button": 1, "pos": (15, 15)}
    )

    assert menu.expanded is True
    menu.handle_event(toggle_event)
    assert menu.expanded is False
    menu.handle_event(toggle_event)
    assert menu.expanded is True
