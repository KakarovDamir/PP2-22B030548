CREATE OR REPLACE PROCEDURE add_one(contact_name VARCHAR(20), contact_number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT tsis11.number FROM tsis11 WHERE contact_name = tsis11.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE tsis11 SET number = contact_number WHERE tsis11.name = contact_name;
		ELSE
			INSERT INTO tsis11 (name, number) VALUES (contact_name, contact_number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'