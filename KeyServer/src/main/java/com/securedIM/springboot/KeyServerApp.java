package com.securedIM.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = {"com.securedIM.springboot"})
public class KeyServerApp {
    public static void main(String[] args){
        SpringApplication.run(KeyServerApp.class, args);
    }
}
