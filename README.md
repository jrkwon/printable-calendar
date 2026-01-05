# Printable Lunar Calendar (인쇄용 음력 달력)

Printable Calendar is a simple, print-friendly web application built with **Flask**. It generates a clean calendar layout optimized for landscape printing, featuring both **Solar** and **Lunar** dates, along with **Korean and US holidays**.

## Key Features

1.  **Print-Optimized Layout**:
    -   Designed for **A4 Landscape** printing.
    -   **One Month Per Page**: Automatically adjusts layout to fit exactly one month per page, even for months with 6 weeks.
    -   Large fonts for easy visibility from a distance.
2.  **Solar & Lunar Dates**:
    -   Displays large Solar dates.
    -   Displays corresponding Lunar dates (using `korean-lunar-calendar`).
3.  **Holiday Support**:
    -   Automatically marks **Korean (KR)** and **US** holidays.
    -   Holidays are displayed in **RED** with their names.
4.  **Flexible Date Selection**:
    -   Select a specific start and end month to print multiple months at once.
    -   **"1년치 설정" (One Year)** button to quickly generate a full 12-month calendar for the current year.

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/printable-calendar.git
cd printable-calendar
```

### 2. Create and Activate Virtual Environment
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
#!/home/jaerock/Documents/workspaces-antigravity/printable-calendar/venv/bin/python3
```

## Usage

1.  **Start the Server**:
    ```bash
    python app.py
    ```
2.  **Open Browser**:
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
3.  **Generate Calendar**:
    -   Select the desired Year/Month range.
    -   Or click **"1년치 설정"** for the full year.
    -   Click **"조회"** (View).
4.  **Print**:
    -   Click the **"인쇄하기"** (Print) button.
    -   **Important Print Settings**:
        -   **Layout**: Landscape (가로 방향)
        -   **Background Graphics**: Enabled (배경 그래픽 포함) - *Required to see holiday colors*.

## Tech Stack
- **Python**: Flask
- **Libraries**: `korean-lunar-calendar`, `holidays`
- **Frontend**: HTML5, CSS3 (Flexbox for dynamic layout)
