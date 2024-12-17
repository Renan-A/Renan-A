import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Verificando as migrações aplicadas
cursor.execute("SELECT app, name FROM django_migrations")
migrations = cursor.fetchall()
print("Migrações aplicadas:")
for migration in migrations:
    print(migration)

# Remover migração problemática (exemplo: 'meuapp.0001_initial')
cursor.execute("DELETE FROM django_migrations WHERE app='meuapp' AND name='0001_initial'")
conn.commit()

print("Migração removida.")

# Fechando a conexão
conn.close()

print("Banco de dados corrigido.")
