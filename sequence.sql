CREATE TABLE movies (
url text, 
title text, 
releaseDate text,
Distributor text,
Starring text,
Summary text,
Director text,
Genre text,
Rating text,
Runtime text,
Userscore text,
Metascore text,
scoreCounts text
);

\copy movies FROM '/home/pi/RSL/moviesFromMetacritic.csv' delimiter ';' header;

ALTER TABLE movies ADD lexemesSummary tsvector;
ALTER TABLE movies ADD lexemesTitle tsvector;
ALTER TABLE movies ADD lexemesStarring tsvector;

UPDATE movies SET lexemesSummary = to_tsvector(Summary);
UPDATE movies SET lexemesTitle = to_tsvector(title);
UPDATE movies SET lexemesStarring = to_tsvector(Starring);

SELECT url FROM movies WHERE lexemesSummary @@ to_tsquery('pirate');
SELECT url FROM movies WHERE lexemesSummary @@ to_tsquery('space');
SELECT url FROM movies WHERE lexemesTitle @@ to_tsquery('stellar');
SELECT url FROM movies WHERE lexemesStarring @@ to_tsquery('dicaprio');

ALTER TABLE movies ADD rank float4;

UPDATE movies SET RANK = ts_rank(lexemesStarring, plainto_tsquery((SELECT Starring FROM movies WHERE url='i-am-legend') ));
DROP TABLE recommendationsBasedOnStarringField;
CREATE Table recommendationsBasedOnStarringField AS SELECT url, rank FROM movies WHERE rank > 0.02 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/i-am-legend.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesStarring, plainto_tsquery((SELECT Starring FROM movies WHERE url='the-wolf-of-wall-street') ));
DROP TABLE recommendationsBasedOnStarringField;
CREATE Table recommendationsBasedOnStarringField AS SELECT url, rank FROM movies WHERE rank > 0.02 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/wolf-of-wallstreet.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesStarring, plainto_tsquery((SELECT Starring FROM movies WHERE url='interstellar') ));
DROP TABLE recommendationsBasedOnStarringField;
CREATE Table recommendationsBasedOnStarringField AS SELECT url, rank FROM movies WHERE rank > 0.1 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/interstellar.csv' WITH csv;


UPDATE movies SET RANK = ts_rank(lexemesSummarry, plainto_tsquery((SELECT Summary FROM movies WHERE url='i-am-legend') ));
DROP TABLE recommendationsBasedOnSummaryField;
CREATE Table recommendationsBasedOnSummaryField AS SELECT url, rank FROM movies WHERE rank > 0.2 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnSummarySummaryField) to '/home/pi/RSL/Summary/i-am-legend.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesSummary, plainto_tsquery((SELECT Summary FROM movies WHERE url='the-wolf-of-wall-street') ));
DROP TABLE recommendationsBasedOnSummaryField;
CREATE Table recommendationsBasedOnSummaryField AS SELECT url, rank FROM movies WHERE rank > 0.2 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/wolf-of-wallstreet.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesStarring, plainto_tsquery((SELECT Starring FROM movies WHERE url='interstellar') ));
DROP TABLE recommendationsBasedOnStarringField;
CREATE Table recommendationsBasedOnStarringField AS SELECT url, rank FROM movies WHERE rank > 0.2 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/interstellar.csv' WITH csv;


UPDATE movies SET RANK = ts_rank(lexemesSummarry, plainto_tsquery((SELECT Summary FROM movies WHERE url='i-am-legend') ));
DROP TABLE recommendationsBasedOnSummaryField;
CREATE Table recommendationsBasedOnSummaryField AS SELECT url, rank FROM movies WHERE rank > 0.001 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnSummarySummaryField) to '/home/pi/RSL/Summary/i-am-legend.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesSummary, plainto_tsquery((SELECT Summary FROM movies WHERE url='the-wolf-of-wall-street') ));
DROP TABLE recommendationsBasedOnSummaryField;
CREATE Table recommendationsBasedOnSummaryField AS SELECT url, rank FROM movies WHERE rank > 0.1 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/wolf-of-wallstreet.csv' WITH csv;

UPDATE movies SET RANK = ts_rank(lexemesStarring, plainto_tsquery((SELECT Starring FROM movies WHERE url='interstellar') ));
DROP TABLE recommendationsBasedOnStarringField;
CREATE Table recommendationsBasedOnStarringField AS SELECT url, rank FROM movies WHERE rank > 0.01 ORDER BY rank DESC LIMIT 50;
\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/starring/interstellar.csv' WITH csv;
