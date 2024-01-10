PImage img;       // Variable to store the image
int[] grayValues; // Array to store grayscale values

void setup() {
  img = loadImage("data/pass.jpg"); // Load your grayscale image
  size(400,400);
  img.loadPixels();
  
  // Initialize the array to the number of pixels in the image
  grayValues = new int[img.pixels.length];
  
  // Loop over each pixel in the image
  for (int i = 0; i < img.pixels.length; i++) {
    // Since the image is grayscale, red (or green or blue) channel value is enough
    grayValues[i] = int(brightness(img.pixels[i]));
  }

  // Print the grayscale values
  printArray(grayValues);
  //image(img, 0, 0);
}

void printArray(int[] arr) {
  for (int i = 0; i < arr.length; i++) {
    print(arr[i]);
    if (i < arr.length - 1) {
      print(", ");
    }
  }
}
