-- MYSQL BLIND ERROR BASED

-- CREAR DB
CREATE DATABASE blindhackerDB;
use blindhackerDB;

CREATE TABLE `blindhackerDB`.`userinfo` (
`id` int( 11 ) NOT NULL AUTO_INCREMENT ,
`username` varchar( 30 ) NOT NULL ,
`email` varchar( 50 ) NOT NULL ,
`password` varchar( 128 ) NOT NULL ,
PRIMARY KEY ( `id` ) ,
UNIQUE KEY `username` ( `username` )
) ENGINE = MYISAM DEFAULT CHARSET = utf8;

INSERT INTO `userinfo`(`username`, `email`, `password`) VALUES ('betauser','flag{sqli_is_l0v3_but_','letsputapass!');
INSERT INTO `userinfo`(`username`, `email`, `password`) VALUES ('auseryouarenotsearchingf0r','i@told.u','you4recrazy');
INSERT INTO `userinfo`(`username`, `email`, `password`) VALUES ('mike','mikedun@geo.on','giveitatryifyouhaventalready');

-- USER READ-ONLY
CREATE USER 'readuser'@'%' IDENTIFIED BY 'readuserpassword';
GRANT SELECT ON blindhackerDB . * TO 'readuser'@'%';
GRANT SELECT ON tokenDB . * TO 'readuser'@'%';
GRANT DELETE ON tokenDB . * TO 'readuser'@'%';
GRANT INSERT ON tokenDB . * TO 'readuser'@'%';

-- CREAR DB
CREATE DATABASE tokenDB;
use tokenDB;

CREATE TABLE `tokenDB`.`indextokens` (
`token` varchar( 110 ) NOT NULL ,
`fecha` datetime default CURRENT_TIMESTAMP ,
UNIQUE KEY `token` ( `token` )
) ENGINE = MYISAM DEFAULT CHARSET = utf8;

CREATE TABLE `tokenDB`.`forumtokens` (
`token` varchar( 110 ) NOT NULL ,
`fecha` datetime default CURRENT_TIMESTAMP ,
UNIQUE KEY `token` ( `token` )
) ENGINE = MYISAM DEFAULT CHARSET = utf8;

-- Eventos que eliminan cada dos minutos los tokens

CREATE EVENT drop_indextokens ON SCHEDULE EVERY 2 MINUTE STARTS CURRENT_TIMESTAMP DO DELETE FROM indextokens;
CREATE EVENT drop_forumtokens ON SCHEDULE EVERY 2 MINUTE STARTS CURRENT_TIMESTAMP DO DELETE FROM forumtokens;
