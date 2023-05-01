CREATE OR REPLACE FUNCTION query_all(query_mode INT, query_value VARCHAR(20))
    RETURNS TABLE(name VARCHAR(20), number VARCHAR(20))
	AS $$ BEGIN
        IF query_mode = 1 THEN
            RETURN QUERY
				SELECT tsis11.name, tsis11.number FROM tsis11 WHERE
				tsis11.name = query_value OR tsis11.number = query_value;
				
        ELSIF query_mode = 2 THEN
            RETURN QUERY
				(SELECT tsis11.name, tsis11.number FROM tsis11 WHERE
				 starts_with(tsis11.name, query_value) OR  starts_with(tsis11.number, query_value));
				
        ELSIF query_mode = 3 THEN
			RETURN QUERY
				SELECT tsis11.name, tsis11.number FROM tsis11 WHERE 
				tsis11.name ILIKE '%' || query_value || '%' OR tsis11.number ILIKE '%' || query_value || '%';
				
		ELSE
			RAISE EXCEPTION 'WRONG QUERY MODE';
			
        END IF;
		
    END; $$
	LANGUAGE plpgsql