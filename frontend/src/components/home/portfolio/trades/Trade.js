import React from 'react'

export default function Trade(props) {
  props = props.data
  return (
    <div>
      {props.buy_currency.symbol} | {props.sell_currency.symbol} | {props.amount} | {props.price}
    </div>
  )
}
