import React, { useState } from 'react'
import axios from 'axios';
import moment from 'moment';
import { Button } from 'react-bootstrap'
import {toastOnError} from "../../../../utils/Utils";


export default function AutoFillTradeButton(props) {

  const autoData = {
    exchangeId: 1
  }

  const tradeData = props.data

  const [confirm, setConfirm] = useState(false)

  const autoFill = (trade) => {
    setConfirm(!confirm)
    if (confirm) {
      handleSubmit()
    }
  }
  
  const getCurrencyIdFromSymbol = (symbol) => {
    const symbolIndex = props.currencies.currencies.findIndex((element) => element.symbol === symbol)
    return props.currencies.currencies[symbolIndex].id
  }

  const symbol = getCurrencyIdFromSymbol(tradeData.symbol)
  const fiatSymbol = getCurrencyIdFromSymbol("USDT")
  
  const handleSubmit = () => {
    
    const trade = {
      portfolio: props.portfolio.id, 
      exchange: autoData.exchangeId,
      buy_currency: tradeData.side === "BUY" ? symbol : fiatSymbol,
      sell_currency: tradeData.side === "SELL" ? symbol : fiatSymbol,
      amount: tradeData.fiat.toFixed(10),
      price: (tradeData.fiat/tradeData.tokens).toFixed(10),
      timestamp: moment(),
    };
    
    axios.post(`http://localhost:1337/api/v1/trades/`, trade, {headers: {
      'Content-Type': 'application/json'
    }})
      .then(res => {
        window.location.reload();
      })
        .catch(error => {
          toastOnError(error);
      });
       
  }
  
  return (
      <Button
        variant="outline-dark"
        size="sm"
        onClick={() => autoFill(props)}
      >
        {confirm ? 'Confirm' : 'Fill'}
      </Button>
  )
}

