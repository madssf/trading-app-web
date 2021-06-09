import React from 'react'
import CurrencyAsset from './CurrencyAsset.js'

import sortBy from '../../utils/SortBy'


export default function Assets(props) {

    
    let totals = [{'id':props.assets[0].id, 'value': props.assets[0].value, 'symbol': props.assets[0].symbol, 'positions': [{'value': props.assets[0].value, 'exchange': props.assets[0].exchange, 'status':  props.assets[0].status, 'amount': props.assets[0].amount}]}]
    let totalsSymbols = [props.assets[0].symbol]
    let assetIds = [props.assets[0].id]
    for(var i = 1; i < props.assets.length ; i++){
      var id = props.assets[i].id
      var value = props.assets[i].value;
      var symbol = props.assets[i].symbol;
      let j = 0
      while (j < totals.length){
        if (totalsSymbols.includes(symbol)) {
          if (symbol === totals[j].symbol && (!(assetIds.includes(id)))) {

            var newPos = totals[j].positions.concat([{'value': props.assets[i].value, 'exchange': props.assets[i].exchange, 'status':  props.assets[i].status, 'amount': props.assets[i].amount}])
            totals[j]={'id':id, 'value': totals[j].value + value, 'symbol': symbol, 'positions': newPos }
            assetIds.push(id)
          }
        } else {
          if (!(assetIds.includes(id))) {
          totalsSymbols.push(symbol)
          assetIds.push(id)
          totals.push({'id':id, 'value': value, 'symbol': symbol, 'positions': [{'value': props.assets[i].value, 'exchange': props.assets[i].exchange, 'status':  props.assets[i].status, 'amount': props.assets[i].amount}]})
        }
        }
        
        j += 1;
      }
     } 
    totals = totals.sort(sortBy("value", false))
    const currencyTotals = totals.map(coin => {return <CurrencyAsset key ={coin.id} symbol={coin.symbol} value={coin.value} positions={coin.positions}/>})
      
    return (
        <div>
          {currencyTotals}    
        </div>
      )

  }

  
  


    