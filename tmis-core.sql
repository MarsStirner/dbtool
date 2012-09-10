DELIMITER $$

DROP DATABASE IF EXISTS `tmis-core` $$
DROP DATABASE IF EXISTS `tmis_core` $$

CREATE DATABASE `tmis_core` CHARACTER SET utf8 COLLATE utf8_general_ci $$

CREATE TABLE `tmis_core`.`Fault` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `timeshot` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `inMessage` MEDIUMTEXT NOT NULL DEFAULT "",
    `outMessage` MEDIUMTEXT NOT NULL DEFAULT "",
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

$$

CREATE TABLE `tmis_core`.`Profile` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `timeshot` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `sessionIdHigh` BIGINT NOT NULL,
    `sessionIdLow` BIGINT NOT NULL,
    `nestedLevel` INT NOT NULL,
    `number` INT NOT NULL,
    `time` BIGINT NOT NULL,
    `className` VARCHAR(256) NOT NULL,
    `methodName` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

$$

CREATE TABLE `tmis_core`.`Setting` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `path` VARCHAR(255) NOT NULL,
    `value` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `path` (`path`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

$$
