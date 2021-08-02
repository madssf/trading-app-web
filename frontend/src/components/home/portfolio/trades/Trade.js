import React from 'react'

export default function Trade(props) {

  const amount = props.data.amount
  const timestamp = props.data.timestamp
  return (
    <div>
      {amount} | {timestamp}

    </div>
  )
}
