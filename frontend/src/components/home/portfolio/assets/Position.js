import React, { Component } from 'react'
import { toastOnError } from "../../../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";
import moment from 'moment'
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getExchanges} from '../../../store/ExchangesActions'
import { Container } from 'react-bootstrap';


class Position extends Component {
  constructor(props) {
    super(props);
    this.state = {
      deleteConfirm: false,
    };
  }

  

  
    handleDeleteClick= event => {
      if (this.state.deleteConfirm) {
        this.handleDelete()
      } else {
        this.setState({deleteConfirm: true})
      }
    }
    handleDelete= event => {

  
      axios.delete(`http://localhost:1337/api/v1/portfolio_assets/${this.props.data.id}/`)
        .then(res => {
          window.location.reload();
        }).catch(error => {
          toastOnError(error);
        });
  
      
    }   
  
  render() {
    
  
    return (
      <Container>
        <hr />

      <div className="assetGrid">
        <div className="assetGrid1_1">
         {this.props.data.exchange} 
        </div>
        <div className="assetGrid2_1">
        <b>{Math.round(this.props.data.value*100)/100} $ </b>
       </div>
       <div className="assetGrid3_1">
       {this.props.data.status}    
       </div>
       <div className="assetGrid4_1">
       {this.props.data.source}   
       </div>
       <div className="assetGrid5_1">
       <button className="deleteAssetBtn" onClick={this.handleDeleteClick} type="submit">{this.state.deleteConfirm ? "Confirm" : "Delete"}</button>
       </div>
       {this.props.data.stake_end !== null ? 
      <> 
       <div className="assetGrid1_2">
       Expires: {moment(this.props.data.stake_end).format("DD/MM/yy")}   
       </div>
       <div className="assetGrid2_2">
       APR: {this.props.data.apr*100} %   
       </div>
       </>

       : ""}
      </div>      
      <hr />
      </Container>
      
    
    )
  }
}

Position.propTypes = {
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getExchanges})(withRouter(Position))