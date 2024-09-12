from bokeh.plotting import figure, show
import random

if __name__ == "__main__":
    #preparing the data
    x = list(range(0,10))
    y1= random.sample(range(-10, 20), 10)

    # creating the plot
    p = figure(
        title="Custom axes example",
        sizing_mode="stretch_width",
        max_width = 720,
        height = 480
    )

    # adding a renderer
    p.vbar(
        x = x,
        top = y1,
        legend_label="BGE",
        color="navy",
        line_width=4,
        width=0.4,
        bottom = 10,
        fill_alpha=0.64
    )

    # changing things from x-axis
    p.xaxis.axis_label = "Temp"
    p.xaxis.axis_line_width = 3
    p.xaxis.axis_line_color = "red"

    # change some things about the y-axis
    p.yaxis.axis_label = "Volume"
    p.yaxis.major_label_text_color = "blue"
    p.yaxis.major_label_orientation = "parallel"

    # changing both axes
    p.axis.minor_tick_in = -10
    p.axis.minor_tick_out = 10

    # showing the results
    show(p)