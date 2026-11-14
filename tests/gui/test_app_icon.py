"""The application icon ships in the package and loads as a Qt icon."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("PySide6")

from PySide6.QtGui import QIcon

from opensees_studio.app import app_icon_path


def test_the_icon_assets_are_in_the_package() -> None:
    icons = app_icon_path().parent
    for name in ("app.svg", "app.ico", "app.icns", "app-256.png"):
        assert (icons / name).is_file(), name


def test_the_svg_loads_as_a_qt_icon(qtbot) -> None:  # type: ignore[no-untyped-def]
    path = app_icon_path()
    assert isinstance(path, Path)
    icon = QIcon(str(path))
    assert not icon.isNull()
    assert not icon.pixmap(64, 64).isNull()
