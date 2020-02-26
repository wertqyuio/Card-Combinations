-- from the terminal run:
-- psql < seed.sql

DROP DATABASE IF EXISTS combinations;

CREATE DATABASE combinations;

\c combinations

CREATE TABLE DEALS
(
  YEAR TEXT NOT NULL,
  MONTH TEXT NOT NULL,
  DAY TEXT NOT NULL,
  BOARD TEXT NOT NULL,
  HANDS TEXT [],
  PRIMARY KEY (YEAR,MONTH,DAY,BOARD)
);
