CREATE DATABASE budget_buddy;
USE budget_buddy;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    id_users INT,
    FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category ENUM('salaire','loyer','alimentation','loisirs','autres') DEFAULT NULL,
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
    id_category INT,
    id_accounts INT,
    FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE SET NULL,
    FOREIGN KEY (id_accounts) REFERENCES accounts(id) ON DELETE CASCADE
);

CREATE TABLE transfers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_account INT NOT NULL,
    to_account INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transfer_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account) REFERENCES accounts(id) ON DELETE CASCADE,
    FOREIGN KEY (to_account) REFERENCES accounts(id) ON DELETE CASCADE
);

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    id_users INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
);
