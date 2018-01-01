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
  PRIMARY KEY ("account")
);

PRAGMA foreign_keys = true;
