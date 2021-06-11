import React, { Component } from "react";
import {Link} from 'react-router-dom'
import { logout } from "../auth/login/LoginActions";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import PropTypes from "prop-types";
import Updated from './Updated'
import './style.css'

class NavBar extends Component {
  onLogout = () => {
    this.props.logout();
  };
  render () {
    
    
    return (
      <div className='nav'>
        {this.props.auth.isAuthenticated === false ? <p><Link to="/">Front Page</Link></p>: ""} 
        {this.props.auth.isAuthenticated === true ? <p><Link to="/home">Home</Link></p> : ""}
        {this.props.auth.isAuthenticated === false ? <p><Link to="/login">Log in</Link></p>: ""}
        {this.props.auth.isAuthenticated === false ? <p><Link to="/signup">Sign up</Link></p>: ""}
        {this.props.auth.isAuthenticated === true ? <Updated />: ""}
        {this.props.auth.isAuthenticated === true ? <p><button className="navLogout" onClick={this.onLogout}>Logout</button></p> : ""}
        
      </div>
    );
  }
}


NavBar.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired,
};

const mapStateToProps = state => ({
  auth: state.auth,

});

export default connect(mapStateToProps, {
  logout
})(withRouter(NavBar));
