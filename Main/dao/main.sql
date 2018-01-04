/*
 Navicat Premium Data Transfer

 Source Server         : IM main
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 04/01/2018 23:13:54
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
  "account" text,
  "lock_password" text,
  "smtp_server" text,
  "smtp_port" integer,
  "imap_server" text,
  "imap_port" integer,
  "password" text,
  PRIMARY KEY ("account")
);

PRAGMA foreign_keys = true;
