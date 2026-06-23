import streamlit as st
#streamlit run week10/myWebApp.py

if "todo_list" not in st.session_state:
    st.session_state.todo_list = ["Grocery Shopping", "Cook", "Presentation"]


def update_todo():
    if user_input != "":
        st.session_state.todo_list.append(user_input)

st.set_page_config(
    page_title="To_do_list",
    page_icon=":)"
)

st.title("To do list")
st.write("------")

container = st.container(border=False, gap="medium", horizontal=True, vertical_alignment="bottom")
with container:
    user_input = st.text_input(label="Add sth to your to do list")
    st.button("+ Add to list", on_click=update_todo)

for i in range(len(st.session_state.todo_list)):
    st.checkbox(st.session_state.todo_list[i], key=i)