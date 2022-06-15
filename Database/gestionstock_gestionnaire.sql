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
-- Table structure for table `gestionnaire`
--

DROP TABLE IF EXISTS `gestionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionnaire` (
  `idgestionnaire` varchar(45) NOT NULL,
  `nomComplet` varchar(45) NOT NULL,
  `telephone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT '0000',
  `path` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`idgestionnaire`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionnaire`
--

LOCK TABLES `gestionnaire` WRITE;
/*!40000 ALTER TABLE `gestionnaire` DISABLE KEYS */;
INSERT INTO `gestionnaire` VALUES ('0000','admin','0616452352','Rabat agdal1','omaimaouahline01@gmail.com','cfcd208495d565ef66e7dff9f98764da','D:inptPFARapportphotologo.png'),('0001','omaima ouahline','0606060606','Rabat madinat al irfane','omaimaouahline@gmail.com','9a797095236a1ef9abefbe6edb8ddf27','D:inptPFARapportphotologo.png'),('0002','fatima taoufiq','0707070707','Temara','fatimata352@gmail.com','912e1c889fc7616798193b31e1dd740a',NULL),('0003','test1','0245789647','Rabat','omaimaouahline01@gmail.com','3380ea84b92b83010f920cd61389bab4','profil1.png'),('0004','t','0214587964','Rabat','omaimaouahline01@gmail.com','83dd29386397e5da56aa55a55bbbe491','profil1.png'),('0005','test','0615478975','Rabat','omaimaouahline01@gmail.com','61dfc04631635522d7087b9a82606db5','profil1.png');
/*!40000 ALTER TABLE `gestionnaire` ENABLE KEYS */;
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
