package com.example.demo.mqtt;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;

public class MqttSubscriber {

    public static void main(String[] args) throws MqttException {

        MqttClient client = new MqttClient("https://broker.hivemq.com:1883", MqttClient.generateClientId());
        client.setCallback(new SimpleMqttCallBack());
        client.connect();

        client.subscribe("itis_team_4/indications");
    }
}
