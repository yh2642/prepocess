CREATE TABLE company_checker
(memberid CHAR(22) NOT NULL PRIMARY KEY,
qualitylevel TINYINT)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司库';

INSERT company_checker SELECT memberid, avg(qualitylevel) FROM offer_info GROUP BY memberid;



CREATE TABLE company_stat
(memberid CHAR(22) NOT NULL,
category CHAR(9) NOT NULL,
C_index FLOAT NOT NULL,
PRIMARY KEY (memberid, category)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司产品构成指数';




CREATE TABLE company_model
(offerId CHAR(12) NOT NULL PRIMARY KEY,
type CHAR(4) NOT NULL,
memberid VARCHAR(22) NOT NULL,
subject VARCHAR(100),
category CHAR(9) NOT NULL,
company VARCHAR(50) NOT NULL,
sale mediumint,
status VARCHAR(20),
qualitylevel TINYINT)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='产品信息';







CREATE TABLE company_production
(companyId CHAR(10) NOT NULL PRIMARY KEY,
 factory_size CHAR(15),
 employees_count VARCHAR(15),
 rnd_staff_num VARCHAR(10),
 brand_name VARCHAR(20),
 production_capacity VARCHAR(20))ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司生产信息';

 CREATE TABLE company_basic
(companyId CHAR(10) NOT NULL PRIMARY KEY,
 memberId VARCHAR(50) NOT NULL,
 company_name VARCHAR(50) NOT NULL,
 company_name_en VARCHAR(50),
 homepageurl VARCHAR(100),
 bizplace VARCHAR(20),
 bizmodel VARCHAR(20),
 main_category VARCHAR(20),
 production_service VARCHAR(300),
 legal_status VARCHAR(20),
 profile BLOB,
 reg_capital VARCHAR(20))ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司基本信息';

 CREATE TABLE company_business
(companyId CHAR(10) NOT NULL PRIMARY KEY,
 bank CHAR(20),
 account VARCHAR(30),
 annual_revenue VARCHAR(25),
 annual_import VARCHAR(25),
 annual_export VARCHAR(25))ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司营业信息';


 CREATE TABLE company_cert
(companyId CHAR(10) NOT NULL PRIMARY KEY,
 established_year SMALLINT,
 founded_place VARCHAR(20),
 principal VARCHAR(20),
 certification VARCHAR(20),
 qaQc VARCHAR(20),
 trade_region VARCHAR(50),
 key_clients VARCHAR(200),
 oemOdm VARCHAR(20))ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司资质';