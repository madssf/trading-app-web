import React, {useState} from 'react'
import {Button} from 'react-bootstrap'

import Asset from './Asset'
export const CurrencyAsset = (props) => {
  const symbol = props.symbol
  const value = Math.round(props.value *100)/100
  let positions = []

  const [open, setOpen] = useState(false);
  
  let assets = 0
  if (props.positions !== undefined) {
    positions = props.positions.map(asset => {return <Asset key={asset.id+asset.status+asset.exchange} symbol={props.symbol} asset={asset}/>})
    assets = props.positions.length
  }

  return (
    <div>

         
    <Button className="currencyAssetBtn" onClick={() => setOpen(prev => !prev)}>{symbol}</Button>
    {value} $ | {assets}
    {props.positions !== undefined && open ? positions : []}

    </div>
    
  )
}

export default CurrencyAsset
