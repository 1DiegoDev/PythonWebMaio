-- feito para criar tablea ou banco de dados
-- NOT EXISTS é pra criar um bd se não já existir
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo string NOT NULL,
    texto string NOT NULL,
    data_criacao DATETIME default CURRENT_TIMESTAMP
)






