import React, {useState} from 'react'

import Position from './Position'
export const Asset = (props) => {
  
  const data = props.data
  const symbol = data.symbol
  const total = Math.round(props.total *100)/100
  const last_price = Math.round(data.last_price*100)/100
  const pct_change_24h = Math.round(data.pct_change_24h*100)/100

  const [open, setOpen] = useState(false);
  
  let positions = []
  if (props.data.positions !== undefined) {
    positions = data.positions.map(position => {return <Position key={position.id} data={position}/>})
  }

  return (
    <div className="currencyAsset">

         
    <button className="currencyBtn" onClick={() => setOpen(prev => !prev)}>
      <b>{symbol}</b> | <b>{total} $</b> | {last_price} $ | {pct_change_24h}% | {positions.length}

    </button>
    <div className="positions">
    {data.positions !== undefined && open ? positions : []}
    </div>
    </div>
    
  )
}

export default Asset
