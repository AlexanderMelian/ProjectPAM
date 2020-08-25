DROP DATABASE IF EXISTS ProjectPAM;

CREATE DATABASE ProjectPAM;

USE ProjectPAM;

DROP TABLE IF EXISTS `records`;

CREATE TABLE `records`(
    `record_id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(255),
    `device_id` INT,
    `record_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `desc` TEXT
);

DROP TABLE IF EXISTS `devices`;

CREATE TABLE `devices`(
    `device_id` INT UNSIGNED PRIMARY KEY,
    `owner_name` VARCHAR(20),
    `device_banned` TINYINT(1) NOT NULL DEFAULT 0
);
