import colorgram

selected_colors = colorgram.extract('hirst-white-paper.jpg', 20)
rgb_tuples = []
for selected_color in selected_colors:
    rgb_tuples.append(tuple(selected_color.rgb))
print(rgb_tuples)
