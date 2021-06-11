import React, {useState} from 'react'

import Asset from './Asset'
export const CurrencyAsset = (props) => {
  const symbol = props.symbol
  const value = Math.round(props.value *100)/100
  let positions = []

  const [open, setOpen] = useState(false);
  
  if (props.positions !== undefined) {
    positions = props.positions.map(asset => {return <Asset key={asset.id+asset.status+asset.exchange} symbol={props.symbol} asset={asset}/>})
  }

  return (
    <div className="currencyAsset">

         
    <button className="currencyBtn" onClick={() => setOpen(prev => !prev)}>
      <b>{symbol}</b> | {value} $ | {props.positions.length}
    </button>
    <div className="positions">
    {props.positions !== undefined && open ? positions : []}
    </div>
    </div>
    
  )
}

export default CurrencyAsset
