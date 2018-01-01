package com.securedIM.springboot.controller;

import com.securedIM.springboot.model.Key;
import com.securedIM.springboot.service.KeyService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@CrossOrigin("*")
@RequestMapping("/api/key")
@RestController
public class KeyController {
    private static final Logger logger = LoggerFactory.getLogger(KeyController.class);
    @Autowired
    private KeyService keyService;

    @PostMapping(value = "")
    public ResponseEntity<?> addKey(@RequestBody Key key){
        if (keyService.getKeyByEmail(key.getEmail()) != null){
            return new ResponseEntity<>(HttpStatus.CONFLICT);
        }
        keyService.addKey(key);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @PostMapping(value = "/public_key")
    public ResponseEntity<?> getPublicKey(@RequestBody Map<String, String> body){
        String email = body.get("email");
        if (keyService.getKeyByEmail(email) == null){
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }
        String public_key = keyService.gerPublicKey(email);
        return new ResponseEntity<String>(public_key, HttpStatus.OK);
    }
}
