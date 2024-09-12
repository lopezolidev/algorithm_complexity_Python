from bokeh.plotting import figure, show
from bokeh.models import BoxAnnotation
import random

if __name__ == "__main__":

    #preparing some data:
    x = list(range(0,10))
    y1 = random.sample(range(0, 20), 10)
    y2 = random.sample(range(0, 20), 10)
    
    plot = figure(title="Legend Example")

    line = plot.line(x, y1, legend_label="SDP", line_color="navy", line_width=4)

    circles = plot.scatter(
        x,
        y2,
        marker="circle",
        size=60,
        legend_label="Objects",
        fill_color="red",
        fill_alpha=0.6,
        line_color="orange"
    )

    #changing headline location to the bottom
    plot.title_location = "below" # only valid → "above", "below", "right", "left"

    # if we want to change the text in the title
    plot.title.text = "Changing headline text"

    # styling the headline
    plot.title.text_font_size = "2rem"
    plot.title.align = "center"
    plot.title.background_fill_color = "darkgrey"
    plot.title.text_color = "white"
    plot.title.padding = (16,16) # applying padding in px, the property recieves a tuple ( x = NonNegative(Int), y = NonNegative(Int))

    #displaying the legend in top left corner
    plot.legend.location = "top_left"

    #adding a title to the legend
    plot.legend.title = "Data"

    #changing the appearance of legend text
    plot.legend.label_text_font = "times"
    plot.legend.label_text_font_style = "bold"
    plot.legend.label_text_color = "darkblue"

    #changing the border and background of legend
    plot.legend.border_line_width = 2.8
    plot.legend.border_line_color = "navy"
    plot.legend.border_line_alpha = 0.8
    plot.legend.background_fill_color = "darkblue"
    plot.legend.background_fill_alpha = 0.2

    # creating box annotations for this plot; tops and bottoms are associated with the height of the figure in the y-axis
    low_box = BoxAnnotation(top=4, fill_alpha=0.1, fill_color="#F0E442")
    mid_box = BoxAnnotation(bottom=4, top=16, fill_alpha=0.1, fill_color="#009E73")
    high_box = BoxAnnotation(bottom=16, fill_alpha=0.1, fill_color="#F0E442")

    #adding the box annotations to our figure
    plot.add_layout(low_box)
    plot.add_layout(mid_box)
    plot.add_layout(high_box)

    # showing results
    show(plot)