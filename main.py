from calculations import *
from input import *
from function import *

if ask_input_data() == 1:
    x, y = get_points_file()
    temp_func = None
else:
    x, y = get_points_from_func(func, 0, 6, 0.5, 0.1)
    temp_func = func

x_plot = np.linspace(np.min(x) - 1, np.max(x) + 1, 1000)

plot(x_plot, temp_func, [lagranz_method(x, y, x_now) for x_now in x_plot], x, y)