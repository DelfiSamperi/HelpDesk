<--cada vez que alguien haga update en tickets se actualiza la fecha -->

CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_tickets
BEFORE UPDATE ON ticket
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();