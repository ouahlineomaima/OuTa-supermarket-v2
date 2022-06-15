-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: gestionstock
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acheter`
--

DROP TABLE IF EXISTS `acheter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acheter` (
  `idproduit` varchar(45) NOT NULL,
  `idcommande` varchar(45) NOT NULL,
  `quantite` int NOT NULL,
  `prix` float NOT NULL,
  `total` float NOT NULL,
  PRIMARY KEY (`idproduit`,`idcommande`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acheter`
--

LOCK TABLES `acheter` WRITE;
/*!40000 ALTER TABLE `acheter` DISABLE KEYS */;
INSERT INTO `acheter` VALUES ('1','2',8,6,48),('1','35',7,6,42),('1','36',7,6,42),('1','37',6,6,36),('1','38',1,6,6),('1','39',1,6,6),('1','40',1,6,6),('1','41',1,6,6),('1','42',9,6,54),('1','43',6,6,36),('1','44',4,6,24),('1','45',5,6,30),('1','46',6,6,36),('1','47',6,6,36),('2','1',2,6,12),('2','11',4,6,24),('2','12',2,6,12),('2','13',2,6,12),('2','14',2,6,12),('2','16',3,6,18),('2','33',3,6,18),('2','34',3,6,18),('2','4',3,6,18),('3','15',3,10,30),('3','17',7,10,70),('3','24',3,10,30),('3','3',3,10,30),('3','4',6,10,60),('4','10',4,6,24),('4','18',2,6,12),('4','21',3,6,18),('4','22',3,6,18),('4','23',2,6,12),('4','25',2,6,12),('4','48',7,6,42),('4','49',4,6,24),('4','5',5,6,30),('4','6',3,6,18),('4','7',5,6,30),('4','8',7,6,42),('4','9',2,6,12),('5','8',1,6000,6000),('75','19',3,100,300),('75','20',3,100,300),('75','26',3,100,300),('75','27',2,100,200),('75','28',3,100,300),('75','29',3,100,300),('75','30',2,100,200),('75','31',4,100,400),('75','32',3,100,300),('75','48',4,100,400),('75','49',2,100,200);
/*!40000 ALTER TABLE `acheter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-15  4:13:34
