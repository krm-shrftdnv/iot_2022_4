package com.example.demo.mqtt;

import com.example.demo.model.Indications;
import com.example.demo.repository.IndicationsRepository;
import com.google.gson.Gson;
import lombok.Getter;
import lombok.Setter;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;

@Service
@Getter
@Setter
public class SimpleMqttCallBack implements MqttCallback {

    @Autowired
    IndicationsRepository indicationsRepository;

    @Autowired
    MqttPublisher publisher;

    private int CO2 = 1000;
    private int tVOC = 9;

    Gson gson = new Gson();

    @Override
    public void connectionLost(Throwable throwable) {
        System.out.println("Connection to MQTT broker lost!");
    }

    @Override
    public void messageArrived(String s, MqttMessage mqttMessage) throws MqttException {
        Indications indications = gson.fromJson(new String(mqttMessage.getPayload()), Indications.class);
        indications.setCreatedAt(new Date());
        indicationsRepository.save(indications);

        if (indications.getCO2() > CO2 || indications.getTVOC() > tVOC) {
            publisher.publish("alert");
        }
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {
    }
}
