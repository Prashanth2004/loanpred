-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: my_db
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `details`
--

DROP TABLE IF EXISTS `details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `married` varchar(255) DEFAULT NULL,
  `dependents` int DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `self_employed` varchar(255) DEFAULT NULL,
  `applicant_income` decimal(10,2) DEFAULT NULL,
  `coapplicant_income` decimal(10,2) DEFAULT NULL,
  `loan_amount` decimal(10,2) DEFAULT NULL,
  `loan_amount_term` int DEFAULT NULL,
  `credit_history` int DEFAULT NULL,
  `property_area` varchar(255) DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `entered_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `details`
--

LOCK TABLES `details` WRITE;
/*!40000 ALTER TABLE `details` DISABLE KEYS */;
INSERT INTO `details` VALUES (2,1,'Yes',2,'Graduate','Yes',10000000.00,2000000.00,20000000.00,36,4,'Urban','Approved','2023-06-19 14:29:07'),(3,1,'Yes',5,'Not Graduate','No',200000.00,100000.00,10000000.00,36,0,'Rural','Not Approved','2023-06-19 14:30:18'),(4,1,'Yes',4,'Graduate','Yes',2324233.00,0.00,34000000.00,200,3,'Urban','Not Approved','2023-06-19 14:38:29'),(5,1,'Yes',6,'Not Graduate','No',100000.00,0.00,10000000.00,100,1,'Rural','Not Approved','2023-06-19 14:46:36'),(6,3,'Yes',3,'Graduate','Yes',10000000.00,3500000.00,90000000.00,80,3,'Urban','Not Approved','2023-06-19 14:48:54'),(7,3,'Yes',2,'Graduate','Yes',10000000.00,3700000.00,50000000.00,150,3,'Urban','Not Approved','2023-06-19 14:50:20'),(8,3,'Yes',2,'Graduate','Yes',10000000.00,1000000.00,20000000.00,36,4,'Urban','Approved','2023-06-19 14:51:58'),(9,1,'Yes',3,'Graduate','Yes',10000000.00,200000.00,20000000.00,36,3,'Urban','Approved','2023-06-19 17:19:29'),(10,3,'Yes',3,'Graduate','Yes',10000000.00,3200000.00,20000000.00,40,3,'Urban','Approved','2023-06-20 08:55:20'),(11,1,'Yes',2,'Graduate','Yes',1000000.00,20000.00,2000000.00,30,3,'Urban','Not Approved','2023-06-20 09:46:03'),(12,1,'Yes',2,'Graduate','Yes',10000000.00,2000000.00,20000000.00,36,3,'Urban','Approved','2023-06-25 09:07:42'),(13,7,'Yes',1,'Graduate','Yes',2000000.00,20000.00,1500000.00,40,3,'Urban','Not Approved','2023-06-27 08:52:47'),(14,7,'Yes',2,'Graduate','Yes',2000000.00,50000.00,1500000.00,36,2,'Urban','Approved','2023-06-27 08:53:53');
/*!40000 ALTER TABLE `details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-03 22:52:06
