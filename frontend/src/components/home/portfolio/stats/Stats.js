import React from 'react'

export default function Stats(props) {
  return (
    <div>
      <h2>Portfolio stats</h2>
      <b>Deposited</b> | {props.portfolio.stats.deposit_total}
    </div>
  )
}
