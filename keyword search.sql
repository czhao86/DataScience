SELECT sum(s.count)
FROM frequency s
WHERE s.term='washington' OR s.term='taxes' OR s.term='treasury'
GROUP BY s.docid;
