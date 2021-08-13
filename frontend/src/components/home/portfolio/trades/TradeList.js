import React from 'react'
import Trade from './Trade'

export default function TradeList(props) {
  if (props.currencies === undefined || props.trades.length === 0) {
    return "No trades"
  }
  const currencies = props.currencies.currencies.sort((a, b) => {
    return a.id - b.id} )
  

  let trades = props.trades

  let tradedCurrencies = trades.map(trade => trade.buy_currency)

  tradedCurrencies = [...new Set(tradedCurrencies)].sort((a,b) => {
    return a-b
  })

  let currencyIndex  = 0
  let tradesIndex = 0
  while (currencyIndex < currencies.length) {
    
    if (tradedCurrencies[tradesIndex] === currencies[currencyIndex].id) {
      
        tradedCurrencies[tradesIndex] = currencies[currencyIndex]
        tradesIndex += 1
  
    }
    currencyIndex += 1
    
  }
  
  for (let i = 0; i < trades.length; i++) {
    let buyId = trades[i].buy_currency
    let index = 0
    while (trades[i].buy_currency === buyId  && index < tradedCurrencies.length) {
      if (buyId === tradedCurrencies[index].id) {
        trades[i].buy_currency = tradedCurrencies[index]
      }
      index += 1
    }
  }
  
  for (let i = 0; i < trades.length; i++) {
    let sellId = trades[i].sell_currency
    let index = 0
    while (trades[i].sell_currency === sellId && index < tradedCurrencies.length) {
      if (sellId === tradedCurrencies[index].id) {
        trades[i].sell_currency = tradedCurrencies[index]
      }
      index += 1
    }
  }

  trades = trades.map(trade => {return <Trade key ={trade.id} data={trade}/>})
  return (
    <div>
      {trades}
    </div>
  )
}
