CREATE DATABASE budget_Bunny;
USE budgetBunny;

CREATE TABLE users (
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname HASH VARCHAR(255) NOT NULL,
email VARCHAR(266) NOT NULL UNIQUE,
password_hash VARCHAR(255) NOT NULL);

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    id_users INT,
    FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
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
    FOREIGN KEY (id_accounts) REFERENCES accounts(id) ON DELETE CASCADE);

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

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category ENUM('salaire','loyer','alimentation','loisirs','autres') DEFAULT NULL,
);


CREATE TABLE banker(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
password_hash VARCHAR(255) NOT NULL,
id_users INT,
FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE);



INSERT INTO users (name, surname, email, password_hash) 
VALUES 
('Alice', 'Dupont', 'alice.dupont@email.com', 'motdepasse1'),
('John', 'Doe', 'john.doe@email.com', 'motdepasse2'),
('Emma', 'Martin', 'emma.martin@email.com', 'motdepasse3');

INSERT INTO accounts (account_name, balance, id_users) 
VALUES 
('Dupont', 1500.00, 1),
('Doe', 800.00, 2),
('Martin', 3000.00, 3);

INSERT INTO transaction (description, amount, transaction_date, type , id_categories, id_accounts) 
VALUES 
('Achat supermarché', 45.30, '2025-03-18', 'deposit', 'Alimentation', 1, 1),
('Virement salaire', 2000.00, '2025-03-17', 'transfer', 'Revenu', 2, 2),
('Facture internet', 35.99, '2025-03-16', 'withdrawal', 'Abonnements', 3, 3);

INSERT INTO transfers (from_account, to_account, amount, transfert_date) 
VALUES 
(1, 2, 100.00, '2025-02-19'),
(2, 3, 250.00, '2025-01-10'), 
(3, 1, 50.00, '2025-03-12');

INSERT INTO alerts (Message, is_read, id_users, created_at) 
VALUES 
('Votre solde est inférieur à 100€.', FALSE, 1, '2025-10-03'),
('Un virement de 500€ a été reçu.', TRUE, 2, '2025-11-03'),
('Attention : transaction suspecte détectée.', FALSE, 3, '2025-08-01');

INSERT INTO category(category) 
VALUES 
('Alimentation'),
('Revenu'),
('Abonnements'),
('Loisirs'),
('Santé'),
('Éducation');

INSERT INTO banker (name, surname, email, password_hash, id_users)
VALUES
('Sophie', 'Lemoine', 'sophie.lemoine@email.com','coucou' 1),
('Marc', 'Durant', 'marc.durant@email.com', 'zouzou' 2),
('Isabelle', 'Moreau', 'isabelle.moreau@email.com', 'loulou' 3);











