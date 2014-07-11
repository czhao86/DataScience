SELECT count(t.docid)
FROM frequency t, frequency s
WHERE t.term='world' AND s.term='transactions' AND t.docid=s.docid;
