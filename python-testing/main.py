import svgwrite

def draw_logo(output_size=(512, 512), padding=0, bg_color=None, corner_radius=0, circle_radius=13, line_thickness=8, export_type='svg'):

    points = [[58, 221], [72, 150], [129, 115], [199, 89], [279, 89], [345, 107], [390, 150], [439, 225], [437, 310], [391, 330], [83, 256], [129, 274], [153, 322], [234, 330], [297, 368], [294, 414], [357, 380], [327, 325], [286, 273], [356, 230], [210, 266], [134, 209], [182, 165], [248, 212], [299, 167]]

    lines = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 16), (16, 14), (15, 14), (15, 13), (13, 12), (12, 11), (11, 10), (10, 0), (0, 21), (1, 21), (2, 21), (2, 22), (3, 22), (3, 24), (4, 24), (5, 24), (6, 24), (6, 19), (7, 19), (8, 19), (9, 19), (9, 17), (16, 17), (14, 17), (14, 13), (13, 20), (13, 18), (13, 17), (12, 20), (11, 20), (11, 21), (10, 21), (22, 24), (24, 19), (19, 17), (17, 18), (20, 18), (20, 21), (21, 22), (18, 19), (21, 23), (22, 23), (24, 23), (19, 23), (18, 23), (20, 23),
    ]

    color = "#519872"

    dwg = svgwrite.Drawing(f'generated-logo.{export_type}', size=output_size)
    dwg.viewbox(0, 0, *output_size)

    if bg_color:
        dwg.add(dwg.rect(insert=(0, 0), size=output_size, fill=bg_color, rx=corner_radius))

    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    
    pattern_width = max_x - min_x
    pattern_height = max_y - min_y

    scale_x = (output_size[0] - 2 * padding) / pattern_width
    scale_y = (output_size[1] - 2 * padding) / pattern_height

    scale_factor = min(scale_x, scale_y)

    offset_x = (output_size[0] - pattern_width * scale_factor) / 2
    offset_y = (output_size[1] - pattern_height * scale_factor) / 2

    for start_idx, end_idx in lines:
        start = points[start_idx]
        end = points[end_idx]
        
        start_scaled = ((start[0] - min_x) * scale_factor + offset_x,
                        (start[1] - min_y) * scale_factor + offset_y)
        end_scaled = ((end[0] - min_x) * scale_factor + offset_x,
                      (end[1] - min_y) * scale_factor + offset_y)
        dwg.add(dwg.line(start=start_scaled, end=end_scaled, stroke=color, stroke_width=line_thickness))

    for (x, y) in points:
        x_scaled = (x - min_x) * scale_factor + offset_x
        y_scaled = (y - min_y) * scale_factor + offset_y
        dwg.add(dwg.circle(center=(x_scaled, y_scaled), r=circle_radius, fill=color))

    dwg.save()
    print(f"Saved as 'generated-logo.{export_type}'")




draw_logo(output_size=(1024, 1024), padding=200, bg_color='#000000', corner_radius=200, circle_radius=20, line_thickness=10, export_type='svg')
