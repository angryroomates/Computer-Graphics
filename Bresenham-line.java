public class BresenhamLineDrawing {
    public static void drawLine(int x0, int y0, int xn, int yn) {
        int dx = Math.abs(xn - x0); // Difference in x
        int dy = Math.abs(yn - y0); // Difference in y
        int x = x0;
        int y = y0;

        int xInc = (xn > x0) ? 1 : -1; // Direction of x increment
        int yInc = (yn > y0) ? 1 : -1; // Direction of y increment

        if (dx >= dy) {
            // Slope <= 1
            int Pk = 2 * dy - dx;
            for (int i = 0; i <= dx; i++) {
                System.out.println("x: " + x + ", y: " + y);
                x += xInc; // Increment x for each step
                if (Pk < 0) {
                    Pk += 2 * dy; // Update decision parameter if Pk < 0
                } else {
                    y += yInc; // Increment y conditionally
                    Pk += 2 * dy - 2 * dx; // Update decision parameter
                }
            }
        } else {
            // Slope > 1
            int Pk = 2 * dx - dy;
            for (int i = 0; i <= dy; i++) {
                System.out.println("x: " + x + ", y: " + y);
                y += yInc; // Increment y for each step
                if (Pk < 0) {
                    Pk += 2 * dx; // Update decision parameter if Pk < 0
                } else {
                    x += xInc; // Increment x conditionally
                    Pk += 2 * dx - 2 * dy; // Update decision parameter
                }
            }
        }
    }

    public static void main(String[] args) {
        int x0 = 10, y0 = 5, xn = 20, yn = 15;
        drawLine(x0, y0, xn, yn);
    }
}
