-- CREATE DB
CREATE DATABASE ctfdb;
use ctfdb;

-- CTF USER
CREATE USER 'ctfuser'@'%' IDENTIFIED BY 'ctfpass';
GRANT SELECT ON ctfdb . * TO 'ctfuser'@'%';
GRANT INSERT ON ctfdb . * TO 'ctfuser'@'%';
GRANT CREATE ON ctfdb . * TO 'ctfuser'@'%';
GRANT UPDATE ON ctfdb . * TO 'ctfuser'@'%';

CREATE TABLE `ctfdb`.`uAgents` (
`id` int( 11 ) NOT NULL AUTO_INCREMENT ,
`userAgent` varchar( 128 ) NOT NULL ,
`url` varchar( 128 ) NOT NULL ,
PRIMARY KEY ( `id` ) ,
UNIQUE KEY `userAgent` ( `userAgent` )
) ENGINE = MYISAM DEFAULT CHARSET = utf8;

INSERT INTO `ctfdb`.`uAgents` (`userAgent`, `url`) VALUES ('AgentTester v1', 'https://google.com');