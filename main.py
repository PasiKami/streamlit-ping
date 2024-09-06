import streamlit as st
import time
from sqlalchemy import create_engine

engine1 = st.text_input('输入数据库1地址📝:', key="sql_create_table_name")
engine2 = st.text_input('输入数据库2地址📝:', key="sql_create_table_name2")

if st.button("测试1"):
    start_time = time.time()
    engine = create_engine(engine1)
    with engine.connect() as conn:
        res = conn.execute("select * from test")
        for i in res:
            st.write(i)
    st.write(f"用时: {time.time() - start_time}")
    engine.dispose()

if st.button("测试2"):
    start_time = time.time()
    engine = create_engine(engine2)
    with engine.connect() as conn:
        res = conn.execute("select * from test")
        for i in res:
            st.write(i)
    st.write(f"用时: {time.time() - start_time}")
    engine.dispose()