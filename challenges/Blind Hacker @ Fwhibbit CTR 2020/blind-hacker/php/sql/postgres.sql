CREATE DATABASE blindhackerdb;

\c blindhackerdb;

CREATE TABLE userinfo( 
	id serial PRIMARY KEY,
	username VARCHAR (50) UNIQUE NOT NULL,
	password VARCHAR (50) NOT NULL,
	email VARCHAR (355) UNIQUE NOT NULL,
	is_admin VARCHAR (500) NOT NULL
);

CREATE USER readuser WITH ENCRYPTED PASSWORD 'readuserpassword';
GRANT CONNECT ON DATABASE blindhackerdb TO readuser;
GRANT SELECT ON userinfo TO readuser;
GRANT SELECT ON information_schema.tables TO readuser;
GRANT SELECT ON information_schema.columns TO readuser;
GRANT SELECT ON pg_database TO readuser;

INSERT INTO userinfo (username, email, password, is_admin) VALUES ('betauser','p0stgr3s_1s_c00l3r_','letsputsomepwd!', 'no');
INSERT INTO userinfo (username, email, password, is_admin) VALUES ('auser','i@told.u','you4recrazy', '&_y0u_r0ck}');
INSERT INTO userinfo (username, email, password, is_admin) VALUES ('administrator','admin@domain.admin','admin_password', 'yes');
INSERT INTO userinfo (username, email, password, is_admin) VALUES ('guest','guest@where.ever','h4x0r', 'no');
