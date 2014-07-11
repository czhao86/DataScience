SELECT sum(A.value*B.value)
FROM A, B
WHERE A.col_num=B.row_num
GROUP BY A.row_num, B.col_num
HAVING A.row_num=2 AND B.col_num=3;
