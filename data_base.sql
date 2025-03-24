CREATE DATABASE budget_buddy;
USE budget_buddy;

-- Table des utilisateurs
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- Table des comptes bancaires
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_name ENUM('courant', 'épargne', 'joint', 'entreprise') NOT NULL,
    iban VARCHAR(34) NOT NULL UNIQUE,  
    balance DECIMAL(10,2) DEFAULT 0.00 NOT NULL,
    id_users INT NOT NULL,
    FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
);


-- Table des catégories de transactions
CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category ENUM('salaire','loyer','alimentation','loisirs','autres') NOT NULL DEFAULT 'autres'
);

-- Table des transactions financières
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0), -- Assurer que le montant est positif
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    type ENUM('deposit', 'withdrawal') NOT NULL, -- Exclusion des transferts ici
    id_category INT,
    id_accounts INT NOT NULL,
    FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE SET NULL,
    FOREIGN KEY (id_accounts) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Table des transferts d'argent entre comptes
CREATE TABLE transfers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_account INT NOT NULL,
    to_account INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0), -- Assurer que le montant est positif
    transfer_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account) REFERENCES accounts(id) ON DELETE CASCADE,
    FOREIGN KEY (to_account) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Table des alertes utilisateurs
CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    id_users INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
);
