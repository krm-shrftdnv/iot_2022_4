package com.example.demo.controller;

import com.example.demo.model.Control;
import com.example.demo.model.Indications;
import com.example.demo.mqtt.MqttPublisher;
import com.example.demo.mqtt.SimpleMqttCallBack;
import com.example.demo.repository.ControlRepository;
import com.example.demo.repository.IndicationsRepository;
import com.google.gson.Gson;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class FrontendController {

    @Autowired
    IndicationsRepository indicationsRepository;

    @Autowired
    MqttPublisher mqttPublisher;

    @Autowired
    SimpleMqttCallBack simpleMqttCallBack;

    @GetMapping("/get")
    public void get() throws MqttException {
        mqttPublisher.publish("get");
    }

    @GetMapping("/start")
    public void start() throws MqttException {
        mqttPublisher.publish("start");
    }

    @GetMapping("/stop")
    public void stop() throws MqttException {
        mqttPublisher.publish("stop");
    }

    @GetMapping("/indications")
    public ResponseEntity<List<Indications>> indications() {
        return ResponseEntity.ok(indicationsRepository.findAll());
    }

    @PostMapping("/set_criticals")
    public void setCriticals(@RequestBody Indications indications){
        simpleMqttCallBack.setCO2(indications.getCO2());
        simpleMqttCallBack.setTVOC(indications.getTVOC());
    }
}
