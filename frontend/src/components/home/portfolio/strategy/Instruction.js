import React from 'react'

export default function Instruction(props) {
  return (
    <div>
      <b>{props.data.side} </b> | {props.data.symbol} | {props.data.fiat} | {props.data.tokens}
    </div>
  )
}
