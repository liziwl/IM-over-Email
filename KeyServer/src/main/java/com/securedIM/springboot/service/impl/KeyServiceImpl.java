package com.securedIM.springboot.service.impl;

import com.securedIM.springboot.model.Key;
import com.securedIM.springboot.repository.KeyRepository;
import com.securedIM.springboot.service.KeyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;


@Service("KeyService")
public class KeyServiceImpl implements KeyService {
    @Autowired
    private KeyRepository keyRepository;
    @Autowired
    JdbcTemplate jdbcTemplate;

    @Override
    public void addKey(Key key) {
//        String sql = String.format("INSERT INTO MYKEY(email, public_key) VALUES(%s, %s)",
//                key.getEmail(), key.getPublic_key());
//        jdbcTemplate.update(sql);
        keyRepository.save(key);
    }

    @Override
    public Key getKeyByEmail(String email) {
        return keyRepository.findByEmail(email);
    }

    @Override
    public String gerPublicKey(String email) {
        Key key = keyRepository.findByEmail(email);
        if (key != null){
            return key.getPublic_key();
        }
        return null;
    }
}
