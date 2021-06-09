import React from 'react'
import Asset from './Asset.js'
import CurrencyAsset from './CurrencyAsset.js'

import sortBy from '../../utils/SortBy'


export default function Assets(props) {
  //if (props.assets !== undefined){
    let assets = props.assets.sort(sortBy("value", false)).map(asset => {return <Asset key={asset.id} asset={asset} exchanges={props.exchanges}/>})
    let totals = [{'id':props.assets[0].id, 'value': props.assets[0].value, 'symbol': props.assets[0].symbol}]
    let totalsSymbols = [props.assets[0].symbol]
    for(var i = 1; i < props.assets.length ; i++){
      var id = props.assets[i].id
      var value = props.assets[i].value;
      var symbol = props.assets[i].symbol;
      let j = 0
      while (j < totals.length){
       
        if (totalsSymbols.includes(symbol)) {
          if (symbol === totals[j].symbol) {
            totals[j]={'id':id, 'value': totals[j].value + value, 'symbol': symbol}
          }
        } else {
          totalsSymbols.push(symbol)
          totals.push({'id':id, 'value': value, 'symbol': symbol})
        }
        
        j += 1;
      }
     } 

    const currencyTotals = totals.map(coin => {return <CurrencyAsset key ={coin.id} symbol={coin.symbol} value={coin.value}/>})
      
    return (
        <div>
          {currencyTotals}

          {assets}
    
        </div>
      )

  }

  
  


    