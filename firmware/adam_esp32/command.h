/*
==================================================
A.D.A.M V1
commands.h
==================================================
*/

#ifndef COMMANDS_H
#define COMMANDS_H

#include "config.h"

class Commands {

public:

    static void begin() {

        pinMode(
            BUZZER_PIN,
            OUTPUT
        );

        digitalWrite(
            BUZZER_PIN,
            LOW
        );

    }

    static void execute(String command) {

        command.trim();

        if (command.length() == 0)
            return;

        Serial.print("COMMAND: ");
        Serial.println(command);

        if (command == "activate_alarm") {

            activateAlarm();

            return;

        }

        if (

            command == "dismiss" ||

            command == "ignore"

        ) {

            stopAlarm();

            return;

        }

    }

private:

    static void activateAlarm() {

        Serial.println(
            "Alarm Activated"
        );

        for (

            int i = 0;

            i < 10;

            i++

        ) {

            digitalWrite(
                BUZZER_PIN,
                HIGH
            );

            delay(250);

            digitalWrite(
                BUZZER_PIN,
                LOW
            );

            delay(250);

        }

    }

    static void stopAlarm() {

        digitalWrite(
            BUZZER_PIN,
            LOW
        );

        Serial.println(
            "Alarm Stopped"
        );

    }

};

#endif
