import React from 'react'

export default function Deposit(props) {

  const amount = props.data.amount
  const timestamp = props.data.timestamp
  return (
    <div>
      {amount} | {timestamp}

    </div>
  )
}
