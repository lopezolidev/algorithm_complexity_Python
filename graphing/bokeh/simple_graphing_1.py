from bokeh.plotting import figure, show

if __name__ == "__main__":
    fig = figure(title="first_line_plot", x_axis_label="days", y_axis_label="explosions")
    # creating the new plot with labels for x, y axis and title of the plot

    print(type(fig))
    # what's a figure?

    values = int(input("insert the number of values: "))

    x_vals = list(range(values))

    y_vals = []

    for i in x_vals:
        y_vals.append(int(input(f"Insert a value for {i}: ")))

    fig.line(x_vals, y_vals, legend_label="tendency to explode", line_width=4)
    # giving a line to our plot, inserting x and y values, so as a label for this line graph and width of the line in pixels
   
    show(fig)
    # calling function 'show' for display in the browser 
    