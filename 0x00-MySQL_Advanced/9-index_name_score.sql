-- sql script that creates an INDEX
-- on names table & first letter of name , score

CREATE INDEX idx_name_first_score ON names (name(1), score);
