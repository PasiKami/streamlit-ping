import streamlit as st
from ping3 import ping

def main():
    st.title("Ping 工具")
    st.write("请输入一个地址来查看平均延迟。")

    address = st.text_input("地址", "google.com")
    num_pings = st.number_input("发送 ping 的次数", min_value=1, value=4)

    if st.button("开始 Ping"):
        if address:
            total_time = 0
            valid_pings = 0

            for i in range(num_pings):
                try:
                    response_time = ping(address)
                    if response_time is not None:
                        total_time += response_time
                        valid_pings += 1
                except Exception as e:
                    st.error(f"Ping 错误: {str(e)}")
                    response_time = None

                st.write(f"第 {i+1} 次 ping: {response_time} 秒")

            if valid_pings > 0:
                average_time = total_time / valid_pings
                st.success(f"平均延迟为: {average_time} 秒")
            else:
                st.warning("没有有效的 ping 响应得到。")
        else:
            st.error("请提供一个有效的地址")

if __name__ == "__main__":
    main()
