package com.securedIM.springboot.repository;

import com.securedIM.springboot.model.Key;
import org.springframework.data.repository.CrudRepository;

import javax.transaction.Transactional;

@Transactional
public interface KeyRepository extends CrudRepository<Key, Integer>{
    public Key findByEmail(String email);
    public Key findById(int id);
    @Override
    Key save(Key key);
    @Override
    void delete(Key key);
}
