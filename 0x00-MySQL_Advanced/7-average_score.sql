-- 7-average_score.sql
-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SET avg_score = (SELECT AVG(score) FROM corrections WHERE user_id = users.id);
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END
