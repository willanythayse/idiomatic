alter session set "_ORACLE_SCRIPT"=true; 

-- Create a new tablespace
CREATE TABLESPACE tbs_idioma
DATAFILE 'C:/app/product/21c/oradata/XE/tbs_idioma.dbf' 
SIZE 100M
AUTOEXTEND ON
NEXT 10M MAXSIZE UNLIMITED;

--drop user IDIOMA;
create user IDIOMA identified by welcome1;
ALTER USER IDIOMA 
DEFAULT TABLESPACE tbs_idioma
QUOTA UNLIMITED ON tbs_idioma;
grant connect, create session, create table, create view, create trigger, create procedure to IDIOMA;


---------------------------------------------------------------------------------------
-- Connect as SYSDBA
CONNECT / AS SYSDBA;

-- Create a new user with admin privileges
CREATE USER IDIOMA IDENTIFIED BY welcome1;

-- Grant DBA role to the new user
GRANT DBA TO IDIOMA;
grant connect, create session, create table, create view, create trigger, create procedure to IDIOMA;

-- Assign default and temporary tablespaces (optional)
ALTER USER IDIOMA DEFAULT TABLESPACE tbs_idioma;
ALTER USER IDIOMA TEMPORARY TABLESPACE temp;
ALTER USER IDIOMA QUOTA UNLIMITED ON USERS;
--ALTER USER IDIOMA QUOTA 100M ON USERS;

ALTER USER IDIOMA DEFAULT TABLESPACE tbs_idioma;
ALTER USER IDIOMA TEMPORARY TABLESPACE temp;
GRANT SELECT ANY TABLE TO IDIOMA;
GRANT INSERT ANY TABLE TO IDIOMA;
GRANT UPDATE ANY TABLE TO IDIOMA;
GRANT DELETE ANY TABLE TO IDIOMA;
GRANT ALTER ANY TABLE TO IDIOMA;
GRANT DROP ANY TABLE TO IDIOMA;


DROP TABLE IDIOMA.languages cascade constraints;
purge recyclebin;
CREATE TABLE IDIOMA.languages(
    id_languages			NUMBER 			GENERATED BY DEFAULT AS IDENTITY,
    languages_abr  			VARCHAR2(255),
    languages      		    VARCHAR2(4000),
    dt_writing   			DATE DEFAULT SYSDATE
)tablespace tbs_idioma;


select LANGUAGES_ABR, length(LANGUAGES) from languages;