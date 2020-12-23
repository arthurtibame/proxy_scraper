SET GLOBAL time_zone = '+8:00';

use Scrapy;

CREATE TABLE IF NOT EXISTS proxy_pool (	
	proxy varchar(99) PRIMARY KEY,
    scheme varchar(5) NULL,
    port INT NUll,
	createtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	modifytime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;