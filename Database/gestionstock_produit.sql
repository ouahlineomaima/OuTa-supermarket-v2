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
-- Table structure for table `produit`
--

DROP TABLE IF EXISTS `produit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produit` (
  `idproduit` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `quantite` int NOT NULL,
  `service` varchar(45) NOT NULL,
  `prix` int NOT NULL,
  `min` int NOT NULL,
  `max` int NOT NULL,
  PRIMARY KEY (`idproduit`),
  KEY `service` (`service`),
  CONSTRAINT `service` FOREIGN KEY (`service`) REFERENCES `service` (`idservice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produit`
--

LOCK TABLES `produit` WRITE;
/*!40000 ALTER TABLE `produit` DISABLE KEYS */;
INSERT INTO `produit` VALUES ('1','Cocacola 1L',71,'1',6,70,100),('10','millefeuilles',20,'4',3,0,100),('11','Paquet pain de mie',50,'4',15,0,0),('13','Pomme de terre',100,'5',100,0,0),('14','Fraise',30,'5',15,0,0),('15','Sneackers',100,'6',6,0,0),('16','Mars',100,'6',6,0,0),('17','Twix',100,'6',6,0,0),('18','Arial matic 5kg',50,'00',100,0,0),('2','Hawai',71,'1',6,70,100),('3','Ouelmes 1L',17,'1',10,0,0),('4','Sidi Ali 1L',59,'1',6,0,0),('50','prodduit',10,'5',10,0,0),('6','Four Itimat',5,'2',1300,0,0),('7','Machine à laver Samsung',8,'2',3000,0,0),('75','produit',68,'1',100,0,0),('8','Poulet',50,'3',33,0,0),('9','Filet d\'agneau',20,'3',100,0,0);
/*!40000 ALTER TABLE `produit` ENABLE KEYS */;
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
