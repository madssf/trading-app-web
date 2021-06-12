import React, {useState} from 'react'
import './style.css'
import TextField from '@material-ui/core/TextField';


export default function ParameterInput(props) {

    

    const TYPES = ["STRING","INT", "FLOAT", "LIST"]

    switch (props.type) {

        // STRING
        case TYPES[0]:
        return (
               <div className="paramInput string">   
                <TextField 
                label={props.type} 
                />
              </div>
        );

       // INT
        case TYPES[1]:
          return (
                 <div className="paramInput int">
              <TextField
              type={"number"} 
              label={props.type} 
              />
                </div>
          );

        // FLOAT
        case TYPES[2]:
          return (
                 <div className="paramInput float">
                <TextField  
                type="number" 
                step="0.01" 
                label={props.type} /> 
                </div>
          );

        // LIST
        case TYPES[3]:
          return (
                  <div className="paramInput list">
                  <TextField  
                  label={props.type} 
                  />
                </div>
          );
     default:
          return (
            "Unkown parameter type."
          )
 


  }
}

  
  


    