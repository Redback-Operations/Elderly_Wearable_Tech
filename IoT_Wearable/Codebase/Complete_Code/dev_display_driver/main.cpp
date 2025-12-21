// This is used for:
// - Arduino Nano 33 IoT board, paired with
// - WaveShare ST7789v2 display module

#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7789.h> // Hardware-specific library for ST7789, used for initializing display object
#include <SPI.h>
#include <WiFiNINA.h>
#include <WiFiUdp.h>
#include <RTCZero.h>

//Include user defined header files
#include <template.h>
#include <wifi_time.h>

//Setting up the pins 
  #define TFT_CS        10
  #define TFT_RST        8
  #define TFT_DC         9

// We are using the HARDWARE SPI pins for MOSI and SCLK, which are unique
// to each board and not reassignable. For Arduino Nano 33 IoT: MOSI = pin 11 and
// SCLK = pin 13. This is done to improve the performance of the display.

// Create a display object of the Adafruit_ST7789 class
Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_RST);

//Declare rtc object for real time clock
RTCZero rtc;


void drawTemplate() {
  tft.fillScreen(ST77XX_BLACK); //Clear screen before redrawing
  
  uint8_t padding = 10; // Padding for layout

  // Top Section: Battery level with battery icon
  drawBatteryIcon(tft, padding + 10, padding + 10, ST77XX_WHITE);  // Draw battery icon with 85% charge

  // First Section: Heart Rate and SpO2
  drawHeartIcon(tft, padding + 10, padding + 170, ST77XX_RED);    // Heart icon
  drawBubbleIcon(tft, padding + 10, padding + 240, ST77XX_CYAN); // Bubble icon with SpO2 percentage

  drawCircularStepsGauge(tft, 170, 220, 2000, 10000, ST77XX_GREEN);

  // Fourth Section: Body Temperature
  drawThermometerIcon(tft, padding + 10, padding + 200); // Thermometer icon

  // Use the new RTC-aware version of drawTime
  drawTime(tft, rtc, 20, 85, ST77XX_WHITE);
  drawDate(tft, rtc, 120, 25, ST77XX_WHITE);
}

void setup() {
  // Initialize Serial Monitor
  Serial.begin(9600);
  Serial.println(F("Initializing ST7789 Display..."));

  // Initialize WiFi
  WiFi_Setup(WiFi, rtc);
  
  // Initialize display (240x280 resolution)
  tft.init(240, 280);
  tft.setRotation(2); // Portrait orientation
  tft.fillScreen(ST77XX_BLACK);

  // Set default text size and color
  tft.setTextSize(2);
  tft.setTextColor(ST77XX_WHITE);

  // Draw the template
  drawTemplate();
}

void loop() {
  // Continuously update the time every second
  delay(3000);  // Wait for 3 seconds
  drawTemplate();  // Redraw the template to update the time
}
