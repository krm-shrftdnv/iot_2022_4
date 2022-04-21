package com.example.demo;

import com.example.demo.mqtt.MqttSubscriber;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) throws MqttException {
        SpringApplication.run(DemoApplication.class, args);
        MqttSubscriber.main(args);
    }

}
