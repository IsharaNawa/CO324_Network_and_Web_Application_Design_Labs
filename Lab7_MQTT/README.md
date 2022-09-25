![Autograde](../../actions/workflows/workflow.yml/badge.svg)
# CO324 Lab 7: Publish-Subscribe with MQTT

## Objective
* Contrast and compare publish-subscribe against request-response style protocols.
* Choose a suitable topic structure for a particular problem.
* Justify an appropriate QoS for various message types.
* Justify  the appropriateness of using the clean session and retained message flags in a particular application.

## Preparation
* This lab is based on the [Eclipse Paho MQTT](https://github.com/eclipse/paho.mqtt.python) client’s Python bindings.
```bash
pip3 install paho-mqtt
```

## Instructions
* Use **only paho-mqtt and built-in modules** in Python 3 to complete these exercises.
* Put the solutions to coding exercises for the files in `src/` directory.
* **Put your E Number as a comment** in top of each source file.
* **DO NOT** change any code in `test/` directory.

## References
* [Publisher-Subscriber Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber)
* [MQTT Basics](http://www.steves-internet-guide.com/mqtt-basics-course/#clean)


## Exercises
Exercises can be found in the `src/` folder.