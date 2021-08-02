import React from 'react'
import Trade from './Trade'

export default function TradeList(props) {
  const trades = props.trades.map(trade => {return <Trade id ={trade.id} data={trade}/>})
  return (
    <div>
      {trades}
    </div>
  )
}
