-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT) 
BEGIN
	DECLARE total_score FLOAT DEFAULT 0;
	DECLARE total_weight FLOAT DEFAULT 0;

	SELECT SUM(corrections.score * projects.weight), SUM(projects.weight) INTO total_score, total_weight FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id;

	if total_weight > 0 THEN
		UPDATE users SET average_score = total_score / total_weight WHERE users.id = user_id;
	ELSE
		UPDATE users SET average_score = 0 WHERE users.id = user_id;
	END IF;
END $$

DELIMITER ;
