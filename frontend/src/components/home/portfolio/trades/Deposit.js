import React from 'react'

export default function Deposit(props) {

  const amount = props.data.amount
  
  return (
    <div>
      {amount}
    </div>
  )
}
