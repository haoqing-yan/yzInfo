CREATE TABLE `majors`
(
    `majors`           varchar(16) DEFAULT NULL COMMENT '专业大类',
    `majorCode`        varchar(8)  DEFAULT NULL COMMENT '专业大类代码',
    `subjectMajor`     varchar(16) DEFAULT NULL COMMENT '细分专业名',
    `subjectMajorCode` char(4) COMMENT '细分专业代码',
    `createTime`       varchar(12) DEFAULT NULL COMMENT '创建时间',
    `updateTime`       varchar(12) DEFAULT NULL COMMENT '修改时间',
    PRIMARY KEY (`subjectMajorCode`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `universities`
(
    `id`            char(19) COMMENT 'id',
    `name`          varchar(24) DEFAULT NULL COMMENT '招生单位',
    `location`      varchar(10) DEFAULT NULL COMMENT '所在地',
    `faculty`       varchar(32) DEFAULT NULL COMMENT '院系所',
    `major`         varchar(64) DEFAULT NULL COMMENT '专业',
    `research`      varchar(64) DEFAULT NULL COMMENT '研究方向',
    `type`          varchar(10) DEFAULT NULL COMMENT '学习方式',
    `studentNumber` varchar(10) DEFAULT NULL COMMENT '招生人数',
    `comment`       varchar(80) DEFAULT NULL COMMENT '备注',
    `createTime`    varchar(12) DEFAULT NULL COMMENT '创建时间',
    `updateTime`    varchar(12) DEFAULT NULL COMMENT '修改时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `exam`
(
    `id`                   varchar(19) COMMENT 'id',
    `name`                 varchar(24) DEFAULT NULL COMMENT '招生单位',
    `politics`             varchar(20) DEFAULT NULL COMMENT '政治',
    `foreignLanguage`      varchar(20) DEFAULT NULL COMMENT '外语',
    `professionalSubject1` varchar(20) DEFAULT NULL COMMENT '业务课1',
    `professionalSubject2` varchar(20) DEFAULT NULL COMMENT '业务课2',
    `createTime`           varchar(12) DEFAULT NULL COMMENT '创建时间',
    `updateTime`           varchar(12) DEFAULT NULL COMMENT '修改时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

