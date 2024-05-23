def draw_line(x0, y0, xn, yn):
    dx = abs(xn - x0)  # Difference in x
    dy = abs(yn - y0)  # Difference in y
    x = x0
    y = y0
    
    x_inc = 1 if xn > x0 else -1  # Direction of x increment
    y_inc = 1 if yn > y0 else -1  # Direction of y increment
    
    if dx >= dy:
        # Slope <= 1
        Pk = 2 * dy - dx
        for _ in range(dx + 1):
            print(f"x: {x}, y: {y}")
            x += x_inc  # Increment x for each step
            if Pk < 0:
                Pk += 2 * dy  # Update decision parameter if Pk < 0
            else:
                y += y_inc  # Increment y conditionally
                Pk += 2 * dy - 2 * dx  # Update decision parameter
    else:
        # Slope > 1
        Pk = 2 * dx - dy
        for _ in range(dy + 1):
            print(f"x: {x}, y: {y}")
            y += y_inc  # Increment y for each step
            if Pk < 0:
                Pk += 2 * dx  # Update decision parameter if Pk < 0
            else:
                x += x_inc  # Increment x conditionally
                Pk += 2 * dx - 2 * dy  # Update decision parameter

# Example usage
x0, y0, xn, yn = 10, 5, 20, 15
draw_line(x0, y0, xn, yn)
