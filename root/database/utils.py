
"""
    Commit
"""
def Commit(engine):
    with engine.connect() as conn:
        conn.commit()