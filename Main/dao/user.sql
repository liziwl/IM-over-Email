/*
 Navicat Premium Data Transfer

 Source Server         : IM user db template
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 12/01/2018 21:26:47
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for attachments
-- ----------------------------
DROP TABLE IF EXISTS "attachments";
CREATE TABLE "attachments" (
  "message_id" integer,
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "content" blob,
  CONSTRAINT "fk_msg_id" FOREIGN KEY ("message_id") REFERENCES "messages" ("id")
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
  "is_blocked" integer(1) DEFAULT 0,
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
  CONSTRAINT "fk_group_id" FOREIGN KEY ("group_") REFERENCES "groups" ("group_id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Auto increment value for attachments
-- ----------------------------
UPDATE "main"."sqlite_sequence" SET seq = 4 WHERE name = 'attachments';

PRAGMA foreign_keys = true;
