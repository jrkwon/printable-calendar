from flask import Flask, render_template, request
import calendar
from korean_lunar_calendar import KoreanLunarCalendar
from datetime import datetime, date
import holidays

app = Flask(__name__)
calendar.setfirstweekday(calendar.SUNDAY)

@app.route('/', methods=['GET', 'POST'])
def index():
    now = datetime.now()
    
    # Default to current month only
    start_year = now.year
    start_month = now.month
    end_year = now.year
    end_month = now.month

    if request.method == 'POST':
        try:
            start_year = int(request.form.get('start_year'))
            start_month = int(request.form.get('start_month'))
            end_year = int(request.form.get('end_year'))
            end_month = int(request.form.get('end_month'))
        except (ValueError, TypeError):
            pass

    # Normalize dates
    start_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)
    
    if start_date > end_date:
        end_year, end_month = start_year, start_month

    calendars_data = [] # List of dicts: {year, month, weeks_data}
    
    current_year = start_year
    current_month = start_month

    lunar_cal = KoreanLunarCalendar()
    
    # Initialize Holiday Objects
    # Note: Holidays library handles years automatically when we query
    kr_holidays = holidays.KR()
    us_holidays = holidays.US()

    while True:
        # Generate data for current_year, current_month
        cal = calendar.monthcalendar(current_year, current_month)
        month_weeks = []
        
        for week in cal:
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append(None)
                else:
                    curr_date = date(current_year, current_month, day)
                    lunar_cal.setSolarDate(current_year, current_month, day)
                    lunar_text = f"{lunar_cal.lunarMonth}.{lunar_cal.lunarDay}"
                    
                    # Holiday Check
                    is_holiday = False
                    holiday_list = []
                    
                    if curr_date in kr_holidays:
                        is_holiday = True
                        holiday_list.append(kr_holidays.get(curr_date))
                    
                    if curr_date in us_holidays:
                        # Optional: Maybe different color for US? Or just list it? 
                        # User wants both. Let's append name.
                        # If it's not a KR holiday, technically it's not a red day in Korea, 
                        # but user asked to "mark" them. Let's make it red too or just list it.
                        # "한국과 미국의 국경일을 표시해줘" -> Usually implies visual marker.
                        # Let's consider US holidays as holidays too for this request.
                        is_holiday = True
                        holiday_list.append(us_holidays.get(curr_date))
                    
                    # Deduplicate names if any overlap (rare) purely by string check
                    holiday_names = ", ".join(sorted(list(set(holiday_list))))

                    week_data.append({
                        'day': day,
                        'lunar': lunar_text,
                        'is_holiday': is_holiday,
                        'holiday_name': holiday_names
                    })
            month_weeks.append(week_data)
        
        calendars_data.append({
            'year': current_year,
            'month': current_month,
            'weeks': month_weeks
        })

        # Move to next month
        if current_year == end_year and current_month == end_month:
            break
            
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        
        if len(calendars_data) > 24:
            break

    return render_template('calendar.html', 
                           start_year=start_year, start_month=start_month,
                           end_year=end_year, end_month=end_month,
                           calendars=calendars_data)

if __name__ == '__main__':
    app.run(debug=True)
