CREATE OR REPLACE PROCEDURE delete_data(data_to_delete VARCHAR(20))
	AS $$	
	BEGIN
	DELETE FROM tsis11 WHERE name = data_to_delete OR number = data_to_delete;
	END; $$
	LANGUAGE plpgsql