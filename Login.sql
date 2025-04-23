
CREATE TABLE USERS (
USER_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name varchar(30),
last_name VARCHAR(30) NOT NULL,
email VARCHAR(30) NOT NULL,
password VARCHAR(50) NOT NULL 
);

INSERT INTO USERS
VALUES ('1','Amogh', 'Baraar', 'amoghbaraar@gmail.com', 'Amo@password');

TRUNCATE USERS;



 