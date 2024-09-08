CREATE DATABASE SecurePass;

USE SecurePass;

CREATE TABLE Dados(
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_hora DATETIME,
    alerta VARCHAR(255),
    status_cpu DECIMAL(5,2)
) CHARACTER SET='utf8mb4';
