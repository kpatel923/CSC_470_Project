-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.7.32-log

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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id_book` int(11) NOT NULL AUTO_INCREMENT,
  `book_code` varchar(45) COLLATE utf8_bin NOT NULL,
  `book_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `book_subject` varchar(45) COLLATE utf8_bin NOT NULL,
  `book_author` varchar(45) COLLATE utf8_bin NOT NULL,
  `book_description` varchar(100) COLLATE utf8_bin NOT NULL,
  `book_price` float NOT NULL,
  `book_status` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id_book`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'1','Python','Coding','Jean P Morgan','Beginners guide to Python',230,'Renew'),(2,'2','Java','Programming','JJ Mc','Java OOP',251,'Request hold'),(3,'3','Python 3','Coding','JJ Mc','OOP with Python',315,'Check Out'),(4,'4','C++','Coding','Jean P Morgan','C++ for beginners',257,NULL),(5,'5','Python','Programming','JJ Mc','Advance Python',287,NULL),(6,'6','Calculus 2','Math','Jean P Morgan','Easy way to learn Calculus 2',251,NULL),(7,'7','Calculus 1','Math','Chris McCain','Get startedwith Calculus 1',152,NULL),(8,'8','Software Engineering','Programming','Pablo Rivera','A practicioners approach to Software Engineering',328,NULL),(9,'9','C++','Programming','Chris McCain','Operating Systems',190,NULL),(10,'10','Java','Coding','Pablo Rivera','Advance Programming with Java',275,NULL);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-07 10:56:23
