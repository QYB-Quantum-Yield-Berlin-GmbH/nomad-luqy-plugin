from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Dashboard,
    Layout,
    Menu,
    MenuItemHistogram,
    MenuItemTerms,
    MenuSizeEnum,
    SearchQuantities,
    WidgetScatterPlot,
)

SCHEMA_QN = 'nomad_luqy_plugin.schema_packages.schema_package.LuQYProMeasurement'

app_entry_point = AppEntryPoint(
    name='LuQY Pro Explorer',
    description=('Browse and analyze LuQY Pro absolute PL measurements.'),
    app=App(
        label='LuQY Pro',
        path='luqypro',
        category='Measurements',
        breadcrumb='Explore LuQY Pro',
        search_quantities=SearchQuantities(
            include=[
                f'*#{SCHEMA_QN}',
                'authors.name',
                'datasets.dataset_name',
                'upload_create_time',
                'upload_user.name',
                'entry_id',
                'mainfile',
            ]
        ),
        filters_locked={'section_defs.definition_qualified_name': [SCHEMA_QN]},
        columns=[
            # Basic info
            Column(
                quantity='datasets.dataset_name',
                label='Dataset',
                selected=False,
            ),
            Column(quantity='mainfile', label='File', selected=True),
            Column(
                quantity=f'data.settings.timestamp#{SCHEMA_QN}',
                label='Timestamp',
                selected=True,
            ),
            # Results
            Column(
                quantity=f'data.results[0].luqy#{SCHEMA_QN}',
                label='LuQY (%)',
                selected=True,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.results[0].qfls#{SCHEMA_QN}',
                label='QFLS',
                unit='eV',
                selected=True,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.results[0].qfls_het#{SCHEMA_QN}',
                label='QFLS HET',
                unit='eV',
                selected=False,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.results[0].qfls_confidence#{SCHEMA_QN}',
                label='QFLS Confidence',
                selected=False,
                format={'decimals': 0, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.results[0].bandgap#{SCHEMA_QN}',
                label='Bandgap',
                unit='eV',
                selected=True,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.results[0].derived_jsc#{SCHEMA_QN}',
                label='Jsc',
                unit='mA/cm**2',
                selected=True,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            # Settings
            Column(
                quantity=f'data.settings.laser_intensity#{SCHEMA_QN}',
                label='Laser Intensity',
                unit='mW/cm**2',
                selected=False,
                format={'decimals': 2, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.bias_voltage#{SCHEMA_QN}',
                label='Bias voltage',
                unit='V',
                selected=False,
                format={'decimals': 4, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.smu_current_density#{SCHEMA_QN}',
                label='SMU current density',
                unit='mA/cm**2',
                selected=False,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.integration_time#{SCHEMA_QN}',
                label='Integration time',
                unit='ms',
                selected=False,
                format={'decimals': 0, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.delay_time#{SCHEMA_QN}',
                label='Delay time',
                unit='s',
                selected=False,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.eqe_at_laser#{SCHEMA_QN}',
                label='EQE @ laser wavelength',
                selected=False,
                format={'decimals': 2, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.laser_spot_size#{SCHEMA_QN}',
                label='Laser spot size',
                unit='cm**2',
                selected=False,
                format={'decimals': 1, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.subcell_area#{SCHEMA_QN}',
                label='Subcell area',
                unit='cm**2',
                selected=False,
                format={'decimals': 3, 'mode': 'standard'},
            ),
            Column(
                quantity=f'data.settings.subcell#{SCHEMA_QN}',
                label='Subcell',
                selected=False,
            ),
            # Metadata
            Column(quantity='authors.name', label='Author', selected=False),
            Column(quantity='entry_id', label='Entry ID', selected=False),
            Column(quantity='upload_create_time', label='Uploaded at', selected=False),
        ],
        # LEFT FILTERS
        menu=Menu(
            items=[
                # --- Basic info ---
                MenuItemTerms(
                    search_quantity='datasets.dataset_name',
                    title='Dataset',
                ),
                MenuItemTerms(
                    search_quantity='mainfile',
                    title='File',
                ),
                MenuItemHistogram(
                    x=Axis(search_quantity=f'data.settings.timestamp#{SCHEMA_QN}'),
                    title='Timestamp',
                    show_input=True,
                    nbins=30,
                ),
                # --- Results ---
                Menu(
                    title='Results',
                    size=MenuSizeEnum.MD,
                    items=[
                        MenuItemHistogram(
                            x=Axis(search_quantity=f'data.results.luqy#{SCHEMA_QN}'),
                            title='LuQY (%)',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.results.qfls#{SCHEMA_QN}',
                                unit='eV',
                            ),
                            title='QFLS',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.results.qfls_het#{SCHEMA_QN}',
                                unit='eV',
                            ),
                            title='QFLS HET',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.results.qfls_confidence#{SCHEMA_QN}'
                            ),
                            title='QFLS confidence',
                            show_input=True,
                            nbins=3,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.results.bandgap#{SCHEMA_QN}',
                                unit='eV',
                            ),
                            title='Bandgap',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.results.derived_jsc#{SCHEMA_QN}',
                                unit='mA/cm**2',
                            ),
                            title='Jsc',
                            show_input=True,
                            nbins=30,
                        ),
                    ],
                ),
                # --- Measurement settings ---
                Menu(
                    title='Measurement Settings',
                    size=MenuSizeEnum.MD,
                    items=[
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.laser_intensity#{SCHEMA_QN}',
                                unit='mW/cm**2',
                            ),
                            title='Laser intensity',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.bias_voltage#{SCHEMA_QN}',
                                unit='V',
                            ),
                            title='Bias voltage',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.smu_current_density#{SCHEMA_QN}',
                                unit='mA/cm**2',
                            ),
                            title='SMU current density',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.integration_time#{SCHEMA_QN}',
                                unit='ms',
                            ),
                            title='Integration time',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.delay_time#{SCHEMA_QN}',
                                unit='s',
                            ),
                            title='Delay time',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.eqe_at_laser#{SCHEMA_QN}',
                            ),
                            title='EQE @ laser wavelength',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.laser_spot_size#{SCHEMA_QN}',
                                unit='cm**2',
                            ),
                            title='Laser spot size',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemHistogram(
                            x=Axis(
                                search_quantity=f'data.settings.subcell_area#{SCHEMA_QN}',
                                unit='cm**2',
                            ),
                            title='Subcell area',
                            show_input=True,
                            nbins=30,
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.settings.subcell#{SCHEMA_QN}',
                            title='Subcell',
                        ),
                    ],
                ),
                # --- Metadata ---
                Menu(
                    title='Metadata',
                    size=MenuSizeEnum.MD,
                    items=[
                        MenuItemTerms(
                            search_quantity='authors.name',
                            title='Author',
                        ),
                        MenuItemTerms(
                            search_quantity='entry_id',
                            title='Entry ID',
                        ),
                        MenuItemHistogram(
                            x=Axis(search_quantity='upload_create_time'),
                            title='Uploaded at',
                            show_input=True,
                            nbins=30,
                        ),
                    ],
                ),
            ],
        ),
        dashboard=Dashboard(
            widgets=[
                # 1) Eg vs LuQY (QFLS)
                WidgetScatterPlot(
                    title='Eg vs LuQY (QFLS)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=0, y=0)},
                    x=Axis(
                        search_quantity=f'data.results[0].bandgap#{SCHEMA_QN}',
                        unit='eV',
                        title='Bandgap',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].luqy#{SCHEMA_QN}',
                        title='LuQY (%)',
                    ),
                    color=f'data.results[0].qfls#{SCHEMA_QN}',
                    size=8,
                ),
                # 2) QFLS vs Bandgap (LuQY)
                WidgetScatterPlot(
                    title='QFLS vs Eg (LuQY)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=7, y=0)},
                    x=Axis(
                        search_quantity=f'data.results[0].bandgap#{SCHEMA_QN}',
                        unit='eV',
                        title='Bandgap',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].qfls#{SCHEMA_QN}',
                        unit='eV',
                        title='QFLS',
                    ),
                    color=f'data.results[0].luqy#{SCHEMA_QN}',
                    size=8,
                ),
                # 3) LuQY (%) vs Laser intensity (t_int)
                WidgetScatterPlot(
                    title='LuQY vs Intensity (t_int)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=14, y=0)},
                    x=Axis(
                        search_quantity=f'data.settings.laser_intensity#{SCHEMA_QN}',
                        unit='mW/cm**2',
                        title='Laser',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].luqy#{SCHEMA_QN}',
                        title='LuQY (%)',
                    ),
                    color=f'data.settings.integration_time#{SCHEMA_QN}',
                    size=8,
                ),
                # 4) QFLS vs Laser intensity (LuQY)
                WidgetScatterPlot(
                    title='QFLS vs Intensity (LuQY)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=0, y=6)},
                    x=Axis(
                        search_quantity=f'data.settings.laser_intensity#{SCHEMA_QN}',
                        unit='mW/cm**2',
                        title='Laser',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].qfls#{SCHEMA_QN}',
                        unit='eV',
                        title='QFLS',
                    ),
                    color=f'data.results[0].luqy#{SCHEMA_QN}',
                    size=8,
                ),
                # 5) Jsc (derived) vs Bandgap (LuQY)
                WidgetScatterPlot(
                    title='Jsc vs Eg (LuQY)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=7, y=6)},
                    x=Axis(
                        search_quantity=f'data.results[0].bandgap#{SCHEMA_QN}',
                        unit='eV',
                        title='Bandgap',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].derived_jsc#{SCHEMA_QN}',
                        unit='mA/cm**2',
                        title='Jsc',
                    ),
                    color=f'data.results[0].luqy#{SCHEMA_QN}',
                    size=8,
                ),
                # 6) LuQY (%) vs Jsc (QFLS)
                WidgetScatterPlot(
                    title='LuQY vs Jsc (QFLS)',
                    autorange=True,
                    layout={'lg': Layout(h=6, w=7, x=14, y=6)},
                    x=Axis(
                        search_quantity=f'data.results[0].derived_jsc#{SCHEMA_QN}',
                        unit='mA/cm**2',
                        title='Jsc',
                    ),
                    y=Axis(
                        search_quantity=f'data.results[0].luqy#{SCHEMA_QN}',
                        title='LuQY (%)',
                    ),
                    color=f'data.results[0].qfls#{SCHEMA_QN}',
                    size=8,
                ),
            ]
        ),
    ),
)


"""
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus

app_entry_point = AppEntryPoint(
    name='NewApp',
    description='New app entry point configuration.',
    app=App(
        label='NewApp',
        path='app',
        category='simulation',
        columns=Columns(
            selected=['entry_id'],
            options={
                'entry_id': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
            }
        ),
    ),
)
"""
