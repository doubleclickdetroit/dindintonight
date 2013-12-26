-- MySQL dump 10.13  Distrib 5.1.61, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dindintonight
-- ------------------------------------------------------
-- Server version	5.1.61-0+squeeze1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location_id` int(11) DEFAULT NULL,
  `address` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_6FCA751664D218E` (`location_id`),
  CONSTRAINT `FK_6FCA751664D218E` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (1,1,'10 Witherell St. 17J'),(2,1,'10 Witherell St. 23K'),(3,1,'10 Witherell St. 27B'),(4,2,'1431 Washington Boulevard #203'),(5,2,'1431 Washington Boulevard #204'),(6,2,'1431 Washington Boulevard #205'),(7,2,'1431 Washington Boulevard #317');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stripeId` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `last4` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,'x132456',2589),(2,'y932456',4521),(3,'z421256',7631);
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dropmeals`
--

DROP TABLE IF EXISTS `dropmeals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dropmeals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `drop_id` int(11) NOT NULL,
  `meal_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dropmeals`
--

LOCK TABLES `dropmeals` WRITE;
/*!40000 ALTER TABLE `dropmeals` DISABLE KEYS */;
INSERT INTO `dropmeals` VALUES (1,2,1,2),(2,2,2,4);
/*!40000 ALTER TABLE `dropmeals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drops`
--

DROP TABLE IF EXISTS `drops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drops` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location_id` int(11) DEFAULT NULL,
  `dateAndTime` datetime NOT NULL,
  `timezone` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_CE1E9BEA64D218E` (`location_id`),
  CONSTRAINT `FK_CE1E9BEA64D218E` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drops`
--

LOCK TABLES `drops` WRITE;
/*!40000 ALTER TABLE `drops` DISABLE KEYS */;
INSERT INTO `drops` VALUES (1,1,'0000-00-00 00:00:00',''),(2,1,'0000-00-00 00:00:00',''),(3,1,'2013-12-15 20:00:00','America/Detroit'),(4,2,'2013-12-15 20:00:00','America/Detroit'),(5,1,'2013-12-15 21:00:00','America/Detroit'),(6,2,'2013-12-15 19:00:00','America/Detroit');
/*!40000 ALTER TABLE `drops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `city` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `state` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `zip` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Broderick Tower','10 Witherell St','Detroit','Michigan','48226'),(2,'Detroit City Apartments','1431 Washington Boulevard','Detroit','Michigan','48226');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations_meals`
--

DROP TABLE IF EXISTS `locations_meals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations_meals` (
  `location_id` int(11) NOT NULL,
  `meal_id` int(11) NOT NULL,
  PRIMARY KEY (`location_id`,`meal_id`),
  KEY `IDX_2B7ED19C64D218E` (`location_id`),
  KEY `IDX_2B7ED19C639666D6` (`meal_id`),
  CONSTRAINT `FK_2B7ED19C639666D6` FOREIGN KEY (`meal_id`) REFERENCES `meals` (`id`),
  CONSTRAINT `FK_2B7ED19C64D218E` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations_meals`
--

LOCK TABLES `locations_meals` WRITE;
/*!40000 ALTER TABLE `locations_meals` DISABLE KEYS */;
INSERT INTO `locations_meals` VALUES (1,1),(1,2),(2,1),(2,2);
/*!40000 ALTER TABLE `locations_meals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meals`
--

DROP TABLE IF EXISTS `meals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `price` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meals`
--

LOCK TABLES `meals` WRITE;
/*!40000 ALTER TABLE `meals` DISABLE KEYS */;
INSERT INTO `meals` VALUES (1,'Glazed Salmon','Fresh salmon marinated in basil, garlic, sea salt, and olive oil, grilled and glazed with a sweet flowery honey. Served with a fluffly long grain rice','http://www.dindintonight.co/img/salmon.jpg','12'),(2,'Vegetarian Fettuccine','Fettuccine tossed with celery, garlic, diced tomates in a white wine and asiago cream sauce topped with fresh parsely','http://www.dindintonight.co/img/pasta.jpg','12');
/*!40000 ALTER TABLE `meals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_address`
--

DROP TABLE IF EXISTS `user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_address` (
  `user_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`address_id`),
  KEY `IDX_5543718BA76ED395` (`user_id`),
  KEY `IDX_5543718BF5B7AF75` (`address_id`),
  CONSTRAINT `FK_5543718BF5B7AF75` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE CASCADE,
  CONSTRAINT `FK_5543718BA76ED395` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_address`
--

LOCK TABLES `user_address` WRITE;
/*!40000 ALTER TABLE `user_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `facebookId` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `stripeToken` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `lastName` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `facebookToken` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Allan','1234567890','12345','Bruford','abruford@gmail.com','asdf12345P');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_addresses`
--

DROP TABLE IF EXISTS `users_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_addresses` (
  `user_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`address_id`),
  UNIQUE KEY `UNIQ_9B70FF7F5B7AF75` (`address_id`),
  KEY `IDX_9B70FF7A76ED395` (`user_id`),
  CONSTRAINT `FK_9B70FF7F5B7AF75` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`),
  CONSTRAINT `FK_9B70FF7A76ED395` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_addresses`
--

LOCK TABLES `users_addresses` WRITE;
/*!40000 ALTER TABLE `users_addresses` DISABLE KEYS */;
INSERT INTO `users_addresses` VALUES (1,4),(1,6);
/*!40000 ALTER TABLE `users_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_cards`
--

DROP TABLE IF EXISTS `users_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_cards` (
  `user_id` int(11) NOT NULL,
  `card_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`card_id`),
  UNIQUE KEY `UNIQ_E3B5FCB44ACC9A20` (`card_id`),
  KEY `IDX_E3B5FCB4A76ED395` (`user_id`),
  CONSTRAINT `FK_E3B5FCB44ACC9A20` FOREIGN KEY (`card_id`) REFERENCES `cards` (`id`),
  CONSTRAINT `FK_E3B5FCB4A76ED395` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_cards`
--

LOCK TABLES `users_cards` WRITE;
/*!40000 ALTER TABLE `users_cards` DISABLE KEYS */;
INSERT INTO `users_cards` VALUES (1,1),(1,3);
/*!40000 ALTER TABLE `users_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-26 23:28:31
