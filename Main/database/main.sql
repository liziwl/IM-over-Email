/*
 Navicat Premium Data Transfer

 Source Server         : IM main
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 30/12/2017 14:43:01
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
  "account" text,
  "uuid" text,
  "lock_password" text,
  "private_key" text,
  "public_key" text,
  PRIMARY KEY ("account")
);

PRAGMA foreign_keys = true;
