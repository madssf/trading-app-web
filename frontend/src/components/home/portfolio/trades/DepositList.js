import React from 'react'
import Deposit from './Deposit'

export default function DepositList(props) {
  const deposits = props.deposits.map(deposit => {return <Deposit data={deposit}/>})
  return (
    <div>
      {deposits}
    </div>
  )
}
