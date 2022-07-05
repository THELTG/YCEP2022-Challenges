CREATE DATABASE IF NOT EXISTS `secret_database`;
USE `secret_database`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `userid` int(11) NOT NULL,
    `username` varchar(45) NOT NULL,
    `password` varchar(45) NOT NULL
);

LOCK TABLES `users` WRITE;  -- userid, username, password
INSERT INTO `users` VALUES (1,"Johnathan_Elamaran_James","pAssw0rd"),(2,"0xDEADBEEF","hAx0rRR"),(3,"DOCtor_SHARK","aUm_wIreShaRK"),(4,"tH1sIsn0tTh3FlAg","YCEP22{1_hAt3_SQL_iNj3Ct10ns}");
UNLOCK TABLES;

SELECT * FROM users; 