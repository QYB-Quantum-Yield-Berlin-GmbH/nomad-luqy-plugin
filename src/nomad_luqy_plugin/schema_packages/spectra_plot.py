import plotly.graph_objects as go
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Section


class LuQYSpectrumPlot(PlotSection):
    m_def = Section(label='LuQY Spectrum', a_eln={'overview': True})

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        result = self.m_parent

        x_nm = getattr(result, 'wavelength', None)
        y = getattr(result, 'luminescence_flux_density', None)
        if x_nm is None or y is None or len(x_nm) == 0 or len(y) == 0:
            return

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x_nm,
                y=y,
                mode='lines',
                name='Spectrum',
                hovertemplate='<b>%{x:.4f}</b> nm<br>%{y:.4g}<extra></extra>',
            )
        )
        fig.update_layout(
            title='Luminescence Spectrum',
            xaxis_title='Wavelength (nm)',
            yaxis_title='Luminescence Flux Density',
            hovermode='x unified',
            uirevision='luqy-spectrum',
        )

        figure_json = fig.to_plotly_json()
        figure_json['config'] = {'displaylogo': False, 'scrollZoom': True}

        self.figures = [PlotlyFigure(label='PL spectrum', figure=figure_json)]
