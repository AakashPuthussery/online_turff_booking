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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `court` */

insert  into `court`(`court_id`,`court_name`,`place`,`district`,`fee`,`prop_id`,`latitude`,`longtitude`,`contact_no`,`email`,`court_image`,`status`) values (1,'nam_court','chalaa','Alappuzha',500,2,111,111,1114,'namcout@gmail.com','/static/pic/220307-135106.jpg','pending'),(2,'joon_court','aaa','Thrissur',250,2,222,222,222,'jooncourt@gmail.com','/static/pic/220307-135155.jpg','pending'),(4,'jin_court','kochii','Ernakulam',600,3,222,222,777,'jincourt@gmail.com','/static/pic/220307-135401.jpg','pending'),(6,'kim_court','www','Thrissur',600,2,13.0338,77.6755,111,'kim_cout@gmail.com','/static/pic/220307-153552.jpg','pending');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `court_booking` */

insert  into `court_booking`(`booking_id`,`court_id`,`date`,`start_time`,`end_time`,`user_id`,`status`) values (1,1,'2022-03-01','15:00:00','16:00:00',4,'approved'),(2,2,'2022-03-29','14:56:00','18:52:00',8,'pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`utype`) values (1,'admin','admin','admin'),(2,'kimnamjoon@gmail.com','1','prop'),(3,'jin@gmail.com','1','prop'),(4,'junkook@gmail.com','1','user'),(5,'tae@gmail.com','1','user'),(6,'oli@gmail.com','1','rejected'),(7,'jimin@gmail.com','1','user'),(8,'jhope@gmail.com','1','user'),(9,'oliii@gmail.com','1','user'),(10,'namif@gmail.com','n234','prop'),(11,'suga@gmail.com','1','user'),(12,'a@gmail.com','1','rejected'),(13,'aaa@gmail.com','11','user'),(14,'a@gmail.com','1','pending');

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

insert  into `prop`(`login_id`,`prop_name`,`email`,`phone_no`,`image`,`district`) values (2,'kim namjoon','kimnamjoon@gmail.com',111,'/static/pic/220307-125917.jpg','Kannur'),(3,'jin','jin@gmail.com',222,'/static/pic/220307-125956.jpg','Kozhikod'),(10,'Namil','namif@gmail.com',9876543210,'/static/pic/220307-171701.jpg','Pathanamthitta'),(14,'apz','a@gmail.com',22,'/static/pic/220313-100637.jpg','Alappuzha');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `court_id` int(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`rating`,`court_id`,`date`) values (1,4,'Nice keep Going !!!',1,'2022-03-07'),(2,8,'wow',2,'2022-03-07');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `review_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `court_id` varchar(100) NOT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`review_id`,`user_id`,`review`,`date`,`court_id`) values (1,4,'Nice Nice !!!','2022-03-07','1'),(2,8,'wowwww!!!','2022-03-07','1');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tournament` */

insert  into `tournament`(`tournament_id`,`tournament_name`,`court_id`,`no_of_teams`,`start_date`,`entry_fee`,`winning_prize`,`deadline`,`maximum_teams`) values (1,'nam_tournament',1,4,'2022-01-01',500,1000,'2022-02-02',5),(3,'joon_tournament',2,5,'2022-03-23',600,10000,'2022-03-23',5),(4,'aaa',1,3,'2022-03-15',111,10000,'2022-03-31',5);

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tournament_request` */

insert  into `tournament_request`(`tournament_req_id`,`tournament_id`,`user_id`,`team_name`,`logo`,`status`,`req_date`) values (1,1,4,'Golden maknae','/static/pic/220307-135155.jpg','approved','2022-03-07'),(2,1,5,'Super heros','/static/pic/220307-135401.jpg','approved','2022-03-07'),(3,1,7,'Avengers','/static/pic/220307-135155.jpg','approved','2022-03-07'),(4,1,8,'Masters','/static/pic/220307-135401.jpg','approved','2022-03-07'),(5,1,9,'oli','/static/pic/220307-135155.jpg','rejected','2022-03-07'),(6,1,5,'Rockers','/static/pic/220307-135106.jpg','pending','2022-03-07'),(7,1,7,'roro','/static/pic/220307-150526.jpg','approved','2022-03-07');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tournament_schedule` */

insert  into `tournament_schedule`(`tournament_schedule_id`,`tournament_id`,`game_type`,`match_date`,`match_time`,`duration`,`team1`,`team2`,`break`,`winner`) values (1,1,'Semi Finals','2022-03-03','15:00:00','2hr','Golden maknae','Super heros','15min','Golden maknae'),(2,3,'Semi Finals','2022-03-01','16:00:00','3hr','Avengers','Masters','30min','Masters'),(3,1,'Finals','2022-03-10','16:00:00','2hr','Avengers','Masters','15min','Avengers'),(4,3,'Finals','2022-03-10','17:00:00','3hr','Avengers','Masters','30min','Masters'),(5,3,'Finals','2022-03-23','18:42:00','2hr','Avengers','Masters','3','Avengers');

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

insert  into `users`(`login_id`,`user_name`,`phone_no`,`email`,`place`,`profile_pic`,`pin`,`district`) values (4,'junkook',999,'junkook@gmail.com','busan','/static/pic/220307-141434.jpg',111,'Malappuram'),(5,'tae',888,'tae@gmail.com','plce','/static/pic/220307-134439.jpg',88,'Wayanad'),(7,'jimin',111,'jimin@gmail.com','busan','/static/pic/220307-144857.jpg',111,'Palakkad'),(8,'jhop',333,'jhope@gmail.com','12','/static/pic/220307-144933.jpg',11,'Thrissur'),(9,'olilon',11,'oliii@gmail.com','hhh','/static/pic/220307-145010.jpg',33,'Ernakulam'),(11,'suga',222,'suga@gmail.com','ee','/static/pic/220307-172243.jpg',33,'Wayanad'),(13,'qq',122,'aaa@gmail.com','wwq','/static/pic/220308-123053.jpg',11,'Kottayam');

/*Table structure for table `winners_list` */

DROP TABLE IF EXISTS `winners_list`;

CREATE TABLE `winners_list` (
  `winner_id` int(100) NOT NULL AUTO_INCREMENT,
  `tournament_id` int(100) NOT NULL,
  `champions` varchar(100) NOT NULL,
  PRIMARY KEY (`winner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `winners_list` */

insert  into `winners_list`(`winner_id`,`tournament_id`,`champions`) values (1,1,'Avengers'),(2,3,'Avengers');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
