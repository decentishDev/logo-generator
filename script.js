document.getElementById('generateBtn').addEventListener('click', generateLogo);

function generateLogo() {
    const width = parseInt(document.getElementById('width').value);
    const height = parseInt(document.getElementById('height').value);
    const padding = parseInt(document.getElementById('padding').value);
    const bgColor = document.getElementById('bgColor').value;
    const cornerRadius = parseInt(document.getElementById('cornerRadius').value);
    const circleRadius = parseInt(document.getElementById('circleRadius').value);
    const lineThickness = parseInt(document.getElementById('lineThickness').value);

    const points = [
        [58, 221], [72, 150], [129, 115], [199, 89], [279, 89], [345, 107], [390, 150], [439, 225], 
        [437, 310], [391, 330], [83, 256], [129, 274], [153, 322], [234, 330], [297, 368], [294, 414], 
        [357, 380], [327, 325], [286, 273], [356, 230], [210, 266], [134, 209], [182, 165], [248, 212], [299, 167]
    ];
    
    const lines = [
        [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 16], 
        [16, 14], [15, 14], [15, 13], [13, 12], [12, 11], [11, 10], [10, 0], [0, 21], [1, 21], 
        [2, 21], [2, 22], [3, 22], [3, 24], [4, 24], [5, 24], [6, 24], [6, 19], [7, 19], 
        [8, 19], [9, 19], [9, 17], [16, 17], [14, 17], [14, 13], [13, 20], [13, 18], [13, 17], 
        [12, 20], [11, 20], [11, 21], [10, 21], [22, 24], [24, 19], [19, 17], [17, 18], [20, 18], 
        [20, 21], [21, 22], [18, 19], [21, 23], [22, 23], [24, 23], [19, 23], [18, 23], [20, 23]
    ];
    
    const color = "#519872";

    let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}">`;

    if (bgColor) {
        svg += `<rect width="${width}" height="${height}" fill="${bgColor}" rx="${cornerRadius}"></rect>`;
    }

    const min_x = Math.min(...points.map(p => p[0]));
    const max_x = Math.max(...points.map(p => p[0]));
    const min_y = Math.min(...points.map(p => p[1]));
    const max_y = Math.max(...points.map(p => p[1]));

    const pattern_width = max_x - min_x;
    const pattern_height = max_y - min_y;

    const scale_x = (width - 2 * padding) / pattern_width;
    const scale_y = (height - 2 * padding) / pattern_height;

    const scale_factor = Math.min(scale_x, scale_y);
    const offset_x = (width - pattern_width * scale_factor) / 2;
    const offset_y = (height - pattern_height * scale_factor) / 2;

    lines.forEach(([startIdx, endIdx]) => {
        const start = points[startIdx];
        const end = points[endIdx];

        const start_scaled = [
            (start[0] - min_x) * scale_factor + offset_x,
            (start[1] - min_y) * scale_factor + offset_y
        ];

        const end_scaled = [
            (end[0] - min_x) * scale_factor + offset_x,
            (end[1] - min_y) * scale_factor + offset_y
        ];

        svg += `<line x1="${start_scaled[0]}" y1="${start_scaled[1]}" x2="${end_scaled[0]}" y2="${end_scaled[1]}" stroke="${color}" stroke-width="${lineThickness}"></line>`;
    });

    points.forEach(([x, y]) => {
        const x_scaled = (x - min_x) * scale_factor + offset_x;
        const y_scaled = (y - min_y) * scale_factor + offset_y;

        svg += `<circle cx="${x_scaled}" cy="${y_scaled}" r="${circleRadius}" fill="${color}"></circle>`;
    });

    svg += `</svg>`;

    document.getElementById('svgOutput').innerHTML = svg;

    const blob = new Blob([svg], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);
    document.getElementById('downloadLink').href = url;
}
