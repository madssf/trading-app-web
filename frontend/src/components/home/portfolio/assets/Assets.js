import React, {useState} from 'react'
import Asset from './Asset.js'

import sortBy from '../../../../utils/SortBy'
import PieChart from '../graphs/PieChart.js'
import AddPosition from './AddPosition';
import BatchAddPosition from './BatchAddPosition';
import {Button} from "react-bootstrap";


export default function Assets(props) {
      
    
    const [showAdd, toggleShowAdd] = useState(false)
    const [showBatchAdd, toggleShowBatchAdd] = useState(false)

    if (props.portfolio.assets === undefined) {
      return <div style={{margin: "20px"}}>Please add your first asset, or register credentials to fetch balances automatically.</div>
    }


    let assets = props.portfolio.assets
    for(var i = 0; i < props.portfolio.assets.length ; i++){
      if (assets[i].positions.length > 1) {
        assets[i].total = assets[i].positions.reduce((a, b) => a.value + b.value)

      } else {
        assets[i].total = assets[i].positions[0].value
      } 

      
    }
    
    assets = assets.sort(sortBy("total", false))
    const assetComponents = assets.map(asset => {return <Asset key={asset.id} total={asset.total} data={asset} />})

          
      
    return (
        <div className="assets">
          <PieChart labels={assets.map(asset => asset.symbol)} data={assets.map(asset => asset.total)}/>
    
          {assetComponents}    

          <Button className="toggleView" onClick={() => toggleShowAdd(!showAdd)}>{showAdd ? "Close" : "Add positon"}</Button>
          <Button className="toggleView" onClick={() => toggleShowBatchAdd(!showBatchAdd)}>{showBatchAdd ? "Close" : "Batch add positons"}</Button>
          {showAdd ?  
          <AddPosition portfolio={props.portfolio.id} currencies={props.currencies} exchanges={props.exchanges}/>
            : ""}
          {showBatchAdd ?  
          <BatchAddPosition portfolio={props.portfolio.id} exchanges={props.exchanges}/>
            : ""}

        </div>
      )

  }


  


    