/*
==================================================
A.D.A.M V1 Firmware

ESP32 Dev Module
==================================================
*/

#include "config.h"
#include "wifi_manager.h"
#include "api_client.h"
#include "sensors.h"
#include "commands.h"

Sensors sensors;

unsigned long lastCommandPoll = 0;

void setup() {

    Serial.begin(115200);

    delay(1000);

    Commands::begin();

    sensors.begin();

    WiFiManager::connect();

    Serial.println();
    Serial.println("========================");
    Serial.println("A.D.A.M READY");
    Serial.println("========================");
    Serial.println();

}

void loop() {

    //------------------------------------------------
    // Maintain WiFi
    //------------------------------------------------

    WiFiManager::reconnect();

    //------------------------------------------------
    // Motion Detection
    //------------------------------------------------

    if (

        sensors.motionDetected()

    ) {

        Serial.println(
            "Motion Detected"
        );

        bool sent = APIClient::sendMotionEvent();

        if (sent) {

            Serial.println(
                "Event Uploaded"
            );

        }

        else {

            Serial.println(
                "Upload Failed"
            );

        }

    }

    //------------------------------------------------
    // Poll Commands
    //------------------------------------------------

    if (

        millis()

        -

        lastCommandPoll

        >

        COMMAND_INTERVAL

    ) {

        lastCommandPoll = millis();

        String command =

            APIClient::getCommand();

        if (

            command.length()

            >

            0

        ) {

            Commands::execute(

                command

            );

        }

    }

    delay(50);

}
