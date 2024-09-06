import streamlit as st
import time
from sqlalchemy import create_engine

engine1 = st.text_input('输入内网数据库地址📝:', key="sql_create_table_name")
engine2 = st.text_input('输入外网数据库地址📝:', key="sql_create_table_name2")

if st.button("测试内网"):
    start_time = time.time()
    engine = create_engine(engine1)
    with engine.connect() as conn:
        res = conn.execute("select * from test")
        for i in res:
            st.write(i)
    st.write(f"用时: {time.time() - start_time}")
    engine.dispose()

if st.button("测试外网"):
    start_time = time.time()
    engine = create_engine(engine2)
    with engine.connect() as conn:
        res = conn.execute("select * from test")
        for i in res:
            st.write(i)
    st.write(f"用时: {time.time() - start_time}")
    engine.dispose()