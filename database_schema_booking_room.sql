CREATE DATABASE booking_room_sql
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE booking_room_sql;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE booking (
  booking_id int(11) NOT NULL AUTO_INCREMENT,
  booking_date timestamp NOT NULL DEFAULT current_timestamp(),
  user_id int(11) DEFAULT NULL,
  user_department varchar(255) DEFAULT NULL,
  booker_name varchar(255) DEFAULT NULL,
  phone_number varchar(20) DEFAULT NULL,
  room_id int(11) DEFAULT NULL,
  desired_date date DEFAULT NULL,
  start_time time DEFAULT NULL,
  end_time time DEFAULT NULL,
  booking_verify enum('Pending','Approved','Rejected') DEFAULT 'Pending',
  PRIMARY KEY (booking_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE booking_equipment (
  id_booking_equipment int(11) NOT NULL AUTO_INCREMENT,
  booking_id int(11) DEFAULT NULL,
  equipment_id int(11) DEFAULT NULL,
  PRIMARY KEY (id_booking_equipment),
  KEY booking_id (booking_id),
  KEY equipment_id (equipment_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE cancelled_booking (
  cancelled_id int(11) NOT NULL AUTO_INCREMENT,
  booking_date datetime NOT NULL,
  user_id int(11) NOT NULL,
  user_department varchar(255) NOT NULL,
  room_id int(11) NOT NULL,
  desired_date date NOT NULL,
  start_time time NOT NULL,
  end_time time NOT NULL,
  cancelled_by int(11) NOT NULL,
  cancelled_at datetime NOT NULL,
  PRIMARY KEY (cancelled_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE room (
  room_id int(11) NOT NULL AUTO_INCREMENT,
  room_name varchar(255) NOT NULL,
  room_detail text DEFAULT NULL,
  room_status varchar(50) DEFAULT NULL,
  PRIMARY KEY (room_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE equipment (
  equipment_id int(11) NOT NULL AUTO_INCREMENT,
  room_id int(11) DEFAULT NULL,
  equipment_name varchar(255) NOT NULL,
  PRIMARY KEY (equipment_id),
  KEY room_id (room_id),
  CONSTRAINT fk_equipment_room
    FOREIGN KEY (room_id) REFERENCES room(room_id)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE members (
  user_id int(24) NOT NULL AUTO_INCREMENT,
  user_username varchar(255) DEFAULT NULL,
  user_password varchar(255) DEFAULT NULL,
  user_firstname varchar(255) DEFAULT NULL,
  user_lastname varchar(255) DEFAULT NULL,
  user_tel varchar(10) DEFAULT NULL,
  user_status varchar(50) DEFAULT NULL,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE users (
  user_id int(11) NOT NULL AUTO_INCREMENT,
  user_username varchar(50) NOT NULL,
  user_password varchar(255) NOT NULL,
  user_department varchar(50) DEFAULT NULL,
  user_status varchar(20) DEFAULT NULL,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE booking_equipment
  ADD CONSTRAINT fk_booking_equipment_booking
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
    ON DELETE CASCADE,
  ADD CONSTRAINT fk_booking_equipment_equipment
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id);

COMMIT;
