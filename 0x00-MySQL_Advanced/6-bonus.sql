-- 6-bonus.sql
-- creates a stored procedure AddBonus that adds a new correction for a student
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)          
BEGIN
	DECLARE project_id INT;
	SET project_id = (SELECT id FROM projects WHERE name = project_name);
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, @project_id, score);
END
