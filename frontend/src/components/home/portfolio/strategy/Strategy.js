import React from 'react'
import {Button} from 'react-bootstrap'
import StrategyParameter from './StrategyParameter'
export default function Strategy(props) {



    if (props.data.strategy.parameters.length === 0 || props.data.strategy.parameters === undefined) {
      return "No parameters for this strategy."
    }

      
    let params = props.data.strategy.parameters.map(param => {
      
      return <StrategyParameter key={param.strat_param_id} portfolio={props.data} data={param} />

    })
    return (
        <div className="strategy">
          
          <h1>{props.data.name}</h1>
          <Button className="action ">Change</Button>


          <p>Difference bar chart</p>
          <p>Balanced portfolio chart</p>
          <p>Trading instructions</p>


          <div className="strategyBtns">
          <Button className="action">Execute</Button>
          <Button className="action">Schedule</Button>
          <Button className="action">Simulate</Button>
          </div>

       
          {params}

       
        </div>

        
      )
      

  }

  
  


    