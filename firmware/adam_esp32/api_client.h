/*
==================================================
A.D.A.M V1
api_client.h
==================================================
*/

#ifndef API_CLIENT_H
#define API_CLIENT_H

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include "config.h"

class APIClient {

public:

    //------------------------------------------------
    // POST /event
    //------------------------------------------------

    static bool sendMotionEvent(float confidence = 0.95) {

        if (WiFi.status() != WL_CONNECTED)
            return false;

        HTTPClient http;

        String url = String(SERVER_URL) + "/event";

        http.begin(url);

        http.setTimeout(HTTP_TIMEOUT);

        http.addHeader(
            "Content-Type",
            "application/json"
        );

        StaticJsonDocument<256> doc;

        doc["device_id"] = DEVICE_ID;
        doc["event_type"] = "motion";
        doc["confidence"] = confidence;

        String body;

        serializeJson(
            doc,
            body
        );

        int code = http.POST(body);

        Serial.println();

        Serial.print("POST /event -> ");

        Serial.println(code);

        http.end();

        return code == 201;

    }

    //------------------------------------------------
    // GET /commands
    //------------------------------------------------

    static String getCommand() {

        if (WiFi.status() != WL_CONNECTED)
            return "";

        HTTPClient http;

        String url =
            String(SERVER_URL)
            + "/commands/"
            + DEVICE_ID;

        http.begin(url);

        http.setTimeout(
            HTTP_TIMEOUT
        );

        int code = http.GET();

        if (code != 200) {

            http.end();

            return "";

        }

        String response =
            http.getString();

        http.end();

        StaticJsonDocument<256> doc;

        deserializeJson(
            doc,
            response
        );

        if (

            doc["status"] == "idle"

        ) {

            return "";

        }

        return doc["command"];

    }

};

#endif
