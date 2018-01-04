package com.securedIM.springboot.controller;

import com.securedIM.springboot.model.Key;
import com.securedIM.springboot.service.KeyService;
import org.hibernate.validator.constraints.Email;
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

    // add a key
    @PostMapping(value = "")
    public ResponseEntity<?> addKey(@RequestBody Key key){
        Key old_key = keyService.getKeyByEmail(key.getEmail());
        if (old_key != null){
            keyService.delete(old_key);
        }
        keyService.addKey(key);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    // delete a key
    @DeleteMapping(value = "")
    public ResponseEntity<?> removeKey(@RequestBody Map<String, String> body){
        String email = body.get("email");
        Key old_key = keyService.getKeyByEmail(email);
        if (old_key == null){
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }else {
            keyService.delete(old_key);
        }
        return new ResponseEntity<>(HttpStatus.OK);
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
