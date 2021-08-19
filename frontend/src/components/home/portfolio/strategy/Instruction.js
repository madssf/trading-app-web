import React from 'react'
import AutoFillTradeButton from './AutoFillTradeButton'

export default function Instruction(props) {
  return (
    <div className="instruction">
      <b>{props.data.side} </b> | {props.data.symbol} | {props.data.fiat} $ | {props.data.tokens} tokens 
      <AutoFillTradeButton data={props.data} portfolio={props.portfolio} currencies={props.currencies} />
    </div>
  )
}
