/*
 Navicat Premium Data Transfer

 Source Server         : IM user db template
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 16/01/2018 13:44:32
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for attachments
-- ----------------------------
DROP TABLE IF EXISTS "attachments";
CREATE TABLE "attachments" (
  "message_id" integer,
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "data" blob,
  "filename" text,
  CONSTRAINT "fk_msg_id" FOREIGN KEY ("message_id") REFERENCES "messages" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for black_list
-- ----------------------------
DROP TABLE IF EXISTS "black_list";
CREATE TABLE "black_list" (
  "account" text,
  PRIMARY KEY ("account")
);

-- ----------------------------
-- Table structure for contacts
-- ----------------------------
DROP TABLE IF EXISTS "contacts";
CREATE TABLE "contacts" (
  "name" text,
  "account" text,
  "public_key" text,
  "trusted" integer(1),
  PRIMARY KEY ("account")
);

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS "groups";
CREATE TABLE "groups" (
  "name" text,
  "uuid" text,
  PRIMARY KEY ("uuid")
);

-- ----------------------------
-- Table structure for member_in_group
-- ----------------------------
DROP TABLE IF EXISTS "member_in_group";
CREATE TABLE "member_in_group" (
  "id" integer,
  "group_id" integer,
  "account" text,
  PRIMARY KEY ("id"),
  CONSTRAINT "fk_group_id" FOREIGN KEY ("group_id") REFERENCES "groups" ("uuid") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS "messages";
CREATE TABLE "messages" (
  "content" text,
  "date_" text,
  "sender" text,
  "group_" integer,
  "id" integer,
  PRIMARY KEY ("id"),
  CONSTRAINT "fk_group_id" FOREIGN KEY ("group_") REFERENCES "groups" ("uuid")
);

PRAGMA foreign_keys = true;
