/*
 Navicat Premium Data Transfer

 Source Server         : IM user db template
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 01/01/2018 15:47:54
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for contacts
-- ----------------------------
DROP TABLE IF EXISTS "contacts";
CREATE TABLE "contacts" (
  "id" integer(11,2),
  "name" text,
  "account" text,
  "public_key" text,
  "trusted" integer(1),
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS "groups";
CREATE TABLE "groups" (
  "name" text,
  "uuid" text,
  PRIMARY KEY ("uuid", "name")
);

-- ----------------------------
-- Table structure for member_in_group
-- ----------------------------
DROP TABLE IF EXISTS "member_in_group";
CREATE TABLE "member_in_group" (
  "id" integer,
  "member_id" integer,
  "group_id" integer,
  PRIMARY KEY ("id"),
  CONSTRAINT "fk_member_id" FOREIGN KEY ("member_id") REFERENCES "contacts" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "fk_group_id" FOREIGN KEY ("group_id") REFERENCES "groups" ("uuid") ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT "unique_record" UNIQUE ("member_id" ASC, "group_id" ASC) ON CONFLICT FAIL
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
  CONSTRAINT "fk_group_id" FOREIGN KEY ("group_") REFERENCES "groups" ("uuid") ON DELETE NO ACTION ON UPDATE NO ACTION
);

PRAGMA foreign_keys = true;
