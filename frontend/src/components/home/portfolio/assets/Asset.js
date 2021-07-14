import React, {useState} from 'react'

import Position from './Position'
export const Asset = (props) => {
  
  const data = props.data
  const symbol = data.symbol
  const value = Math.round(props.value *100)/100

  const [open, setOpen] = useState(false);
  
  let positions = []
  if (props.data.positions !== undefined) {
    positions = data.positions.map(position => {return <Position key={position.id} data={position}/>})
  }

  return (
    <div className="currencyAsset">

         
    <button className="currencyBtn" onClick={() => setOpen(prev => !prev)}>
      <b>{symbol}</b> | {value} $ | {positions.length} | 
    </button>
    <div className="positions">
    {data.positions !== undefined && open ? positions : []}
    </div>
    </div>
    
  )
}

export default Asset
