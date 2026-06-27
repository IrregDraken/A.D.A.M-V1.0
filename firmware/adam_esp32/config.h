/*
==================================================
A.D.A.M V1
config.h

Central configuration file.

Edit ONLY this file when changing:
- Wi-Fi
- Server
- Device ID
- GPIO Pins
==================================================
*/

#ifndef CONFIG_H
#define CONFIG_H

//==================================================
// Wi-Fi
//==================================================

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";


//==================================================
// Backend
//==================================================

// Local Flask server running on your laptop

const char* SERVER_URL = "http://10.96.53.176:5000";


//==================================================
// Device
//==================================================

const char* DEVICE_ID = "pir_01";


//==================================================
// GPIO
//==================================================

// PIR Sensor

#define PIR_PIN 14

// Active Buzzer

#define BUZZER_PIN 27


//==================================================
// Timers
//==================================================

// Prevent duplicate alerts

const unsigned long MOTION_COOLDOWN = 5000;

// Check server every second

const unsigned long COMMAND_INTERVAL = 1000;

// Heartbeat every 30 seconds
// (future feature)

const unsigned long HEARTBEAT_INTERVAL = 30000;


//==================================================
// HTTP
//==================================================

const int HTTP_TIMEOUT = 5000;

#endif
