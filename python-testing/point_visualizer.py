import svgwrite

# Coordinates you provided
points = [[58, 221], [72, 150], [129, 115], [199, 89], [279, 89], [345, 107], [390, 150], [439, 225],
          [437, 310], [391, 330], [83, 256], [129, 274], [153, 322], [234, 330], [297, 368], [294, 414],
          [357, 380], [327, 325], [286, 273], [356, 230], [210, 266], [134, 209], [182, 165], [248, 212], [299, 167]]

# Settings
output_size = (512, 512)
circle_radius = 5
text_offset = (6, -6)
color = "#000000"

# Create SVG
dwg = svgwrite.Drawing("numbered_points.svg", size=output_size)
dwg.viewbox(0, 0, *output_size)

# Draw each point with a number
for i, (x, y) in enumerate(points):
    dwg.add(dwg.circle(center=(x, y), r=circle_radius, fill=color))
    dwg.add(dwg.text(str(i), insert=(x + text_offset[0], y + text_offset[1]),
                     font_size="16px", fill="black", font_family="Arial"))

dwg.save()
print("Saved as numbered_points.svg")
