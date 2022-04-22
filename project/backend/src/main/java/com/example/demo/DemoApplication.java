package com.example.demo;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class DemoApplication {

    @Bean
    public MqttClient mqttClient(){
        try {
            MqttClient mqttClient = new MqttClient("tcp://broker.hivemq.com:1883", MqttClient.generateClientId());
            mqttClient.connect();
            return mqttClient;
        } catch (MqttException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws MqttException {
        ConfigurableApplicationContext context = SpringApplication.run(DemoApplication.class, args);
    }

}
