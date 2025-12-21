#ifndef wifi_time_h
#define wifi_time_h

#include <WiFiNINA.h>  // WiFi library for Arduino boards using NINA module
#include <WiFiUdp.h>   // Required for time retrieval using NTP
#include <RTCZero.h>   // Real-time clock library

// Debug toggle: Set to false to disable Serial prints
bool WIFI_DEBUG = true;

// WiFi credentials
#define SECRET_SSID "REPLACE_WITH_YOUR_SSID"
#define SECRET_PASS "REPLACE_WITH_YOUR_PASSWORD"

// WiFi connection status tracking variable
int status = WL_IDLE_STATUS;

/**
 * Function to connect to WiFi and synchronize RTC with NTP time.
 * 
 * @param wifi  Reference to the WiFi module instance (usually `WiFi`)
 * @param rtc   Reference to RTCZero instance used for tracking real time
 * 
 * @return true if setup was successful and time was synced, false otherwise
 */
bool WiFi_Setup(WiFiClass& wifi, RTCZero& rtc) {
  // Check if WiFi module is present and working
  if (wifi.status() == WL_NO_SHIELD) {
    if (WIFI_DEBUG) Serial.println("WiFi adapter not ready");
    return false;  // Exit early if WiFi hardware is not detected
  }

  // Attempt to connect to the WiFi network
  while (status != WL_CONNECTED) {
    if (WIFI_DEBUG) {
      Serial.print("Connecting to SSID: ");
      Serial.println(SECRET_SSID);
    }
    status = wifi.begin(SECRET_SSID, SECRET_PASS);  // Start connection attempt
    delay(3000); // Wait 3 seconds before retrying
  }

  if (WIFI_DEBUG) Serial.println("WiFi connected!");


  // Clock logic to be fixed, currently not accurate

  // Initialize the real-time clock
  rtc.begin();

  // Try to get the current time from an NTP server
  unsigned long epoch;           // Stores the retrieved epoch time
  int tries = 0, maxTries = 6;   // Retry up to 6 times

  do {
    epoch = wifi.getTime();  // Request time from NTP server
    tries++;
    delay(1000);             // Wait 1 second between tries
  } while ((epoch == 0) && (tries < maxTries));

  // If time could not be retrieved after maxTries, return false
  if (tries == maxTries) {
    if (WIFI_DEBUG) Serial.println("NTP unreachable!!");
    return false;
  }

Serial.print("Epoch received: ");
Serial.println(epoch);

  // Set RTC time using the retrieved epoch
  rtc.setEpoch(epoch);
  if (WIFI_DEBUG) Serial.println("Time synced.");

  return true;
}

#endif
