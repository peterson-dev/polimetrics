from django.shortcuts import render, get_object_or_404, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap
from core.models import Candidate

# Create your views here.

def index(request):
    candidates = ['Bernie Sanders', 'Joe Biden', 'Elizabeth Warren']
    counts = [.3, .4, .2]

    data = { 'candidates' : candidates }

    source = ColumnDataSource(data=dict(candidates=candidates, counts=counts))

    plot = figure(x_range=FactorRange(*candidates), plot_height=500, title="Average Sentiment to Date", toolbar_location=None, tools="")

    plot.vbar(x='candidates', top='counts', width=0.5, source=source, line_color="white", fill_color=factor_cmap('candidates', palette=Spectral6, factors=candidates))

    plot.y_range.start = -1
    plot.y_range.end = 1
    plot.x_range.range_padding = 0.1
    plot.xaxis.major_label_orientation = 1
    plot.xgrid.grid_line_color = None

    script, div = components(plot)
    return render_to_response( "index.html", {'script' : script, 'div' : div} )

# def index(request):
#     candidates = ['Bernie Sanders', 'Joe Biden', 'Elizabeth Warren']
#     counts = [.3, .4, .2]

#     data = { 'candidates' : candidates }

#     source = ColumnDataSource(data=dict(candidates=candidates, counts=counts))

#     plot = figure(x_range=FactorRange(*candidates), plot_height=250, title="Average Sentiment to Date", toolbar_location=None, tools="")

#     plot.vbar(x='candidates', top='counts', width=0.9, source=source, line_color="white", fill_color=factor_cmap('candidates', palette=Spectral6, factors=candidates))

#     plot.y_range.start = 0
#     plot.x_range.range_padding = 0.1
#     plot.xaxis.major_label_orientation = 1
#     plot.xgrid.grid_line_color = None

#     script, div = components(plot)
#     return render_to_response( "index.html", {'script' : script, 'div' : div} )


# def candidates(request, slug):
#     candidate = get_object_or_404(Candidate, slug=slug)
#     return render(request, "candidates.html")

def candidates(request):
    return render(request, "candidates.html")

def tags(request):
    return render(request, "tags.html")


def about(request):
    return render(request, "about.html")
