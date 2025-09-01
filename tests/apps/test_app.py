def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from nomad_luqy_plugin.apps import app_entry_point

    app = app_entry_point.app
    assert app.label == 'LuQY Pro'

    assert app.menu is not None
    assert len(app.menu.items) >= 2

    results_menu = next(
        (m for m in app.menu.items if getattr(m, 'title', '') == 'Results'), None
    )
    assert results_menu is not None
    from nomad.config.models.ui import MenuItemHistogram

    histos = [it for it in results_menu.items if isinstance(it, MenuItemHistogram)]
    assert any(
        h.x.search_quantity.endswith(
            '.luqy#nomad_luqy_plugin.schema_packages.schema_package.LuQYProMeasurement'
        )
        for h in histos
    )
