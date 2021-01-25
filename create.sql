CREATE TABLE `majors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `majors` varchar(16) DEFAULT NULL COMMENT '专业大类',
  `majorCode` varchar(8) DEFAULT NULL COMMENT '专业大类代码',
  `subjectMajor` varchar(16) DEFAULT NULL COMMENT '细分专业名',
  `subjectMajorCode` varchar(8) DEFAULT NULL COMMENT '细分专业代码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;