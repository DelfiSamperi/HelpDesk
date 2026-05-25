-- aca van los datos que quiero ingresar en mi base de datos

-- limpiar tablas al ejecutar varias veces
TRUNCATE comments, ticket_history, ticket, users, categories RESTART IDENTITY CASCADE;

--categorias
INSERT INTO categories (category_name) VALUES
('Hardware'), ('Software'), ('Red');

--usuarios
INSERT INTO users (id, user_name, email, password_hash, user_role) VALUES
('11111111-1111-1111-1111-111111111111', 'Admin', 'admin@test.com', 'hash', 'admin'),
('22222222-2222-2222-2222-222222222222', 'Tecnico', 'tech@test.com', 'hash', 'tech'),
('3cccc33c-cc3c-3333-3cc3-cccc33333333', 'Usuario', 'user@test.com', 'hash', 'user');

--tickets
INSERT INTO ticket (title, description, created_by, category_id) VALUES
('No funciona la impresora','No imprime','3cccc33c-cc3c-3333-3cc3-cccc33333333',1),
('No conecta a internet', 'Al intentar conectarme dice que hay un problema de red','3cccc33c-cc3c-3333-3cc3-cccc33333333',3);

