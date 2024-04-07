/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - turf booking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`turf booking` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `turf booking`;

/*Table structure for table `court` */

DROP TABLE IF EXISTS `court`;

CREATE TABLE `court` (
  `court_id` int(100) NOT NULL AUTO_INCREMENT,
  `court_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `fee` int(100) DEFAULT NULL,
  `prop_id` int(100) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longtitude` float DEFAULT NULL,
  `contact_no` int(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `court_image` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`court_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `court` */

insert  into `court`(`court_id`,`court_name`,`place`,`district`,`fee`,`prop_id`,`latitude`,`longtitude`,`contact_no`,`email`,`court_image`,`status`) values (1,'Real Arena','kannur','Kannur',899,1,9.93218,76.2666,2147483647,'realarena@gmail.com','/static/pic/220314-143023.jpg','pending'),(2,'soccer arena','koothparamba','Kasaragod',1200,1,9.92092,76.2749,789568965,'soccerarena@gmail.com','/static/pic/220314-143155.jpg','pending');

/*Table structure for table `court booking` */

DROP TABLE IF EXISTS `court booking`;

CREATE TABLE `court booking` (
  `booking_id` int(100) NOT NULL AUTO_INCREMENT,
  `court_id` int(100) NOT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `booking_fee` int(100) NOT NULL,
  `user_id` int(100) NOT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `court booking` */

/*Table structure for table `court request` */

DROP TABLE IF EXISTS `court request`;

CREATE TABLE `court request` (
  `req_id` int(100) NOT NULL AUTO_INCREMENT,
  `court_id` int(100) NOT NULL,
  `user_id` int(100) NOT NULL,
  `time` time NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `prop_id` int(100) NOT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `court request` */

/*Table structure for table `court_booking` */

DROP TABLE IF EXISTS `court_booking`;

CREATE TABLE `court_booking` (
  `booking_id` int(100) NOT NULL AUTO_INCREMENT,
  `court_id` int(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `user_id` int(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `court_booking` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`utype`) values (1,'kannan@gmail.com','1','prop'),(2,'suresh@gmail.com','2','pending'),(3,'admin','admin','admin'),(4,'abc','abc','user');

/*Table structure for table `prop` */

DROP TABLE IF EXISTS `prop`;

CREATE TABLE `prop` (
  `login_id` int(100) DEFAULT NULL,
  `prop_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_no` bigint(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `prop` */

insert  into `prop`(`login_id`,`prop_name`,`email`,`phone_no`,`image`,`district`) values (1,'kannan kk','kannan@gmail.com',7845129632,'/static/pic/220314-141955.jpg','Kollam'),(2,'suresh m','suresh@gmail.com',9856241375,'/static/pic/220314-142113.jpg','Malappuram');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `court_id` int(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`rating`,`court_id`,`date`) values (1,1,'5',1,'0000-00-00');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `court_id` varchar(100) NOT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`user_id`,`review`,`date`,`court_id`) values (1,4,'good','0000-00-00','1');

/*Table structure for table `status` */

DROP TABLE IF EXISTS `status`;

CREATE TABLE `status` (
  `court_id` int(100) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `status` */

/*Table structure for table `tournament` */

DROP TABLE IF EXISTS `tournament`;

CREATE TABLE `tournament` (
  `tournament_id` int(100) NOT NULL AUTO_INCREMENT,
  `tournament_name` varchar(100) DEFAULT NULL,
  `court_id` int(100) DEFAULT NULL,
  `no_of_teams` int(100) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `entry_fee` int(100) DEFAULT NULL,
  `winning_prize` int(100) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `maximum_teams` int(100) DEFAULT NULL,
  PRIMARY KEY (`tournament_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tournament` */

insert  into `tournament`(`tournament_id`,`tournament_name`,`court_id`,`no_of_teams`,`start_date`,`entry_fee`,`winning_prize`,`deadline`,`maximum_teams`) values (1,'7s tournament',1,8,'2022-03-02',1000,10000,'2022-03-31',10);

/*Table structure for table `tournament_request` */

DROP TABLE IF EXISTS `tournament_request`;

CREATE TABLE `tournament_request` (
  `tournament_req_id` int(100) NOT NULL AUTO_INCREMENT,
  `tournament_id` int(100) NOT NULL,
  `user_id` int(100) NOT NULL,
  `team_name` varchar(100) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `req_date` date NOT NULL,
  PRIMARY KEY (`tournament_req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tournament_request` */

insert  into `tournament_request`(`tournament_req_id`,`tournament_id`,`user_id`,`team_name`,`logo`,`status`,`req_date`) values (1,1,4,'warriors','r','approved','0000-00-00');

/*Table structure for table `tournament_schedule` */

DROP TABLE IF EXISTS `tournament_schedule`;

CREATE TABLE `tournament_schedule` (
  `tournament_schedule_id` int(100) NOT NULL AUTO_INCREMENT,
  `tournament_id` int(100) NOT NULL,
  `game_type` varchar(100) NOT NULL,
  `match_date` date NOT NULL,
  `match_time` time NOT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `team1` varchar(100) DEFAULT NULL,
  `team2` varchar(100) DEFAULT NULL,
  `break` varchar(100) DEFAULT NULL,
  `winner` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tournament_schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tournament_schedule` */

insert  into `tournament_schedule`(`tournament_schedule_id`,`tournament_id`,`game_type`,`match_date`,`match_time`,`duration`,`team1`,`team2`,`break`,`winner`) values (1,1,'Semi Finals','2022-03-20','10:20:00','45min','warriors','warriors','5min','Team 1');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `login_id` int(100) DEFAULT NULL,
  `user_name` varchar(100) NOT NULL,
  `phone_no` bigint(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `pin` int(100) NOT NULL,
  `district` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`login_id`,`user_name`,`phone_no`,`email`,`place`,`profile_pic`,`pin`,`district`) values (4,'ser',987,'seer@gmail.com','kannu','e',89,'ed');

/*Table structure for table `winners_list` */

DROP TABLE IF EXISTS `winners_list`;

CREATE TABLE `winners_list` (
  `winner_id` int(100) NOT NULL AUTO_INCREMENT,
  `tournament_id` int(100) NOT NULL,
  `champions` varchar(100) NOT NULL,
  PRIMARY KEY (`winner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `winners_list` */

insert  into `winners_list`(`winner_id`,`tournament_id`,`champions`) values (1,1,'team1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
