import React, {useState} from 'react'

import Position from './Position'
export const Asset = (props) => {
  
  const total = Math.round(props.total *100)/100

  const data = props.data
  const symbol = data.symbol
  const amount = data.amount.toString().substring(0,6)
  const average = Math.round(data.average*100)/100
  const last_price = data.last_price.toString().substring(0,6)
  const pct_change_24h = Math.round(data.pct_change_24h*100)/100
  const gain = Math.round(10000*(data.last_price - average)/average)/100

  const [open, setOpen] = useState(false);
  
  let positions = []
  if (props.data.positions !== undefined) {
    positions = data.positions.map(position => {return <Position key={position.id} data={position}/>})
  }

  return (
    <div className="currencyAsset">

         
    <button className="currencyBtn" onClick={() => setOpen(prev => !prev)}>
      <b>{symbol}</b>x{positions.length} | {amount}/<b>{total} $</b> | {last_price} $ / {pct_change_24h}% | {average} $ / {gain} %
 
    </button>
    <div className="positions">
    {data.positions !== undefined && open ? positions : []}
    </div>
    </div>
    
  )
}

export default Asset
