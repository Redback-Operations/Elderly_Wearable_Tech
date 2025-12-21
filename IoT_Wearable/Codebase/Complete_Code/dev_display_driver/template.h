#ifndef template_h
#define template_h

#include <Adafruit_GFX.h>    // Core graphics library for displays
#include <Adafruit_ST7789.h> // Specific driver for the ST7789 display
#include <SPI.h>             // SPI communication used for the display

/**
 * Get the name of the weekday for a given date using Zeller's Congruence.
 *
 * @param day    Day of the month
 * @param month  Month (1 = January, 12 = December)
 * @param year   Full year (e.g., 2024)
 * @return       Abbreviated weekday name (e.g., "Mon", "Tue", ...)
 */
const char* weekdayName(int day, int month, int year) {
  if (month < 3) {
    month += 12;
    year -= 1;
  }

  int k = year % 100;
  int j = year / 100;
  int h = (day + (13 * (month + 1)) / 5 + k + k/4 + j/4 + 5*j) % 7;

  const char* days[] = {"Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"};
  return days[h];
}

/**
 * Draws a battery icon on the display, representing battery percentage visually.
 */
void drawBatteryIcon(Adafruit_ST7789 tft, int x, int y, uint16_t color) {
  tft.drawRect(x, y, 50, 25, color);                // Battery body outline
  tft.fillRect(x + 52, y + 7, 5, 12, color);        // Battery terminal
  tft.fillRect(x + 2, y + 2, 46, 21, ST77XX_BLACK); // Battery "empty" interior

  // Display the battery percentage as text
  tft.setCursor(x + 8, y + 5);
  tft.setTextColor(color);
  tft.setTextSize(2);
  tft.print("80%");
}

/**
 * Draws a heart icon and displays a heart rate value.
 */
void drawHeartIcon(Adafruit_ST7789 tft, int x, int y, uint16_t color) {
  tft.fillCircle(x + 4, y + 4, 4, color);   // Left part of the heart
  tft.fillCircle(x + 12, y + 4, 4, color);  // Right part of the heart
  tft.fillTriangle(x, y + 4, x + 8, y + 16, x + 16, y + 4, color); // Bottom point

  // Display heart rate
  tft.setCursor(x + 25, y);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);
  tft.print("76");
}

/**
 * Draws a bubble (oxygen) icon and displays an SpO2 percentage value.
 */
void drawBubbleIcon(Adafruit_ST7789 tft, int x, int y, uint16_t color) {
  tft.drawCircle(x + 8, y + 8, 8, color);    // Outer bubble outline
  tft.fillCircle(x + 6, y + 6, 2, color);    // Highlight dot inside

  // Display SpO2 percentage
  tft.setCursor(x + 25, y);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);
  tft.print("98%");
}

/**
 * Draws a thermometer icon and displays a body temperature reading.
 */
void drawThermometerIcon(Adafruit_ST7789 tft, int x, int y) {
  tft.fillRect(x + 4, y + 2, 4, 12, ST77XX_WHITE); // Thermometer stem
  tft.fillCircle(x + 6, y + 16, 3, ST77XX_WHITE);  // Thermometer bulb (outer)
  tft.fillRect(x + 5, y + 7, 2, 12, ST77XX_RED);   // Mercury (stem)
  tft.fillCircle(x + 6, y + 16, 2, ST77XX_RED);    // Mercury (bulb)

  // Display body temperature
  tft.setCursor(x + 25, y + 3);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);
  tft.print("36.4C");
}

/**
 * Displays the current time in HH:MM format using RTCZero.
 */
void drawTime(Adafruit_ST7789 tft, RTCZero& rtc, int x, int y, uint16_t color) {
  int hours = rtc.getHours();
  int minutes = rtc.getMinutes();

  tft.setCursor(x, y);
  tft.setTextColor(color);
  tft.setTextSize(7);
  if (hours < 10) tft.print("0");
  tft.print(hours);
  tft.print(":");
  if (minutes < 10) tft.print("0");
  tft.print(minutes);
}

/**
 * Displays the current date in format: Weekday DD/MM using RTCZero.
 */
void drawDate(Adafruit_ST7789 tft, RTCZero& rtc, int x, int y, uint16_t color) {
  int day = rtc.getDay();
  int month = rtc.getMonth();
  int year = rtc.getYear() + 2000;

  const char* weekday = weekdayName(day, month, year);

  tft.setCursor(x, y);
  tft.setTextColor(color);
  tft.setTextSize(2);
  tft.print(weekday);
  tft.print(" ");

  if (day < 10) tft.print("0");
  tft.print(day);
  tft.print("/");

  if (month < 10) tft.print("0");
  tft.print(month);
}

/**
 * Draws a circular step counter gauge showing progress toward a step goal.
 */
void drawCircularStepsGauge(Adafruit_ST7789 tft, int x, int y, int steps, int maxSteps, uint16_t color) {
  // Draw outer circle for gauge
  tft.fillCircle(x, y, 50, ST77XX_BLACK);   // Background
  tft.drawCircle(x, y, 50, ST77XX_WHITE);  // Border

  // Convert step count to angle (0° to 360°)
  int angle = map(steps, 0, maxSteps, 0, 360);

  // Draw each pixel along the arc
  for (int i = 0; i < angle; i++) {
    int x1 = x + 50 * cos(radians(i));
    int y1 = y - 50 * sin(radians(i));
    tft.drawPixel(x1, y1, color);
  }

  // Label: "Steps" above gauge
  tft.setCursor(x - 15, y - 25);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(1);
  tft.print("Steps");

  // Display current step count in center
  tft.setCursor(x - 22, y - 5);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(2);
  tft.print(steps);

  // Display goal step count below
  tft.setCursor(x - 15, y + 25);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(1);
  tft.print("/");
  tft.print(maxSteps);
}

#endif
