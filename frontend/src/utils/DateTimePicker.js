import React, { useState } from 'react';
import DatePicker from 'react-datetime';
import moment from 'moment';
import 'react-datetime/css/react-datetime.css';

function DateTimePicker() {
  const [dt, setDt] = useState(moment());
  return (
    <div className="DateTimePicker">
      <DatePicker
        inputProps={{
          style: { width: 250 }
        }}
        value={dt}
        dateFormat="DD-MM-YYYY"
        timeFormat="hh:mm A"
        onChange={val => setDt(val)}
      /> <br />
      <div><b>Date:</b> {dt.format('LLL')}</div>
    </div>
  );
}

export default DateTimePicker;