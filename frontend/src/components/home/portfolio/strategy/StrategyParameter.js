import React, {useState} from 'react'
import './style.css'
import axios from 'axios';
import {toastOnError} from "../../../../utils/Utils";
import TextField from '@material-ui/core/TextField';

import {Button} from 'react-bootstrap'


export default function StrategyParameter(props) {

    const [val, setVal] = useState(props.data.value)

     const handleChange = (event) => {
      setVal(event.target.value)
    }
    const handleDelete = event => {
    
      axios.delete(`http://localhost:1337/api/v1/portfolio_parameters/${props.data.pf_param_id}/`, {headers: {
          'Content-Type': 'application/json'
          }})
          .then(res => {
            window.location.reload();
          }).catch(error => {
            toastOnError(error);
          });
    
    }

    const handleSubmit = event => {
   
      event.preventDefault();


      const parameter = {
          portfolio: props.portfolio.id, 
          parameter: props.data.strat_param_id,
          value: val
      }
      console.log(parameter)
      
      if (props.data.value) {
        axios.put(`http://localhost:1337/api/v1/portfolio_parameters/${props.data.pf_param_id}/`, parameter, {headers: {
          'Content-Type': 'application/json'
          }})
          .then(res => {
            window.location.reload();
          }).catch(error => {
            toastOnError(error);
          });

      } else {
        axios.post(`http://localhost:1337/api/v1/portfolio_parameters/`,  parameter, {headers: {
        'Content-Type': 'application/json'
        }})
        .then(res => {
          window.location.reload();
        }).catch(error => {
          toastOnError(error);
        });
      }
  }

    return (
      <div>
      <div className="stratParam">
              <p className="name">{props.data.name}</p><p className="value">{props.data.value ? props.data.value : ""}</p>

              <div className="paramInput string">   
                <TextField 
                label={props.data.type} 
                onChange={handleChange}
                />
              </div>

              <Button 
              disabled={val === "" || val === null || val === props.data.value}
              onClick={handleSubmit}
              >
                {props.data.value ? "Edit" : "Add"}
              </Button>
              <Button 
              disabled={props.data.value === null}
              onClick = {handleDelete}
              >
                Delete
              </Button>

          <p className="description">{props.data.description}</p>
          </div>
          <hr />

          </div>
    );

  }


  
  


    