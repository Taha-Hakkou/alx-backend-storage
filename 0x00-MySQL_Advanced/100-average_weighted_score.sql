-- 100-average_weighted_score.sql
-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE weighted_avg FLOAT;
	SET weighted_avg = (
		SELECT SUM(score * weight) / SUM(weight) FROM users
                JOIN corrections ON users.id = corrections.user_id 
                JOIN projects ON corrections.project_id = projects.id
                WHERE users.id = user_id
	);
	UPDATE users SET average_score = weighted_avg WHERE id = user_id;
END
