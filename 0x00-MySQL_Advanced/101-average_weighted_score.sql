-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers 
-- that computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    JOIN (
        SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS average_weighted_score
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS uw ON u.id = uw.user_id
    SET u.average_score = uw.average_weighted_score;
END //
DELIMITER ;
