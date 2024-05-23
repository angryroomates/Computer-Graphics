#include <stdio.h>
#include <stdlib.h>

void drawLine(int x0, int y0, int xn, int yn) {
    int dx = abs(xn - x0); // Difference in x
    int dy = abs(yn - y0); // Difference in y
    int x = x0;
    int y = y0;
    
    int x_inc = (xn > x0) ? 1 : -1; // Direction of x increment
    int y_inc = (yn > y0) ? 1 : -1; // Direction of y increment
    
    if (dx >= dy) {
        // Slope <= 1
        int Pk = 2 * dy - dx;
        for (int i = 0; i <= dx; i++) {
            printf("x: %d, y: %d\n", x, y);
            x += x_inc; // Increment x for each step
            if (Pk < 0) {
                Pk += 2 * dy; // Update decision parameter if Pk < 0
            } else {
                y += y_inc; // Increment y conditionally
                Pk += 2 * dy - 2 * dx; // Update decision parameter
            }
        }
    } else {
        // Slope > 1
        int Pk = 2 * dx - dy;
        for (int i = 0; i <= dy; i++) {
            printf("x: %d, y: %d\n", x, y);
            y += y_inc; // Increment y for each step
            if (Pk < 0) {
                Pk += 2 * dx; // Update decision parameter if Pk < 0
            } else {
                x += x_inc; // Increment x conditionally
                Pk += 2 * dx - 2 * dy; // Update decision parameter
            }
        }
    }
}

int main() {
    int x0 = 10, y0 = 5, xn = 20, yn = 15;
    drawLine(x0, y0, xn, yn);
    return 0;
}
