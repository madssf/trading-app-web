import React, {useState} from 'react';
import axios from 'axios';
import {Container, Button} from "react-bootstrap";
import {toastOnError} from "../../../../utils/Utils";

import DatePicker from 'react-datetime';
import moment from 'moment';
import 'react-datetime/css/react-datetime.css';

import Dropdown from '../../../ui/Dropdown';
import "./style.css"
export default function AddTrade(props) {

  const currencies = props.currencies.currencies
  const exchanges = props.exchanges.exchanges


  const [exchange, setExchange] = useState(null)
  const [currency, setCurrency] = useState(null)
  const [amount, setAmount] = useState(null)
  const [timestamp, setTimestamp] = useState(moment())
  const [canSubmit, setCanSubmit] = useState(false)
  
  function checkForm() {
  if (exchange != null && currency != null && amount != null) {
    setCanSubmit(true)
  } else {
    setCanSubmit(false)
  }
  }




  function handleSubmit() {
   

    const deposit = {
      portfolio: props.portfolio, 
      exchange: exchange.id,
      currency: currency.id,
      amount: amount,
      timestamp: timestamp
    };

    axios.post(`http://localhost:1337/api/v1/deposits/`, deposit, {headers: {
      'Content-Type': 'application/json'
  }})
      .then(res => {
        window.location.reload();
      }).catch(error => {
        toastOnError(error);
      });    
  }


  return (
      <div className="addTradeForm">
      <Container>
        <h2>Add Deposit</h2>
      <Container>
       <input className="amountInput" type="number" step="0.001"name="amount" placeholder="Deposit amount" onChange={event => {setAmount(event.target.value); checkForm()}} />
      <Button className="action" onClick={handleSubmit} disabled={!canSubmit} type="submit">Add</Button>
        
      </Container>
        <div className="dropdowns" >
          
          <Dropdown 
          options={currencies} 
          prompt="Deposited currency..."
          id='id'
          label='name'
          value={currency}
          onChange={val => {setCurrency(val); checkForm()}}
          />

          <Dropdown 
          options={exchanges} 
          prompt="Select an exchange..."
          id='id'
          label='name'
          value={exchange}
          onChange={val => {setExchange(val); checkForm()}}
          />

          <div className="DateTimePicker">
            <DatePicker
            inputProps={{
              style: { width: 250 }
            }}
            value={timestamp}
            dateFormat="DD-MM-YYYY"
            timeFormat="hh:mm A"
            onChange={val => {setTimestamp(val); checkForm()}}
            /> 
          </div>
          

           
        </div>
        

      </Container>
      </div>
    )
}
