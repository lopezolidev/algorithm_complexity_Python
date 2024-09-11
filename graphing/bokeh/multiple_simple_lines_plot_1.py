from bokeh.plotting import figure, show

if __name__ == "__main__":
    # create a new plot with a title and axis labels
    fig = figure(title="multiple lines plot", x_axis_label="x", y_axis_label="y")
    
    # prepare some data
    x = [1, 2, 3, 4, 5]
    y1 = [2, 5, 8, 1, 0]
    y2 = [7, 7, 7, 7, 0]
    y3 = [4, 9, 1, 0, 9]

    # add multiple renderers
    fig.line(x, y1, legend_label="prices", color="green", line_width=4)
    fig.line(x, y2, legend_label="rates", color="red", line_width=4)
    fig.line(x, y3, legend_label="swaps", color="blue", line_width=4)
    
    # show the results
    show(fig)
