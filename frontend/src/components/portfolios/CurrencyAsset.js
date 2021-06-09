import React, {useState} from 'react'
import {Button} from 'react-bootstrap'

import Asset from './Asset'
export const CurrencyAsset = (props) => {
  const symbol = props.symbol
  const value = Math.round(props.value *100)/100
  const positions = props.positions.map(asset => {return <Asset key={asset.id+asset.status+asset.exchange} symbol={props.symbol} asset={asset}/>})

  const [open, setOpen] = useState(false);
  
  return (
    <div>

    <b>{symbol}</b> { value} $     
    <Button onClick={() => setOpen(prev => !prev)} />
    
    {props.positions !== undefined && open ? positions : []}

    </div>
    
  )
}

export default CurrencyAsset
