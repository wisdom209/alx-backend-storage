-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
BEGIN
	UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) 
END;$$
DELIMITER ;
