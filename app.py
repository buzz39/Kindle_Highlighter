import streamlit as st
import pandas as pd
from datetime import datetime

def display_table(highlights_data):
    for highlight in highlights_data:
        st.text(f'"{highlight["Highlight"]} | {highlight["Date"]}"\t"{highlight["Book Name"]}({highlight["Author Name"]}){highlight["Highlight"]}"\t{highlight["Date"]}')

def display_list(data):
    st.text("Structured Data:")
    for item in data:
        st.text(f"- {item}")

def display_dataframe(data):
    df = pd.DataFrame(data, columns=["Book Name", "Author Name", "Highlight", "Date"])
    st.dataframe(df)

def main():
    st.title("Kindle Highlights Viewer")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        content = uploaded_file.getvalue().decode("utf-8")
        lines = content.splitlines()

        highlights_data = []
        current_highlight = {"Book Name": "", "Author Name": "", "Highlight": "", "Date": ""}

        for line in lines:
            if line.strip() == "==========":
                if current_highlight["Book Name"] and current_highlight["Highlight"]:
                    highlights_data.append(current_highlight)
                current_highlight = {"Book Name": "", "Author Name": "", "Highlight": "", "Date": ""}
            elif "Your Highlight at location" in line or "Your Note at location" in line:
                date_string = line.split("|")[-1].strip().replace("Added on ", "")
                date_object = datetime.strptime(date_string, "%A, %d %B %Y %H:%M:%S")
                current_highlight["Date"] = date_object.strftime("%d-%m-%Y %H:%M:%S")
            elif "(" in line and ")" in line:
                book_author_info = line.split("(")
                current_highlight["Book Name"] = book_author_info[0].strip()
                current_highlight["Author Name"] = book_author_info[1].replace(")", "").strip()
            else:
                current_highlight["Highlight"] = line.strip()

        # Get a list of unique book names
        book_names = list(set([highlight["Book Name"] for highlight in highlights_data]))

        # Add a radio button in the sidebar to filter books
        selected_book = st.sidebar.radio("Select a book:", book_names)

        # Filter the highlights data based on the selected book
        filtered_highlights_data = [highlight for highlight in highlights_data if highlight["Book Name"] == selected_book]

        # Add checkboxes in the sidebar to hide columns
        show_book_name = st.sidebar.checkbox("Show Book Name", value=True)
        show_author_name = st.sidebar.checkbox("Show Author Name", value=True)
        show_highlight = st.sidebar.checkbox("Show Highlight", value=True)
        show_date = st.sidebar.checkbox("Show Date", value=True)

        # Filter the columns based on the checkboxes
        columns_to_show = []
        if show_book_name:
            columns_to_show.append("Book Name")
        if show_author_name:
            columns_to_show.append("Author Name")
        if show_highlight:
            columns_to_show.append("Highlight")
        if show_date:
            columns_to_show.append("Date")

        df = pd.DataFrame(filtered_highlights_data)
        #st.dataframe(df[columns_to_show])
        df_html = df[columns_to_show].to_html(index=False)

        st.markdown(df_html, unsafe_allow_html=True)

        st.sidebar.markdown(
            """
            <footer style="width: 100%; text-align: center; padding: 1rem 0;">
                Built in India with <span style="color: red;">&hearts;</span> by <a href="https://www.twitter.com/hi_gaganthakur" target="_blank">Gagan Thakur</a>
            </footer>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
