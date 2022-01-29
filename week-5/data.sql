create database `website`;
show databases;
use `website`;

create table `member`(
`id` bigint primary key AUTO_INCREMENT, 
`name` varchar(255) NOT NULL,
`username` varchar(255) NOT NULL,
`password` varchar(255) NOT NULL,
`follower_count` int NOT NULL DEFAULT 0,
`time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

describe `member`;

INSERT INTO `member`(`id`,`name`,`username`,`password`) VALUES(1,'柯南','test','test');
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES('RJ','u2','p2',20);
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES('IU','u3','p3',100);
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES('允兒','u4','p4',90);
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES('夜神月','u5','p5',30);

SELECT * FROM `member`WHERE `username`='test' AND `password`='test' ORDER BY `time` DESC LIMIT 1,3;


UPDATE `website`.`member` SET `name` = 'test2' WHERE (`name` = '柯南');
SET SQL_SAFE_UPDATES=0;
SELECT * FROM `member`;
SELECT COUNT(*) FROM `member`;
SELECT SUM(`follower_count`) as 總和 FROM `member`;
SELECT AVG(`follower_count`) as 平均 FROM `member`;

create table `message`(
	`id` bigint primary key AUTO_INCREMENT, 
	`member_id` bigint,foreign key(`member_id`) references`member`(`id`) on delete set null,
	`content` varchar(255) NOT NULL,
    `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

describe `message`;
SELECT * FROM`message`;
INSERT INTO `message`(`id`,`member_id`,`content`) VALUES(1,1,'彭彭好帥');
INSERT INTO `message`(`member_id`,`content`) VALUES(3,'我是韓國歌手');
INSERT INTO `message`(`member_id`,`content`) VALUES(4,'我是少女時代');

SELECT `name`,`username`,`content`FROM `member` JOIN `message`ON `website`.`member`.`id`=`website`.`message`.`member_id`WHERE `username` = 'test';


