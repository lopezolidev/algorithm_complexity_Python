from bokeh.plotting import figure, show
from bokeh.io import curdoc
import random

if __name__ == "__main__":
    # let's prepare the data
    x = list(range(0, 10))
    y1 = random.sample(range(0,20), 10)
    y2 = random.sample(range(0,20), 10)
    y3 = random.sample(range(0,20), 10)

    #applying the theme to current document
    curdoc().theme = "dark_minimal"

    # create the plot
    plt = figure(sizing_mode="stretch_width")

    plt2 = figure(
        title="plot sizing example",
        width=800,
        height=720,
        x_axis_label="x",
        y_axis_label="y"
    )

    plt2.width = 720
    plt2.height = 480

    plt3 = figure(
        title="Plot responsive sizing example",
        sizing_mode="stretch_width",
        height=360,
        x_axis_label = "x",
        y_axis_label = "y"
    )

    plt3.vbar(x=x, top=y3, legend_label="DFG", color="firebrick", line_width=2, width=0.4, bottom=0, fill_alpha=0.5)

    #adding the renderer
    plt.line(x, y1)
    plt2.scatter(x, y2, fill_color="red", fill_alpha=0.5, legend_label="objects", line_color="blue", size=16, )

    #showing the results, each one appears in a different page in the same window
    show(plt)
    show(plt2)
    show(plt3)