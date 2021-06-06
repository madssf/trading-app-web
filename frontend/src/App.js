import './App.css';
import React, { Component } from "react";
import Root from "./Root";
import { Route, Switch, BrowserRouter } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import requireAuth from "./utils/RequireAuth";
import Landing from "./components/Landing";
import Signup from "./components/signup/Signup";
import Login from "./components/login/Login";
import Home from "./components/home/Home";
//import MyPortfolioList from "./components/home/MyPortfolioList";


import Logout from "./components/login/Logout";

import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:1337";


class App extends Component {
  render() {
    return (
      <div>
        <Root> 
          <Switch>
            <Route exact path="/" component={Landing} />
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <Route path="/home" component={requireAuth(Home)}/>
            <Route path="*">404 - Not found</Route>
          </Switch>
       
        </Root>
        <ToastContainer hideProgressBar={true} newestOnTop={true} />
      </div>
    );
  }
}

export default App;