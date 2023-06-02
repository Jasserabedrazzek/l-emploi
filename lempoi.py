import streamlit as st
import pandas as pd
import numpy as np
import datetime
import streamlit.components.v1 as components

# Define the HTML code for the calendar widget
calendar_html = """
<style>
    .widget-calendar {
        width: 100%;
        height: 500px;
        border: none;
    }
</style>
<div id="calendar" class="widget-calendar"></div>
<script>
    // Initialize the calendar widget
    const calendar = new FullCalendar.Calendar(document.getElementById('calendar'), {
        // Customize the calendar options here
        initialView: 'dayGridMonth'
        // Add more options as needed
    });

    // Render the calendar
    calendar.render();
</script>
"""

# Render the calendar widget using the HTML code
components.html(calendar_html, scrolling=True)
# Sample event data
events = []

for i in range(1, 19):
    event_name = st.text_input(f'Event {i}:')
    event_date = st.date_input("When's?", datetime.date(2019, 7, i))
    events.append({'Event': event_name, 'Date': str(event_date)})

# Convert event data to a Pandas DataFrame
df = pd.DataFrame(events)

# Display the table using Streamlit
st.table(df)
