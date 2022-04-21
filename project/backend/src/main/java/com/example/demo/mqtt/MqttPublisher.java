package com.example.demo.mqtt;

import com.example.demo.model.Control;
import com.example.demo.repository.ControlRepository;
import com.google.gson.Gson;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MqttPublisher {

    @Autowired
    ControlRepository controlRepository;

    Gson gson = new Gson();

    public void publish(String messageString) throws MqttException {

        Control control = controlRepository.save(Control.builder().command(messageString).build());
        messageString = gson.toJson(control);

        MqttClient client = new MqttClient("https://broker.hivemq.com:1883", MqttClient.generateClientId());
        client.connect();
        MqttMessage message = new MqttMessage();
        message.setPayload(messageString.getBytes());
        client.publish("itis_team_4/control", message);

        System.out.println("\tMessage '" + messageString + "' to 'itis_team_4/control'");

        client.disconnect();

    }

}
