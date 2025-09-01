import plotly.graph_objects as go
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Section


class LuQYSpectrumPlot(PlotSection):
    m_def = Section(label='LuQY Spectrum')

    def get_plot(self):
        result = self.m_parent
        x_nm = getattr(result, 'wavelength', None)
        y = getattr(result, 'luminescence_flux_density', None)
        if x_nm is None or y is None:
            return None
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
        return PlotlyFigure(fig=fig)
