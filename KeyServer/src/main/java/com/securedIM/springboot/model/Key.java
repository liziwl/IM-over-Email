package com.securedIM.springboot.model;

import org.hibernate.validator.constraints.NotEmpty;

import javax.persistence.*;

@Entity
@Table(name="MyKey")
public class Key {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;

    @Column(name = "email", unique = true, nullable = false)
    @NotEmpty
    private String email;

    @Column(name = "public_key", nullable = false)
    @NotEmpty
    private String public_key;

    public Key(){

    }

    public Key(String email, String public_key){
        this.email = email;
        this.public_key = public_key;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPublic_key() {
        return public_key;
    }

    public void setPublic_key(String public_key) {
        this.public_key = public_key;
    }
}
