# Kindle Highlights Viewer

A simple [Streamlit](https://streamlit.io/) web app that lets you explore and filter highlights exported from your Kindle device.

## Features

- **Upload** your Kindle `My Clippings.txt` file directly in the browser.
- **Filter** highlights by book using the sidebar.
- **Toggle columns** (Book Name, Author Name, Highlight, Date) via sidebar checkboxes.
- **Tabular view** of all matching highlights, rendered as an HTML table.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/buzz39/Kindle_Highlighter.git
   cd Kindle_Highlighter
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirement.txt
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

## Usage

1. Connect your Kindle to your computer and locate the `My Clippings.txt` file (usually found in the `documents` folder on the Kindle drive).
2. Click **"Upload a text file"** in the app and select your `My Clippings.txt`.
3. Use the **sidebar** to:
   - Select a book to view its highlights.
   - Show or hide individual columns.
4. The filtered highlights are displayed as a table in the main area.

## Dependencies

| Package     | Purpose                        |
|-------------|--------------------------------|
| `streamlit` | Web application framework      |
| `pandas`    | Data manipulation and display  |

## License

This project is open source. Feel free to use, modify, and distribute it.

---

Built in India with ❤️ by [Gagan Thakur](https://www.twitter.com/hi_gaganthakur)
