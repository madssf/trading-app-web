import React from 'react'
import Trade from './Trade'

export default function TradeList(props) {
  const currencies = props.currencies

  console.log(currencies)

  let trades = props.trades
  let tradedCurrencies = trades.map(trade => trade.buy_currency)//.push(trades.map(trade => trade.sell_currency))

  tradedCurrencies = [...new Set(tradedCurrencies)].sort((a,b) => {
    return a-b
  })
  
  console.log(tradedCurrencies)
  var i = 0
  while (tradedCurrencies.length !== 0 && i < currencies.length) {
   
  }

  console.log(trades)

  trades = trades.map(trade => {return <Trade key ={trade.id} data={trade}/>})
  return (
    <div>
      {trades}
    </div>
  )
}
