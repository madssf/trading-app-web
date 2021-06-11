import React, { Component } from "react";
import {Link} from 'react-router-dom'
import { logout } from "../auth/login/LoginActions";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import PropTypes from "prop-types";
import {Button} from 'react-bootstrap'
import Updated from "./Updated";
class NavBar extends Component {
  onLogout = () => {
    this.props.logout();
  };
  render () {
    
    
    return (
      <div className='nav'>
        {this.props.auth.isAuthenticated !== true ? <p><Link to="/">Front Page</Link></p> : <p><Link to="/home">Home</Link></p>}
         {this.props.auth.isAuthenticated === true ? <p> user: {this.props.auth.user.username}</p>: ""}
        {this.props.auth.isAuthenticated === true ? <Updated />: ""}
        {this.props.auth.isAuthenticated === true ? <p><Button className="navLogout" onClick={this.onLogout}>Logout</Button></p> : ""}
      </div>
    );
  }
}


NavBar.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
  logout
})(withRouter(NavBar));