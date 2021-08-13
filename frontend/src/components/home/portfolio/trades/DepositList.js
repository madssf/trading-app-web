import React from 'react'
import Deposit from './Deposit'

export default function DepositList(props) {
  const deposits = props.deposits.map(deposit => {return <Deposit key={deposit.id} data={deposit}/>})
  return (
    <div>
      {deposits}
    </div>
  )
}
