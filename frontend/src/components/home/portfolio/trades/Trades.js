import React from 'react'
import AddTrade from './AddTrade'
import AddDeposit from './AddDeposit'
import DepositList from './DepositList'
import TradeList from './TradeList'

export default function Trades(props) {
  return (
    <div>
      <AddTrade portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies} />
      <TradeList trades ={props.portfolio.trades} currencies={props.currencies}/>
      <AddDeposit portfolio={props.portfolio.id} exchanges={props.exchanges} currencies={props.currencies}/>
      <DepositList deposits={props.portfolio.deposits} />
    </div>
  )
}

