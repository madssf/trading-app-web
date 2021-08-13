import React from 'react'

export default function Trade(props) {
  props = props.data
  return (
    <div>
      {props.buy_currency} | {props.sell_currency} | {props.amount} | {props.price}
    </div>
  )
}
