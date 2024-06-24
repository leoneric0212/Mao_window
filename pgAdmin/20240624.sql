create table student(
	student_id SERIAL Primary Key,
	name VARCHAR(20),
	major VARCHAR(20)
);

create table account(
	username varchar (50) unique not null,
	password varchar (50) Not null,
	email varchar (255) unique not null,
	created_at timestamp not null,
	last_login timestamp
);

insert into student(name, major)
values ('Mao','學生')
