"""
Triggers para a tabela lembretes.
Ao criar um lembrete, se ele estiver concluído, um registro é criado.
Ao atualizar um lembrete, se ele estiver concluído, um registro é criado.
"""


from sqlalchemy import DDL, event

from banco.tabelas.lembrete import Lembrete

function_adicionar_registro = DDL(
    """
    CREATE FUNCTION adicionar_registro()
    RETURNS TRIGGER AS $$
    BEGIN
        IF NEW.concluido = TRUE THEN
            INSERT INTO registros (id, titulo, data, observacoes) VALUES (gen_random_uuid(), NEW.titulo, CURRENT_DATE, '');
        END IF;
        RETURN NEW;
    END; $$ LANGUAGE PLPGSQL;
"""
)


trigger_lembrete_criado = DDL(
    """
    CREATE TRIGGER adicionar_registro_criado
    AFTER INSERT ON lembretes
    FOR EACH ROW
    EXECUTE PROCEDURE adicionar_registro();
"""
)


trigger_lembrete_atualizado = DDL(
    """
    CREATE TRIGGER adicionar_registro_atualizado
    AFTER UPDATE ON lembretes
    FOR EACH ROW
    WHEN (OLD.concluido = FALSE AND NEW.concluido = TRUE)
    EXECUTE PROCEDURE adicionar_registro();
"""
)

event.listen(
    Lembrete.__table__,
    "after_create",
    function_adicionar_registro.execute_if(dialect="postgresql"),
)

event.listen(
    Lembrete.__table__,
    "after_create",
    trigger_lembrete_criado.execute_if(dialect="postgresql"),
)

event.listen(
    Lembrete.__table__,
    "after_create",
    trigger_lembrete_atualizado.execute_if(dialect="postgresql"),
)
