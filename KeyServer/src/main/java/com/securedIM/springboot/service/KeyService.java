package com.securedIM.springboot.service;

import com.securedIM.springboot.model.Key;

public interface KeyService {
    void addKey(Key key);
    String gerPublicKey(String email);
    Key getKeyByEmail(String email);
}
