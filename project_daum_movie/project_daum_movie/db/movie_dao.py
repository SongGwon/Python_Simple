from db.common.connection import connection

# 리뷰 저장


def add_review(data):
    # 1.Connection
    conn = connection()

    try:
        # 2.일꾼 생성
        curs = conn.cursor()
        # 3.JOB 생성(SQL) -> INSERT, UPDATE, SELECT, DELETE
        sql = """
                INSERT INTO tbl_review(title, review, score, writer, reg_date)
                VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s) 
              """
        # 4.작업 시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        # 5.자원 해제
        conn.close()













