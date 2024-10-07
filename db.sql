CREATE DATABASE productos;

USE productos;

CREATE TABLE Producto(
	id_producto int PRIMARY KEY,
    nombre varchar(50) not null,
    descripcion varchar(100) not null,
    precio decimal(10,2) not null,
    stock int not null
);

CREATE TABLE ProductoElectronico(
	id_producto int PRIMARY KEY,
	garantia int not null,
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE ProductoAlimenticio(
	id_producto int PRIMARY KEY,
	vencimiento date,
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);