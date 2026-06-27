/*
==================================================
A.D.A.M V1
sensors.h
==================================================
*/

#ifndef SENSORS_H
#define SENSORS_H

#include "config.h"

class Sensors {

private:

    unsigned long lastMotion = 0;

public:

    void begin() {

        pinMode(

            PIR_PIN,
 
            INPUT

        );

    }

    bool motionDetected() {

        if (

            digitalRead(PIR_PIN)

            == HIGH

        ) {

            if (

                millis()

                - lastMotion

                >

                MOTION_COOLDOWN

            ) {

                lastMotion = millis();

                return true;

            }

        }

        return false;

    }

};

#endif
