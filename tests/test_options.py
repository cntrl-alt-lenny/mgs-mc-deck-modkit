"""Dialog cancellation semantics — the options-screen bug fix."""
from __future__ import annotations

import builtins

import install

ITEMS = [
    ("hq_movies", "High-quality cinematics", True),
    ("skip_splash", "Skip logos", True),
    ("update_check", "Update checks", False),
]


def _term_ui(monkeypatch, answer: str):
    ui = install.UI()
    ui.kind = "term"
    monkeypatch.setattr(builtins, "input", lambda *a, **k: answer)
    return ui


def test_cancel_returns_none(monkeypatch):
    ui = _term_ui(monkeypatch, "c")
    assert ui.checklist("t", "x", ITEMS) is None


def test_blank_keeps_defaults(monkeypatch):
    ui = _term_ui(monkeypatch, "")
    result = ui.checklist("t", "x", ITEMS)
    assert set(result) == {"hq_movies", "skip_splash"}


def test_toggle_off_yields_empty_not_none(monkeypatch):
    # Toggle both defaults off -> a *deliberate* empty selection, not a cancel.
    ui = _term_ui(monkeypatch, "0 1")
    result = ui.checklist("t", "x", ITEMS)
    assert result == []
    assert result is not None


def test_cancel_preserves_opts_defaults(monkeypatch):
    """Regression: a cancelled extras dialog must NOT flip every option off."""
    opts = {"hq_movies": True, "skip_splash": True, "update_check": False,
            "skip_launcher": True}
    ui = _term_ui(monkeypatch, "c")
    extras = ui.checklist("t", "x", ITEMS)
    if extras is not None:                       # this branch must not run
        for tag, _, _ in ITEMS:
            opts[tag] = tag in extras
    assert opts["hq_movies"] is True
    assert opts["skip_launcher"] is True
