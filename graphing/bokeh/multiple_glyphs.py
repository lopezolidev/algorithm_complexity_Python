from bokeh.plotting import figure, show
import random

if __name__ == "__main__":
    # setting up the data
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y1 = []
    for i in range(10):
        y1.append(random.randint(0,10))

    y2 = []
    for i in range(10):
        y2.append(random.randint(0,10))
    
    y3 = []
    for i in range(10):
        y3.append(random.randint(0,10))

    # creating the plot with a title, x and y axis labels 
    plot = figure(title="multiple glyphs figure", x_axis_label="x", y_axis_label="y")

    # instantiating multiple renderers
    plot.line(x, y1, legend_label="pressure", color="blue", line_width=2)
    # simple line plot

    plot.vbar(x=x, top=y2, legend_label="temp", color="firebrick", line_width=2, width=0.4, bottom=0, fill_alpha=0.5)
    # vertical bar plotting

    circles = plot.scatter(x, y3, legend_label="objects", line_color="blue", fill_color="purple", fill_alpha=0.72, size=40)
    # circles plotting assigning to a variable

    glyph = circles.glyph # 'glyph' is an attribute, which we can customize the properties of this render
    glyph.fill_color = "lightblue"

    # showing the result
    show(plot)


