import numpy as np
import matplotlib.pyplot as plt
import warnings

#MADE BY YAMAN BİLGİ TV (YBT)
# Close warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# c
c = 3j + 2

# Fractal equation form: f(a, c) = a^2 + c
def f(a, c):
    return a**2 + c

# MAIN EQUATION:
def iterate(z, c):
    inner = np.exp(z**2) + z / c
    return f(inner, c)

# Fractal calculation:
def compute_fractal(x_min, x_max, y_min, y_max, width, height, c, max_iter=100, threshold=10):
    image = np.zeros((height, width))
    for ix in range(width):
        for iy in range(height):
            x = x_min + (x_max - x_min) * ix / (width - 1)
            y = y_min + (y_max - y_min) * iy / (height - 1)
            z = complex(x, y)

            for n in range(max_iter):
                try:
                    z = iterate(z, c)
                except:
                    break

                if abs(z) > threshold:
                    image[iy, ix] = n
                    break
            else:
                image[iy, ix] = max_iter

    return image

# Zooming:
def zoomable_fractal():
	#FRACTAL SEEMING PROPERTRIES
    x_min, x_max = -4, 4
    y_min, y_max = -4, 4
    zoom_factor = 0.5
    width, height = 800, 800

    fig, ax = plt.subplots()
	#NAME
    plt.title("Welcome to The Yaman's Fractal Maker! (Left click for zoom)")

    image = compute_fractal(x_min, x_max, y_min, y_max, width, height, c)
    img = ax.imshow(image, extent=(x_min, x_max, y_min, y_max),
                    cmap="twilight_shifted", origin="lower")
    plt.colorbar(img, ax=ax, label="Divergence speed")

    # Zoom function
    def on_click(event):
        nonlocal x_min, x_max, y_min, y_max, width, height

        if event.button == 1 and event.inaxes:  # Sol tıkla zoom in
            x_range = x_max - x_min
            y_range = y_max - y_min
            center_x = event.xdata
            center_y = event.ydata

            x_min = center_x - x_range * zoom_factor / 2
            x_max = center_x + x_range * zoom_factor / 2
            y_min = center_y - y_range * zoom_factor / 2
            y_max = center_y + y_range * zoom_factor / 2

            # Zoom's resulation
            width += 200
            height += 200

            print(f"🔍 Zoom: x=[{x_min:.3f}, {x_max:.3f}] y=[{y_min:.3f}, {y_max:.3f}]")

            image = compute_fractal(x_min, x_max, y_min, y_max, width, height, c)
            img.set_data(image)
            img.set_extent((x_min, x_max, y_min, y_max))
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("button_press_event", on_click)
    plt.show()

# Start Program!
zoomable_fractal()
