SELECT sum(s.count*t.count)
FROM frequency s, frequency t
WHERE s.term=t.term AND s.docid='10080_txt_crude' AND t.docid='17035_txt_earn';
