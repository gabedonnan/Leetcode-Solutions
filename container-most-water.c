double min(double a, double b) {
    return a<b ? a : b;
}

int maxArea(int* height, int heightSize){
    int lpointer = 0;
    int rpointer = heightSize - 1;
    int lhighest = 0;
    int rhighest = 0;
    int area = 0;
    int maximum = 0;
    while (rpointer > lpointer) {
        if (height[lpointer] > lhighest || height[rpointer] > rhighest) {
            area = min(height[lpointer], height[rpointer]) * abs(rpointer - lpointer);
        }
        if (area > maximum) {
            maximum = area;
        }
        if (height[lpointer] > lhighest) {
            lhighest = height[lpointer];
        }
        if (height[rpointer] > rhighest) {
            rhighest = height[rpointer];
        }
        if (height[lpointer] > height[rpointer]) {
            rpointer--;
        }
        else if (height [lpointer] < height[rpointer]) {
            lpointer++;
        } else {
            lpointer++;
            rpointer--;
        }
    }
    return maximum;
}
