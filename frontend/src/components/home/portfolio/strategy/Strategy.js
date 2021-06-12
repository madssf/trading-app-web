import React from 'react'
import {Button} from 'react-bootstrap'
import StrategyParameter from './StrategyParameter'
export default function Strategy(props) {


    if (props.data.parameters.length === 0 || props.data.parameters === undefined) {
      return "No parameters for this strategy."
    }

    console.log(props)
      
    let params = props.data.parameters.map(param => {return <StrategyParameter key={param.name} data={param} />})
    return (
        <div className="strategy">
          
          <h1>{props.data.name}</h1>


          {params}
          <Button>Simulate</Button>
          <Button>Execute</Button>

        </div>

        
      )
      

  }

  
  


    