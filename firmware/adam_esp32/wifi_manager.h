/*
==================================================
A.D.A.M V1
wifi_manager.h
==================================================
*/

#ifndef WIFI_MANAGER_H
#define WIFI_MANAGER_H

#include <WiFi.h>
#include "config.h"

class WiFiManager {

public:

    static void connect() {

        Serial.println();
        Serial.println("=================================");
        Serial.println("A.D.A.M WiFi Manager");
        Serial.println("=================================");

        WiFi.mode(WIFI_STA);

        WiFi.begin(
            WIFI_SSID,
            WIFI_PASSWORD
        );

        Serial.print("Connecting");

        while (WiFi.status() != WL_CONNECTED) {

            delay(500);

            Serial.print(".");
        }

        Serial.println();
        Serial.println("WiFi Connected");

        Serial.print("SSID : ");
        Serial.println(WIFI_SSID);

        Serial.print("IP   : ");
        Serial.println(
            WiFi.localIP()
        );

        Serial.println();
    }

    static bool connected() {

        return WiFi.status() == WL_CONNECTED;

    }

    static void reconnect() {

        if (connected())
            return;

        Serial.println(
            "WiFi Lost. Reconnecting..."
        );

        WiFi.disconnect();

        delay(1000);

        WiFi.begin(
            WIFI_SSID,
            WIFI_PASSWORD
        );

        unsigned long start = millis();

        while (

            WiFi.status() != WL_CONNECTED &&

            millis() - start < 10000

        ) {

            delay(500);

            Serial.print(".");
        }

        if (connected()) {

            Serial.println();

            Serial.println(
                "Reconnected."
            );

        }

        else {

            Serial.println();

            Serial.println(
                "Reconnect Failed."
            );

        }

    }

};

#endif
