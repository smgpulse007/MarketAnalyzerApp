import streamlit as st
# Import pages as modules
from pages import options_and_dark_pool, stocks_with_sma

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Options and Dark Pool", "Stocks with SMA"])

    if page == "Options and Dark Pool":
        options_and_dark_pool.show()
    elif page == "Stocks with SMA":
        stocks_with_sma.show()

if __name__ == "__main__":
    main()
