import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

# Load your image here
image_path = "dendritic-logo-new(1).png"
img = mpimg.imread(image_path)

clicked_points = []

def onclick(event):
    if event.xdata and event.ydata:
        x, y = int(event.xdata), int(event.ydata)
        clicked_points.append((x, y))
        plt.plot(x, y, 'ro')
        plt.draw()

fig, ax = plt.subplots()
ax.imshow(img)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.title("Click to mark points. Close the window when done.")
plt.show()

# Save points
print("Collected Points:")
print(clicked_points)

# Save to JSON file
with open("points.json", "w") as f:
    json.dump(clicked_points, f)

print("Points saved to 'points.json'")
